import os
import sqlite3
from datetime import datetime
from pytz import timezone
import random
from unidecode import unidecode
import pandas as pd
import json

class Singleton(type):

    __instances ={}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class ConnectionDB(metaclass=Singleton):

    def __init__(self,name='Banco_de_Dados_ENGESEP'):
#        print('Banco de dados inicializado')
        self.name = name
        self.name_db = 'usina_db.db'
        self.BASE_DIR = os.path.expanduser("~")
        db_file = os.path.join(self.BASE_DIR,'DBEngesep',self.name_db)
#        print(db_file)
        if not os.path.isfile(db_file):
            os.makedirs(os.path.join(self.BASE_DIR,'DBEngesep'))
            con = self.create_connection()
            cursor = con.cursor()
            con.close()

    def __call__(self):
        return self

    def create_connection(self):
        db_path = os.path.join(self.BASE_DIR,'DBEngesep',self.name_db)
        con = sqlite3.connect(db_path)
        return con

    def list_tables(self):
        con = self.create_connection()
        cursor = con.cursor()
        query_list = "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%';"
        cursor.execute(query_list)
        dados = []
        for linha in cursor.fetchall():
            dados.append(list(linha))
        con.close()
        return dados

    def create_table_unit(self, name_table)->bool:
        try:
            con = self.create_connection()
            cursor = con.cursor()
            query_create = f"CREATE TABLE IF NOT EXISTS {name_table}(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,container text,criado_em DATE NOT NULL,ts timestamp)"
            test = cursor.execute(query_create)
            con.close()
            return True
        except:
            return False

    def create_table(self,tabela):
        try:
            print('Criando tabela do banco de dados', tabela)
            con = self.create_connection()
            cursor = con.cursor()
            query_create = f"CREATE TABLE IF NOT EXISTS {tabela}(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,energia_a real,energia_b real,id_a text,id_b text,nivel real,cidade text,usina text,ip_a text,ip_b text,registro_a text,registro_b text,registro_nivel text,criado_em DATE NOT NULL,ts timestamp)"
            test = cursor.execute(query_create)
            return True
        except:
            return False

    def create_table_b(self,tabela):
        try:
            MWARRAY = {
                'acumulada': ' text',
                'distribuidor': ' text',
                'potencia_ativa_real': ' text',
                'potencia_ativa_solicitada': ' text',
                'fp': ' text',
                'pressao_oleo': ' text',
                'temperatura_UHRLM': ' text',
                'temperatura_UHRV': ' text',
                'velocidade': ' text',
            }
            con = self.create_connection()
            cursor = con.cursor()
            query = f"CREATE TABLE IF NOT EXISTS {tabela} (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, criado_em DATE NOT NULL, nivel_agua text, "
            for name,value in MWARRAY.items():
                query += name + value + ','
            query += 'frequencia text)'
            print(query)
            #query_create = f"CREATE TABLE IF NOT EXISTS {tabela}(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,energia_a real,energia_b real,id_a text,id_b text,nivel real,cidade text,usina text,ip_a text,ip_b text,registro_a text,registro_b text,registro_nivel text,criado_em DATE NOT NULL,ts timestamp)"
#            test = cursor.execute(query)
            # print('Test',test)
            return True
        except Exception as e:
            print('erro: ', e)
            return False
    def seeddbB(self):
        # con = self.create_connection()
        # cursor = con.cursor()
        tabela = "CGH TESTE"
        name_table = 'table_' + unidecode.unidecode(tabela).replace(' ','_')
        print(name_table)
        # query_create = f"CREATE TABLE IF NOT EXISTS {name_table}(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,energia_a real,energia_b real,id_a text,id_b text,nivel real,cidade text,usina text,ip_a text,ip_b text,registro_a text,registro_b text,registro_nivel text,criado_em DATE NOT NULL,ts timestamp)"
        # cursor.execute(query_create)
        i = 0
        acumulado_a = 0
        acumulado_b = 0
        nivel_m = 1000
        dados = []
        alta = 0
        baixa = 0
        z= 7
        aux = 0
        energia1 = 0
        energia2 = 0
        flag = 0
        for ano in range(0,2):
            for mes in range(1, 13):
                for dia in range(1, 32):
                    for horas in range(0, 24):
                        aux = -1
                        for minutos in range(0, 59):
                            # try:
                            aux +=1
                            i += 1
                            anos = 2020 +ano
                            # print(anos, mes, dia, horas, aux, 5, 299)

                            if anos == 2021 and mes >= 10:
                                break
                            colunas = ['criado_em','cidade','nome','nivel_agua',
                                       'acumulada_tb_ug01','acumulada_tb_ug02','distribuidor_tb_ug01',
                                       'distribuidor_tb_ug02','potencia_ativa_real_ug01','potencia_ativa_real_ug02',
                                       'potencia_ativa_solicitada_ug01','potencia_ativa_solicitada_ug2','fp_ug01',
                                       'fp_ug02','pressao_oleo_ug01','pressao_oleo_ug02','temperatura_ug01',
                                       'temperatura_ug02']
                            # data
                            try:
                                min_date = datetime(anos, mes, dia, horas, aux, 5, 299)
                            except:
                                break
                            timestamp = datetime.timestamp(min_date)
                            fuso_horario = timezone('America/Sao_Paulo')
                            min_date = min_date.astimezone(fuso_horario)
                            if mes != flag:
                                flag = mes
                                print(i,min_date)
                            # cidade
                            cidade = "Monte Carlo"
                            # nome
                            usina = "CGH Teste"
                            # nivel de agua
                            if random.randrange(0, 10) < z:
                                nivel_m = nivel_m - random.randrange(0, 2)
                                alta += 1
                            else:
                                baixa += 1
                                nivel_m = nivel_m + random.randrange(0, 2)
                            # acumulado  e potencia real
                            potencia_ativa_real_ug01 = random.randrange(15, 35)
                            potencia_ativa_real_ug02 = random.randrange(15, 35)
                            acumulado_a += potencia_ativa_real_ug01
                            acumulado_b += potencia_ativa_real_ug02
                            # distribuidor
                            distribuidor_ug01 = 100 * random.random()
                            distribuidor_ug02 = 100 * random.random()
                            # potencia solicitada pelo motor
                            potencia_ativa_solicitada_ug1 = potencia_ativa_real_ug01 * random.gauss(2,.2)
                            potencia_ativa_solicitada_ug2 = potencia_ativa_real_ug02 * random.gauss(2,.2)
                            # fator de potencia
                            fp_ug01 = random.gauss(2,.2)
                            fp_ug02 = random.gauss(2,.2)
                            # fp_ug01 = - fp_ug01 if fp_ug01 < 0 else fp_ug01
                            # pressão do oleo
                            pressao_oleo_ug01 = 500 * random.gauss(2,.2)
                            pressao_oleo_ug02 = 500 * random.gauss(2,.2)
                            # pressão do oleo
                            temperatura_ug01 = random.randrange(40, 150,1)
                            temperatura_ug02 = random.randrange(40, 150,1)

                            dados.append([min_date,"Monte Carlo","CGH Teste",nivel_m,acumulado_a,acumulado_b,distribuidor_ug01,distribuidor_ug02,
                                     potencia_ativa_real_ug01,potencia_ativa_real_ug02,potencia_ativa_solicitada_ug1,potencia_ativa_solicitada_ug2,
                                     fp_ug01,fp_ug02,pressao_oleo_ug01,pressao_oleo_ug02,temperatura_ug01,temperatura_ug02])

        # con.close()
        df = pd.DataFrame(data=dados,columns=colunas)
        # print(df.head())
        # print("Seed Realizado!")
        return df

    def seeddb(self):
        con = self.create_connection()
        cursor = con.cursor()
        tabela = "CGH Ponte Caida"
        name_table = 'table_' + unidecode.unidecode(tabela).replace(' ','_')
        print(name_table)
        query_create = f"CREATE TABLE IF NOT EXISTS {name_table}(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,energia_a real,energia_b real,id_a text,id_b text,nivel real,cidade text,usina text,ip_a text,ip_b text,registro_a text,registro_b text,registro_nivel text,criado_em DATE NOT NULL,ts timestamp)"
        cursor.execute(query_create)
        i = 0
        nivel_m = 1000
        dados = []
        alta = 0
        baixa = 0
        z= 7
        aux = 0
        energia1 = 0
        energia2 = 0
        for ano in range(0,3):
            for mes in range(1, 13):
                for dia in range(1, 32):
                    for horas in range(0, 24):
                        aux = 0
                        for minutos in range(0, 4):
                            try:
                                i += 1
                                ip_a = '198.162.10.3'
                                ip_b = '198.162.10.3'
                                anos = 2019 +ano
                                if anos == 2021 and mes >= 6:
                                    break
                                min_date = datetime(anos, mes, dia, horas, aux, 5, 299)
                                id_a = 'UG-01'
                                id_b = 'UG-02'
                                ip_a = '192.168.10.2'
                                ip_b = '192.168.10.2'
                                registro_a = 'MW1326'
                                registro_b = 'MW1326'
                                registro_nivel = 'MW1282'
                                timestamp = datetime.timestamp(min_date)
                                fuso_horario = timezone('America/Sao_Paulo')
                                min_date = min_date.astimezone(fuso_horario)
                                cidade = "Monte Carlo"
                                usina = "CGH Ponte Caida"
                                if random.randrange(0, 10) < z:
                                    nivel_m = nivel_m - random.randrange(0, 2)
                                    alta += 1
                                else:
                                    baixa += 1
                                    nivel_m = nivel_m + random.randrange(0, 2)
                                aux += 15
                                if anos == 2019:
                                    anoss = anos
                                if anos != anoss:
                                    anoss= anos
                                    print('dados: ', energia1, energia2,ip_a, ip_b, nivel_m, id_a, id_b, cidade, usina,min_date,timestamp, alta,baixa)
                                if nivel_m > 1400:
                                    z = 6
                                if nivel_m < 600:
                                    z = 3
                                query = f"""insert into {name_table} (energia_a,energia_b,id_a,id_b,nivel, cidade, usina,ip_a,ip_b,registro_a,registro_b,registro_nivel, criado_em, ts) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                                cursor.execute(query, (energia1,energia2,id_a,id_b,nivel_m,cidade,usina,ip_a,ip_b,registro_a,registro_b,registro_nivel,min_date,timestamp))
                                con.commit()
                                energia1 = energia1 + random.randrange(5, 25)
                                energia2 = energia2 + random.randrange(15, 35)
                            except ValueError:
                                pass
        con.close()
        print("Seed Realizado!")
    def convert_str_dict(self, this_dict):
        try:
            return eval(this_dict)
        except Exception as e:
            return Exception('Erro na conversão str to dict', e)

    def convert_dict_str(self, this_dict):
        try:
            this_dict['objetos'][0]['objeto'] = None
            this_dict['objetos'][1]['objeto'] = None
            return str(this_dict)
        except Exception as e:
            return Exception('Erro na conversão dict to str', e)

    def inserir_data(self, containerx):
        try:
            data = datetime.now()
            fuso_horario = timezone('America/Sao_Paulo')
            data_hora = data.astimezone(fuso_horario)
            data_hora = data_hora.strftime('%d-%m-%Y %H:%M')
            timestamp = datetime.timestamp(data)
            name_table = containerx['geral']['name_table']
            containerx = self.convert_dict_str(containerx)
            con = self.create_connection()
            cursor = con.cursor()
            query_insert = f"insert into {name_table}(container, criado_em, ts) values (?,?,?)"
            cursor.execute(query_insert, (containerx,data_hora,timestamp))
            con.commit()
            con.close()
            print('Salvo no banco de dados com sucesso')
            return True
        except Exception as e:
            print('Erro no banco de dados', e)
            return e



    def inserir(self,tabela,energia_a,energia_b,id_a,id_b,nivel,cidade,usina,ip_a,ip_b,registro_a,registro_b,registro_nivel):
        try:
            con = self.create_connection()
            cursor = con.cursor()
            data = datetime.now()
            fuso_horario = timezone('America/Sao_Paulo')
            data_hora = data.astimezone(fuso_horario)
            data_hora = data_hora.strftime('%d-%m-%Y %H:%M')
            print(data_hora)
            print(type(data_hora))
            timestamp = datetime.timestamp(data)
            query = f"""insert into {tabela} (energia_a,energia_b,id_a,id_b,nivel, cidade, usina,ip_a,ip_b,registro_a,registro_b,registro_nivel, criado_em, ts) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
            print(timestamp)
            print('salvo com sucesso',data_hora,timestamp)
            print('----')
            print('nome tabela: ',tabela, type(tabela))
            print('energia a: ',energia_a,type(energia_a))
            print('energia b: ', energia_b, type(energia_b))
            print('id a: ',id_a,type(id_a))
            print('id b: ', id_b, type(id_b))
            print('nivel: ',nivel,type(nivel))
            print('cidade: ',cidade,type(cidade))
            print('ip a: ',ip_a,type(ip_a))
            print('ip_b: ',ip_b,type(ip_b))
            print('registro_a: ',registro_a,type(registro_a))
            print('registro_b: ',registro_b,type(registro_b))
            print('registro_nivel: ',registro_nivel,type(registro_nivel))
            cursor.execute(query, (energia_a,energia_b,id_a,id_b,nivel,cidade,usina,ip_a,ip_b,registro_a,registro_b,registro_nivel,data_hora,timestamp))
            con.commit()
            con.close()
            print('salvo com sucesso',data_hora,timestamp)
            return True
        except ValueError:
            con.close()
            return ValueError
    def inserirb(self,turbina,dados):
        try:
            MWARRAY = {
                'acumulada': ' text',
                'distribuidor': ' text',
                'potencia_ativa_real': ' text',
                'potencia_ativa_solicitada': ' text',
                'fp': ' text',
                'pressao_oleo': ' text',
                'temperatura_UHRLM': ' text',
                'temperatura_UHRV': ' text',
                'velocidade': ' text',
            }
            con = self.create_connection()
            cursor = con.cursor()
            data = datetime.now()
            fuso_horario = timezone('America/Sao_Paulo')
            data_hora = data.astimezone(fuso_horario)
            timestamp = datetime.timestamp(data)
            data_hora = data_hora.strftime('%d-%m-%Y %H:%M')
            print(dados)
            print(turbina)
            tipos = ['criado_em', 'nivel_agua']
            [tipos.append(s) for s in MWARRAY.keys()]
            query = f"""insert into {turbina} {tuple(tipos)} values (?,?,?,?,?,?,?,?,?,?,?)"""
            valores= [data_hora]
            [valores.append(s) for s in dados.values()]
            print(tuple(valores),len(valores))
            print(tuple(tipos),len(tipos))
        except Exception as e:
            raise Exception('Tipo de erro: ', e)

    def consulta(self,name_table):
        try:
            con = self.create_connection()
            cursor = con.cursor()
            query = f'SELECT * FROM {name_table}'
            cursor.execute(query)
            con.commit()
            colunas = []
            dados = []
            for d in cursor.description:
                colunas.append(d[0])
            for linha in cursor.fetchall():
                dados.append(list(linha))
            con.close()
            dado = pd.DataFrame(data=dados,columns=colunas)
            return dado
        except Exception as e:
            return False

    def delete_all(self):
        con = self.create_connection()
        cur = con.cursor()
        for s in self.list_tables():
            sql = f"""DELETE FROM {s[0]}"""
            cur.execute(sql)
            con.commit()
        con.close()
        return True

#if __name__ == "__main__":
#    banco = ConnectionDB()
#    banco.delete_all()
#    # banco.create_table_b('TESTE')
#    # dados = banco.consulta('TESTE')
#    # df = banco.seeddbB()
#    # df.to_csv('data_usina.csv')
#    # print(dados)
#    # banco.delete_all()
#    # banco.seeddb()
#    # if not banco.create_table_b('teste'):
#    #     print('Criado tabela',banco.create_table_b('teste'))
#    tabelas = banco.list_tables()
#
#
#    print(tabelas)
#    for table in tabelas:
#        dados = banco.consulta(table[0])
#        print(table[0])
#        for s in dados:
#            # print(s)
#            print('id: ',s[0])
#            print('data e hora: ',datetime.fromtimestamp(s[1]))
#            print('valor: ',s[2])
#            print('---')
#        print(len(dados))
    # colunas = ['criado_em DATE NOT NULL,',
    #            'nivel_agua text,', MW1310,
    #            'acumulada_tb_ug01 text,', MW1328,
    #            'acumulada_tb_ug02 text,', MW1328,
    #            'distribuidor_tb_ug01 text,', MW1286,
    #            'distribuidor_tb_ug02 text,', MW1286,
    #            'potencia_ativa_real_ug01 text,', MW1298,
    #            'potencia_ativa_real_ug02 text,', MW1298,
    #            'potencia_ativa_solicitada_ug01 text,', MW506,
    #            'potencia_ativa_solicitada_ug2 text,', MW506,
    #            'fp_ug01 text,', MW1301,
    #            'fp_ug02 text,', MW1301,
    #            'pressao_oleo_ug01 UHRV text,', MW1280,
    #            'pressao_oleo_ug02 text,', MW1280,
    #            'temperatura_ug01 UHRLM text,', MW1323,
    #            'temperatura_ug01 UHRV text,', MW1324,
    #            'temperatura_ug01 UHRLM text,', MW1323,
    #            'temperatura_ug01 UHRV text,', MW1324,
    #            'velocidade_ug01', MW1285,
    #            'frequencia_ug01', MW1302,
    #            'velocidade_ug02', MW1285,
    #            'frequencia_ug02', MW1302]