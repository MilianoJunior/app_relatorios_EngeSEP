from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivy.utils import (get_random_color, get_color_from_hex)
from libs.baseclass.connection_db import ConnectionDB
from libs.baseclass.clp_connection import ConnectionCLP
from kivy.clock import Clock
import asynckivy as ak
from kivymd.uix.spinner import MDSpinner
import concurrent.futures
from unidecode import unidecode
from libs.baseclass.Exception_error import Error
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget
from functools import partial
import pandas as pd

error = Error()


snackbar = None
db = None
CLP = None
entradas_ = None
objeto_ = None
clp_objeto = None
boxspinner = None
clp = []
read_data = None
dialog = None
clpa = None
clpb = None
tentativas = 0
name_table = None
tabelas_ativas = []
taxa_acerto = []
cores = {
         'primary': get_color_from_hex('#0097a7'),
         'secundary': get_color_from_hex('#56c8d8'),
         'background': get_color_from_hex('#1E1F23'),
         'background_widget': get_color_from_hex('#ffffff'),
         'text': get_color_from_hex('#000000'),
         'element': get_color_from_hex('#0D0C0F'),
         'widget': get_color_from_hex('#0D0C0F'),
         'icon_select': get_color_from_hex('#4A148C'),
         'sidebar': get_color_from_hex('#151718'),
         'linecard': get_color_from_hex('#61626d'),
         'danger': get_color_from_hex('#f04849'),
         'alert': get_color_from_hex('#fbe739'),
         'adjust': get_color_from_hex('#6200ee'),
         'check': get_color_from_hex('#2bebc8'),
         'linha1': get_color_from_hex('#1e1f22'),
         'linha2': get_color_from_hex('#28292d'),
         'gauge': get_color_from_hex('#0097a7'),
         'ligado': get_random_color(.5),
         }

box_container = {'geral': None, 'objetos':[]}

geral = {'name_usina': None,
         'localizacao': None,
         'name_table': None,
         'time_update': 15}

container = {'name': None,
             'ip': None,
             'id': None,
             'leituras': None}

container_A = {'nivel_agua': {'name': 'Nível da água',
                               'endereco': 'MW1310',
                               'registro': None,
                               'value': None,
                               'tipo': int(1)},
                'acumulada': {'name': 'Energia acumulada',
                              'endereco': 'MW1328',
                              'registro': None,
                              'value': None,
                              'tipo': int(1)},
                'distribuidor': {'name': 'Distribuidor Turbina',
                                 'endereco': 'MW1286',
                                 'registro': None,
                                 'value': None,
                                 'tipo': int(1)},
                'potencia_ar': {'name': 'Potência ativa real',
                               'endereco': 'MW1298',
                               'registro': None,
                               'value': None,
                               'tipo': int(1)},
                'potencia_as': {'name': 'Potência ativa solicitada',
                              'endereco': 'MW506',
                              'registro': None,
                              'value': None,
                              'tipo': int(1)},
                'fp': {'name': 'Fator de potência',
                       'endereco': 'MW1301',
                       'registro': None,
                       'value': None,
                       'tipo': int(1)},
                'pressao_oleo': {'name': 'Pressão do óleo',
                               'endereco': 'MW1280',
                               'registro': None,
                               'value': None,
                               'tipo': int(1)},
                'temp_UHRLM': {'name': 'Temperatura UHRLM',
                              'endereco': 'MW1323',
                              'registro': None,
                              'value': None,
                              'tipo': int(1)},
                'temp_UHRV': {'name': 'Temperatura UHRV',
                                 'endereco': 'MW1324',
                                 'registro': None,
                                 'value': None,
                                 'tipo': int(1)},
                'velocidade': {'name': 'Velocidade',
                                 'endereco': 'MW1285',
                                 'registro': None,
                                 'value': None,
                                 'tipo': int(1)},
                'frequencia': {'name': 'Frequência',
                                 'endereco': 'MW1302',
                                 'registro': None,
                                 'value': None,
                                 'tipo': int(1)},
        }

container_B = {'nivel_agua': {'name': 'Nível da água',
                               'endereco': 'MW1310',
                               'registro': None,
                               'value': None,
                               'tipo': int(1)},
                'acumulada': {'name': 'Energia acumulada',
                              'endereco': 'MW1328',
                              'registro': None,
                              'value': None,
                              'tipo': int(1)},
                'distribuidor': {'name': 'Distribuidor Turbina',
                                 'endereco': 'MW1286',
                                 'registro': None,
                                 'value': None,
                                 'tipo': int(1)},
                'potencia_ar': {'name': 'Potência ativa real',
                               'endereco': 'MW1298',
                               'registro': None,
                               'value': None,
                               'tipo': int(1)},
                'potencia_as': {'name': 'Potência ativa solicitada',
                              'endereco': 'MW506',
                              'registro': None,
                              'value': None,
                              'tipo': int(1)},
                'fp': {'name': 'Fator de potência',
                       'endereco': 'MW1301',
                       'registro': None,
                       'value': None,
                       'tipo': int(1)},
                'pressao_oleo': {'name': 'Pressão do óleo',
                               'endereco': 'MW1280',
                               'registro': None,
                               'value': None,
                               'tipo': int(1)},
                'temp_UHRLM': {'name': 'Temperatura UHRLM',
                              'endereco': 'MW1323',
                              'registro': None,
                              'value': None,
                              'tipo': int(1)},
                'temp_UHRV': {'name': 'Temperatura UHRV',
                                 'endereco': 'MW1324',
                                 'registro': None,
                                 'value': None,
                                 'tipo': int(1)},
                'velocidade': {'name': 'Velocidade',
                                 'endereco': 'MW1285',
                                 'registro': None,
                                 'value': None,
                                 'tipo': int(1)},
                'frequencia': {'name': 'Frequência',
                                 'endereco': 'MW1302',
                                 'registro': None,
                                 'value': None,
                                 'tipo': int(1)},
        }

class ItemConfirm(ThreeLineAvatarListItem):
    divider = None

# 1 passo: inicialização-

def inicializacao(objeto):
    try:
        global objeto_, db
        objeto_ = objeto
        db = ConnectionDB()
        ak.start(init())
#        ak.start(connection_CLP())
    except Exception as e:
        error.msg(e)

# 2 passo: verifica se existe banco de dados-

async def init():
    try:
        global tabelas_ativas
        with concurrent.futures.ThreadPoolExecutor() as executer:
            data_new, name_new, tabelas_ativas = await ak.run_in_executer(migracao_db, executer)
            if len(tabelas_ativas) >= 1:
                msg(tabelas_ativas)
#            if len(data_new[0]) > 1 and isinstance(name_new, type(None)):
#                painel_aviso('Não existe tabela ativa no banco de dados, por favor configure as conexões','primary')
#                return False
#            dados = db.consulta_descriminada(name_new, 100,'DESC')
#            preencher_inputs(name_new, dados)
#            dados = convert_dict_pandas(dados)
#            objeto_.subject.some_business_logic(dados, name_new)
    except Exception as e:
        error.msg(e)

def migracao_db():
    try:
        colunas_old = ['id', 'energia_a', 'energia_b', 'id_a', 'id_b', 'nivel', 'cidade',
                   'usina', 'ip_a', 'ip_b', 'registro_a', 'registro_b', 'registro_nivel',
                   'criado_em', 'ts']
        colunas_new = ['id', 'container', 'criado_em', 'ts']
        tabelas_ativas = []
        data_new = []
        name_new = None
        for table in db.list_tables():
            dados = db.consulta(table[0])
            if all([item in colunas_old for item in dados.columns]):
                tabelas_ativas.append({'name':table[0],
                                       'inicio':dados['criado_em'].values[0],
                                       'fim':dados['criado_em'].values[-1],
                                       'dados':dados,
                                       'qtd':len(dados),
                                       'state': False})
            if all([item in colunas_new for item in dados.columns]) and len(dados) > len(data_new):
                data_new = dados
                name_new = table[0]
        return data_new, name_new, tabelas_ativas
    except Exception as e:
        error.msg(e)

def msg(tabelas_ativas):
    try:
        global dialog
        button_migracao = MDFlatButton(text='SIM',
                                       text_color=get_color_from_hex("#27979d"))
        migracao = []
        for i, item in enumerate(tabelas_ativas):
            linha = ItemConfirm(text='Nome da tabela: ' + item['name'],
                                secondary_text= 'De: ' + item['inicio'][0:11] + ' até: ' + item['fim'][0:11],
                                tertiary_text= 'Qtd linhas: ' + str(item['qtd']),
                                bg_color=cores['alert'])
            icon_alert = IconLeftWidget(icon='alert-circle')
            linha.add_widget(icon_alert)
            linha.fbind('on_release',set_icon, icon_alert=icon_alert, linha=linha, item=i)
            migracao.append(linha)
        button_migracao.fbind('on_release',criar_migracao)
        dialog = MDDialog(title='Selecione a tabela que deseja fazer a migração',
                          type='confirmation',
                          items= migracao,
                          buttons=[MDFlatButton(text="NÃO",
                                                text_color=get_color_from_hex("#27979d"),
                                                on_release= fechar),
                                   button_migracao])
        dialog.open()
    except Exception as e:
        raise Exception ('Erro na migração do banco de dados : ', e)

def set_icon(instance, icon_alert=None, linha=None, item=None):
    global tabelas_ativas
    icon_alert.icon = 'check' if icon_alert.icon != 'check' else 'alert-circle'
    linha.bg_color = cores['check'] if linha.bg_color != cores['check'] else cores['alert']
    tabelas_ativas[item]['state'] = False if tabelas_ativas[item]['state'] else True

def fechar(*args):
    dialog.dismiss()

def criar_migracao(instance):
    Clock.schedule_once(partial(spinner_active,'migrando'), -1)
    try:
        global entradas_, tabelas_ativas
        dialog.dismiss()
        for base in tabelas_ativas:
            print(base['name'],': ',base['state'])
#        dados =
#        if not len(box_container['objetos']) >= 2:
#            generation_container_migration(dados)
#        colunas_migrar = ['energia_a','energia_b','nivel','criado_em','ts']
#        for i in range(len(dados)):
#            box_container['objetos'][0]['leituras']['acumulada']['value'] = dados['energia_a'].values[i]
#            box_container['objetos'][1]['leituras']['acumulada']['value'] = dados['energia_b'].values[i]
#            box_container['objetos'][0]['leituras']['nivel_agua']['value'] = dados['nivel'].values[i]
#            box_container['objetos'][1]['leituras']['nivel_agua']['value'] = dados['nivel'].values[i]
#            data_hora = dados['criado_em'].values[i]
#            ts = dados['ts'].values[i]
#            if db.inserir_data_b(box_container.copy(), data_hora, ts):
#                pass
#            else:
#                print('Errro')
#        if db.delete_table(box_container['geral']['name_table']):
#            print('Tabela deletada: ', box_container['geral']['name_table'])
#        print(box_container)--
    except Exception as e:
        raise Exception ('Erro na migração do banco de dados: ', e)

def generation_container_migration(dados):
    try:
        global geral, container, container_, box_container
        geral['name_usina'] = dados['usina'].values[-1]
        geral['localizacao'] = dados['cidade'].values[-1]
        geral['name_table'] = 'table_' + unidecode(dados['usina'].values[-1]).replace(' ','_')
        box_container['geral'] = geral
    #    #-------------------------------------
        container['name'] = 'clp_1'
        container['ip'] = dados['ip_a'].values[-1]
        container['id'] = dados['id_a'].values[-1]
        container_A['acumulada']['endereco'] = dados['registro_a'].values[-1]
        container_A['nivel_agua']['endereco'] = dados['registro_nivel'].values[-1]
        container['leituras'] = container_A
        box_container['objetos'].append(container.copy())
    #    #------------------------------------
        container['name'] = 'clp_2'
        container['ip'] = dados['ip_b'].values[-1]
        container['id'] = dados['id_b'].values[-1]
        container_B['acumulada']['endereco'] = dados['registro_b'].values[-1]
        container_B['nivel_agua']['endereco'] = dados['registro_nivel'].values[-1]
        container['leituras'] = container_B
        box_container['objetos'].append(container.copy())
    except Exception as e:
        raise Exception ('Erro na migração do banco de dados: ', e)

# 3 passo: Duas possibilidades [ existe banco de dados, não existe banco de dados]

''' 3.1 - Existe banco de dados com informações'''

# 1 passo: preencher os inputs
def preencher_inputs(name_table, dados):
    try:
        global entradas_, box_container
        box_container = eval(dados['container'].values[len(dados)-1])
        entradas_ = {
                    'inputs_nome'  : box_container['geral']['name_usina'], #
                    'inputs_local' : box_container['geral']['localizacao'], #
                    'inputs_ip_a'  : box_container['objetos'][0]['ip'], #
                    'inputs_ip_b'  : box_container['objetos'][1]['ip'],#
                    'inputs_port_a': box_container['objetos'][0]['leituras']['acumulada']['endereco'],#
                    'inputs_port_b': box_container['objetos'][1]['leituras']['acumulada']['endereco'],
                    'inputs_id_a'  : box_container['objetos'][0]['id'], #
                    'inputs_id_b'  : box_container['objetos'][1]['id'],#
                    'inputs_nivel' : box_container['objetos'][0]['leituras']['nivel_agua']['endereco'],
                    'inputs_time' :  box_container['geral']['time_update'], #
                    }
        for name, value in entradas_.items():
            objeto_.ids[name].text= str(value)
            entradas_[name] = objeto_.ids[name]
    except Exception as e:
        error.msg(e)
# 2 passo: notificar pelo método observer as tabelas

# 3 passo: Faz a conexão e agenda a leitura do CLP
'''
FUNÇÃO LINHA 262 - CHAMADA DE CONEXÃO E AGENDAMENTO
'''

''' 3.2 - Não existir banco de dados ativo '''

def conectar_aux(entradas, objeto):
    try:
        global entradas_, box_container, objeto_
        entradas_ = entradas
        objeto_ = objeto
        if not filtro_entradas():
            painel_aviso('Todas as entradas devem ser preenchidas!', 'alert')
            return False
        if not len(box_container['objetos']) >= 2:
            generation_container()
        create_table()
        ak.start(connection_CLP())
        return True
    except Exception as e:
        error.msg(e)

# 1 passo: Notifica o usuário para preencher a entradas

def painel_aviso(text, tipo, tamanho=["100dp","500dp"],button=True,auto_close=False,tempo=3):
    try:
        global snackbar
        if not snackbar is None:
            snackbar.dismiss()
        snackbar = Snackbar(text=text,
                            duration=tempo,
                            snackbar_x=tamanho[0],
                            snackbar_y=tamanho[1])
        a = (Window.width - (snackbar.snackbar_x * 2))
        snackbar.auto_dismiss = auto_close
        snackbar.bg_color = cores[tipo]
        snackbar.size_hint_x = a / Window.width
        snackbar.duration = tempo
        if button:
            snackbar.buttons = [
                MDFlatButton(
                    text="OK",
                    text_color=(1, 1, 1, 1),
                    on_release=snackbar.dismiss,
                ),
            ]
        snackbar.open()
    except Exception as e:
        error.msg(e)

# 2 passo: Após o acionamento do botão conectar, todas as entradas são validadas

def filtro_entradas():
    try:
        return all([True if len(value.text) > 0 else False for name, value in entradas_.items()])
    except Exception as e:
        error.msg(e)
# 3 passo: gerar container de informações

def generation_container():
    global geral, container, container_, box_container
    geral['name_usina'] = entradas_['inputs_nome'].text
    geral['localizacao'] = entradas_['inputs_local'].text
    geral['name_table'] = 'table_' + unidecode(entradas_['inputs_nome'].text).replace(' ','_')
    box_container['geral'] = geral
#    #-------------------------------------
    container['name'] = 'clp_1'
    container['ip'] = entradas_['inputs_ip_a'].text
    container['id'] = entradas_['inputs_id_a'].text
    container_A['acumulada']['endereco'] = entradas_['inputs_port_a'].text
    container_A['nivel_agua']['endereco'] = entradas_['inputs_nivel'].text
    container['leituras'] = container_A
    box_container['objetos'].append(container.copy())
#    #------------------------------------
    container['name'] = 'clp_2'
    container['ip'] = entradas_['inputs_ip_b'].text
    container['id'] = entradas_['inputs_id_b'].text
    container_B['acumulada']['endereco'] = entradas_['inputs_port_b'].text
    container_B['nivel_agua']['endereco'] = entradas_['inputs_nivel'].text
    container['leituras'] = container_B
    box_container['objetos'].append(container.copy())

# 3 passo: Cria a tabela no banco de dados

def create_table():
    if db.create_table_unit(box_container['geral']['name_table']):
        return True
    painel_aviso('Não use caracteres especiais para o nome da usina', 'alert')

# 3 passo: Faz a conexão e agenda a leitura do CLP
'''
FUNÇÃO LINHA 262 - CHAMADA DE CONEXÃO E AGENDAMENTO
'''
'''
FUNÇÃO CHAMADA DE CONEXÃO E AGENDAMENTO
'''
# 1 passo: executar a função assincrona de conexão ao CLP

async def connection_CLP():
    try:
        spinner_active('Conectando')
        with concurrent.futures.ThreadPoolExecutor() as executer:
                await ak.run_in_executer(conexao_clp, executer)
                objeto_.remove_widget(boxspinner)
                filtro_connection()
                clpa = clp[0]['name'] + str(bool(clp[0]['objeto']))
                clpb = clp[1]['name'] + str(bool(clp[1]['objeto']))
                msga = f'Status: IP-{entradas_["inputs_ip_a"].text} ({clpa})'
                msgb = f'  IP-{entradas_["inputs_ip_b"].text} ({clpb})'
                msgc = f'  tentativa {str(tentativas)}'
                painel_aviso(msga + msgb + msgc, 'ligado')
    except Exception as e:
        error.msg(e)
# 2 passo: executar a função spinner de carregamento

def spinner_active(texto, *args):
    try:
        global boxspinner
        boxspinner = MDFloatLayout(md_bg_color=get_random_color(.5))
        label_spinner = MDLabel(text=texto, halign='center')
        spinner = MDSpinner(size_hint=(None, None),
                            size=(dp(150),dp(150)),
                            pos_hint={'center_x': .5, 'center_y': .5},
                            determinate=False,
                            active=True,
                            palette=[[0.2862, 0.8431, 0.5960, 1],
                                     [0.3568, 0.3215, 0.8666, 1],
                                     [0.88627, 0.3647, 0.59215, 1],
                                     [0.8784, 0.905, 0.40784, 1]])
        boxspinner.add_widget(label_spinner)
        boxspinner.add_widget(spinner)
        objeto_.add_widget(boxspinner)
    except Exception as e:
        error.msg(e)
# 3 passo: executar a função de conexão ao CLP

def conexao_clp():
    try:
        global CLP, box_container, clp
        CLP = ConnectionCLP()
        box_A = box_container['objetos'][0]
        box_B = box_container['objetos'][1]
        clp.append({'name': box_A['name'],'objeto': CLP.run(box_A['ip'])})
        clp.append({'name': box_B['name'],'objeto': CLP.run(box_B['ip'])})
        box_A['leituras'] = search_register(box_A['leituras'])
        box_B['leituras'] = search_register(box_B['leituras'])

    except Exception as e:
        error.msg(e)
# 4 passo: buscar os registros dos endereços do CLP

def search_register(registers: dict)->dict:
    try:
        for key, value in registers.items():
            registers[key]['registro'] = CLP.registro(registers[key]['endereco'])
        return registers
    except Exception as e:
        error,msg(e)

# 5 passo: Executar a função filtro de conexão

def filtro_connection():
    try:
        global tentativas, name_table, container
        clpa = bool(clp[0]['objeto'])
        clpb = bool(clp[1]['objeto'])
        objeto_.ids['inputs_ip_a'].hint_text = 'IP Gerador 1 -' + str(clpa)
        objeto_.ids['inputs_ip_b'].hint_text = 'IP Gerador 2 -' + str(clpb)
        tentativas += 1
        tempo = int(objeto_.ids['inputs_time'].text) * 3
        if not all([clpa,clpb]) and not any([clpa, clpb]):
            objeto_.ids['button_enviar'].text = 'conectar'
            Clock.schedule_once(new_reconnection,10*tentativas)
            return
        if any([clpa, clpb]) and not all([clpa,clpb]):
            objeto_.ids['button_enviar'].text = 'reconectar'
            Clock.schedule_interval(read_clp, tempo)
            return
        if all([clpa, clpb]):
            desabilit_inputs()
            objeto_.ids['layout'].children[0].remove_widget(objeto_.ids['button_enviar'])
            Clock.schedule_interval(read_clp, tempo)
            return
    except Exception as e:
            error.msg(e)

# 6 passo: 3 possibilidades [não conectado, parcialmente conectado, conectado]
# 1 estado: não conectado - executa a função nova tentativa de conexão

def new_reconnection(*args):
    try:
        ak.start(connection_CLP())
    except Exception as e:
        error.msg(e)

# 2 estado: parcialmente conectado - executa a função assincrona de leitura do CLP

def read_clp(*args):
    try:
        ak.start(CLP_G())
    except Exception as e:
        error.msg(e)

# 3 estado: conectado - executa a desativação das entradas e remove o botão de conexão

def desabilit_inputs():
    try:
        for name, value in objeto_.ids.items():
            if name[0:6] == 'inputs':
                value.disabled = True
    except Exception as e:
        error.msg(e)

# 7 passo: executa a função assincrona de leitura do CLP

async def CLP_G():
    global read_data, clp, box_container, clp_objeto
    try:
        with concurrent.futures.ThreadPoolExecutor() as executer:
            box_A = box_container['objetos'][0]
            box_B = box_container['objetos'][1]
            if bool(clp[0]['objeto']):
                clp_objeto = 0
                for key, value in box_A['leituras'].items():
                    read_data = value
                    valor = await ak.run_in_executer(leitura_clp, executer)
                    box_A['leituras'][key] = valor
            if bool(clp[1]['objeto']):
                clp_objeto = 1
                for key, value in box_B['leituras'].items():
                    read_data = value
                    valor = await ak.run_in_executer(leitura_clp, executer)
                    box_B['leituras'][key] = valor
            dados = await ak.run_in_executer(persistir_dados, executer)
            print(dados.columns)
            objeto_.subject.some_business_logic(dados, box_container['geral']['name_table'])
    except Exception as e:
        error.msg(e)

# 8 passo: executa a função com retorno dos dados lidos

def leitura_clp():
    return  CLP.leitura_unit(clp[clp_objeto]['objeto'], read_data)

# 9 passo: verifica a integridade dos dados

def verificacao(escrita, leitura):
    acerto = 0
    for name, value in escrita.items():
        for nam, valu in leitura.items():
            if name == nam:
                if value == valu:
                    acerto += 1
                break
    return acerto/len(escrita)

def filtro_db(dados):
    for name, value in dados.items():
        if not isinstance(dados[name]['value'], str) and name != 'objeto_clp':
            dados[name]['value'] = str(dados[name]['value'])
    return dados

def convert_dict_pandas(data):
    for i, item in enumerate(data['container'].values):
        try:
            teste = eval(item)
            data.loc[i,'name_usina'] =  teste['geral']['name_usina']
            for key, value in teste['objetos'][0]['leituras'].items():
                data.loc[i,key+'_ug1'] = 0 if value['value'] is None else int(value['value'])
            for key, value in teste['objetos'][1]['leituras'].items():
                data.loc[i,key+'_ug2'] = 0 if value['value'] is None else int(value['value'])
        except Exception as e:
            print('Erro encontrado: ', e)
    return data


# 10 passo: persiste os dados no banco de dados de forma assincrona e atualiza todas tabelas, assim como notifica o estado da persistência--

def persistir_dados():
    try:
        global tentativas
        containerx = box_container.copy()
        tentativas += 1
        db.inserir_data(containerx)
        dados = db.consulta_descriminada(box_container['geral']['name_table'],100,'DESC')
        return convert_dict_pandas(dados)
    except Exception as e:
        error.msg(e)

#def write_clp():
#    return CLP.escrever_unit(clp, container)

#def recursiva_dict(this_dict,pontos):
#    for name, key in this_dict.items():
#        pontos += '-'
#        print(pontos)
#        print(name)
#        print(key)
#        if isinstance(key, dict):
#            pontos += '-'
#            recursiva_dict(key, pontos)
#        if isinstance(key, list):
#            for dados in key:
#                if isinstance(dados, dict):
#                    pontos += '-'
#                    recursiva_dict(dados, pontos)

'''
1 passo: verificar se todas as entradas foram preenchidas - ok
2 passo: conectar no CLP - ok
    1 passo: buscar os dados de registro na planilha do excel
    2 passo: verificar se é possível conectar com o CLP
    3 passo: enviar mensagens de notificação
                    # c1 c2
                    # 0  0  = 'Conectar 1 tentativa'
                    # 0  1  = 'c1 desconectado'
                    # 1  0  = 'c2 desconectado'
                    # 1  1  = remove_widget
    4 passo: Tentar uma nova conexão a cada 30 segundos
3 passo: Ler os dados do CLP
4 passo: Armazenar os dados no banco de dados
    1 passo: Criar um container único, com todos os dados para persistir 08:29
5 passo: criar a tabela

'''