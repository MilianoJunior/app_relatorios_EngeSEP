from kivymd.uix.picker import MDDatePicker
from libs.baseclass.pdf import PDF
from libs.baseclass.connection_db import ConnectionDB
from libs.baseclass.observer_db import Subject
from libs.baseclass.periodo import Periodo
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.filemanager import MDFileManager
from unidecode import unidecode
from kivymd.toast import toast
from kivy.metrics import dp
from datetime import datetime
from kivy.utils import get_color_from_hex
import pandas as pd
from os import path
import os

class Relatorio():

    def __init__(self):
        self.db = ConnectionDB()
        self.periodo = Periodo()

    def update(self, subject: Subject):
        self.name_db = subject._name_db

    def button_start(self, period: str, ancora=None):
        self.dados = self.db.consulta(self.name_db)
        print(self.name_db)
        print(self.dados.info())
        self.ancora = ancora
#        getattr(self, period)()

    def diario(self):
        inicio = self.dados['criado_em'].values[0]
        fim = self.dados['criado_em'].values[-1]
        try:
            date_dialog = MDDatePicker(
                        min_date=datetime.date(int(inicio[6:10]), int(inicio[3:5]), int(inicio[0:2])),
                        max_date=datetime.date(int(fim[6:10]), int(fim[3:5]), int(fim[0:2])),
                        primary_color=get_color_from_hex("#363636"),
                        selector_color=get_color_from_hex("#A9A9A9"),
                        text_current_color =get_color_from_hex("#6495ED"),
                        text_button_color=get_color_from_hex("#363636"),
                        )
            date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
            date_dialog.open()
        except:
            raise Exception('Aguarde 1 dia para imprimir o primeiro relatório')

    def mensal(self):
        inicio = self.dados['criado_em'].values[0].split('-')
        fim = self.dados['criado_em'].values[-1].split('-')
        FULL_MONTHS = {'janeiro': 1,  'fevereiro': 2, u'março': 3,    'abril': 4,
                       'maio': 5,     'junho': 6,     'julho': 7,     'agosto': 8,
                       'setembro': 9, 'outubro': 10,  'novembro': 11, 'dezembro': 12}
        menu_items = []
        for key in FULL_MONTHS.items():
            if key[1] >= int(inicio[1]) and key[1] <= int(fim[1]):
                menu_items.append({"viewclass": "OneLineListItem","text": key[0] +': '+str(fim[2][0:5]),"height": dp(56),"on_release":lambda x=key: self.set_item(x)})
        self.menu = MDDropdownMenu(caller=self.ancora,items=menu_items,width_mult=4)
        self.menu.bind()
        self.menu.open()

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def select_path(self, path):
        self.exit_manager()
        data_e_hora = datetime.now().strftime('%d-%m-%H-%M')
        name=f'ensegep-{unidecode(data_e_hora)}-.csv'
        path_save = os.path.join(path, name)
        data = self.convert_dict_pandas()
        data = self.convert_all(data)
        data.to_csv(path_save)
        del data

    def todos(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )
        home = path.expanduser('~')
        location = path.join(home, 'Downloads')
        self.file_manager.show(location)  # output manager to the screen
        self.manager_open = True

    def on_save(self, instance, value, date_range):
        self.dia = value
        data = self.convert_dict_pandas()
        data_selection, descricao = self.periodo.dia_metodo(data, value)
        pdf = PDF()
        pdf.gerar(data_selection, descricao)

    def on_cancel(self, instance, value):
        pass

    def set_item(self, *args):
        self.menu.dismiss()
        data = self.convert_dict_pandas()
        data_selection, descricao = self.periodo.mes_metodo(data,args[0])
        pdf = PDF()
        pdf.gerar(data_selection, descricao)

    def convert_dict_pandas(self):
        colunas=['id','energia_a' ,'energia_b','id_a','id_b',
                 'nivel', 'cidade', 'usina','ip_a','ip_b','registro_a','registro_b',
                 'registro_nivel', 'criado_em', 'ts']
        dados = []
        for i in range(0, len(self.dados)):
            geral = eval(self.dados['container'].values[i])
            energia_a = geral['objetos'][0]['leituras']['acumulada']['value']
            energia_b = geral['objetos'][1]['leituras']['acumulada']['value']
            id_a = geral['objetos'][0]['id']
            id_b = geral['objetos'][1]['id']
            nivel = geral['objetos'][0]['leituras']['nivel_agua']['value']
            cidade = geral['geral']['localizacao']
            usina = geral['geral']['name_usina']
            ip_a = geral['objetos'][0]['ip']
            ip_b = geral['objetos'][1]['ip']
            registro_a = geral['objetos'][0]['leituras']['acumulada']['endereco']
            registro_b = geral['objetos'][1]['leituras']['acumulada']['endereco']
            registro_nivel = geral['objetos'][0]['leituras']['nivel_agua']['endereco']
            criado_em = self.dados['criado_em'].values[i]
            ts = self.dados['ts'].values[i]
            dados.append([i, energia_a, energia_b, id_a, id_b, nivel, cidade, usina,
                          ip_a, ip_b, registro_a, registro_b, registro_nivel, criado_em, ts])
        data = pd.DataFrame(dados, columns=colunas)
        return data

    def convert_all(self, data):
        for i, item in enumerate(self.dados['container'].values):
            try:
                teste = eval(item)
                for key, value in teste['objetos'][0]['leituras'].items():
                    data.loc[i,key+'_ug1'] = 0 if value['value'] is None else int(value['value'])
                for key, value in teste['objetos'][1]['leituras'].items():
                    data.loc[i,key+'_ug2'] = 0 if value['value'] is None else int(value['value'])
            except Exception as e:
                print('Erro encontrado: ', e)
        return data
