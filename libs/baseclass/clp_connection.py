from libs.baseclass.Exception_error import Error
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import pandas as pd
import os
import concurrent.futures
import random

error = Error()

class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class ConnectionCLP(metaclass=Singleton):

    def __init__(self):
        db_path = os.path.join(os.environ["ENGESEP_ASSETS"], 'wago_enderecos.xlsx')
        self.tabela = pd.read_excel(db_path)
        self.contador = 999

    def mapa(self,letras,numero):
        return self.tabela.query(f'{letras} == {numero}')

    def registro(self,reg):
        try:
            if not reg is None:
                s1 = reg.split()[0][0:2].upper()
                s2 = reg.split()[0][2:6].upper()
                return int(self.mapa(s1, int(s2)).DEC.values[0])
            return None
        except Exception as e:
            error.msg(e)

    def connection(self,ip):
        try:
            objeto = ModbusClient(host=ip, auto_open=True, auto_close=True)
            objeto.open()
            if objeto.is_open():
                objeto.close()
                return objeto
            else:
                return False
        except Exception as e:
            error.msg(e)


    def real_to_int(self, data: list) ->list:
        try:
            valor = list(reversed(data))
            return [utils.decode_ieee(f) for f in utils.word_list_to_long(valor)]
        except Exception as e:
            error.msg(e)


    def int_to_real(self, data: list) ->list:
        b32_l = [utils.encode_ieee(f) for f in [data]]
        return list(reversed(utils.long_list_to_word(b32_l)))


    def escrever_unit(self, objeto: object,
                      container: list) ->int:
        try:
            objeto.open()
            if objeto.is_open():
                valor =  container['value'] if not isinstance(container['tipo'], float) else self.int_to_real(container['value'])
                if isinstance(valor,list):
                    return objeto.write_multiple_registers(container['registro'], valor)
                else:
                    return objeto.write_single_register(container['registro'], valor)
            return False
        except Exception as e:
            error.msg(e)


    def leitura_unit(self, objeto: object, container: dict) ->int:
        try:
            objeto.open()
            if objeto.is_open():
                valor = objeto.read_holding_registers(container['registro'], 2)
                valor =  valor if not isinstance(container['tipo'], float) else self.real_to_int(valor)
#                container['value'] = valor[0]
                val = random.randrange(10000)
                container['value'] = val
                return container
            return None

        except Exception as e:
            error.msg(e)


    def leitura_list(self, objeto: object, addrs: dict, tipo: str)->list:
        try:
            objeto.open()
            dados = {}
            if objeto.is_open():
                for key, value in addrs.items():
                    valor = objeto.read_holding_registers(value[2], 10)
                    if not tipo == 'I':
                        try:
                            valor = list(reversed(valor))
                            valor = [utils.decode_ieee(f) for f in utils.word_list_to_long(valor)]
                        except:
                            valor = [-1,-1]
                    dados[key] = [value[2], valor[0]]
            objeto.close()
            return dados
        except Exception as e:
            error.msg(e)

    def leitura(self,objeto,addr_a,nivel,tipo):
        try:
            objeto.open()
            dados = {}
            if objeto.is_open():
                nivel_a = objeto.read_holding_registers(nivel, 10)
                energia = objeto.read_holding_registers(addr_a, 2)
                if not tipo == 'I':
                    try:
                        energia = list(reversed(energia))
                        energia = [utils.decode_ieee(f) for f in utils.word_list_to_long(energia)]
                    except:
                        energia = [19990]
                dados['nivel'] = [addr_a, nivel_a[0]]
                dados['energia'] = [addr_a, energia[0]]
#                print('--------------------')
#                print('nivel: ',nivel)
#                print('energia: ',energia)
#                print('--------------------')
                objeto.close()
                return energia[0], nivel_a[0], dados
            else:
                return None, None
        except Exception as e:
            error.msg(e)

    def run(self, ips: str)->object:
        try:
            return self.connection(ips)
        except Exception as e:
            error.msg(e)
