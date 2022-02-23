from kivymd.uix.picker import MDDatePicker
from libs.baseclass.pdf import PDF
from libs.baseclass.connection_db import ConnectionDB
from libs.baseclass.observer_db import Subject
from libs.baseclass.periodo import Periodo
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.spinner import MDSpinner
from kivy.utils import get_random_color
from unidecode import unidecode
from kivymd.toast import toast
from kivy.metrics import dp
from datetime import datetime
from kivy.utils import get_color_from_hex
import pandas as pd
from os import path
from functools import partial
from kivy.clock import Clock
import asynckivy as ak
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.dialog import MDDialog
import concurrent.futures
import os
import time

class Relatorio():

    boxspinner = False
    dialog = False

    def __init__(self):
        self.db = ConnectionDB()
        self.periodo = Periodo()

    def update(self, subject: Subject):
        self.name_db = subject._name_db

    def button_start(self, period: str, ancora=None):
        self.dados = self.db.consulta(self.name_db)
        self.ancora = ancora
        getattr(self, period)()

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
        data_e_hora = datetime.now().strftime('%d-%m-%H-%M')
        name=f'ensegep-{unidecode(data_e_hora)}-.csv'
        path_save = os.path.join(path, name)
        inicio = time.time()
        async def load():
            with concurrent.futures.ThreadPoolExecutor() as executer:
                await ak.run_in_executer(self.convert_all, executer)
                self.dados.to_csv(path_save)
                del self.dados
        ak.start(load())
        Clock.schedule_once(partial(self.time_loss,inicio),2)
        self.exit_manager()
        

    def time_loss(self, time_actual, *args):
        try:
            dif_time = time.time() - time_actual
            if not self.boxspinner:
                self.boxspinner = True
                spinner = MDSpinner(size_hint=(None, None),
                                    size=(dp(120), dp(120)),
                                    pos_hint={'x': 1, 'center_y': .5},
                                    active=True,
                                    palette=[[0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1],
                                           [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1],
                                           [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1],
                                           [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1]])
                # box.add_widget(spinner)
                self.dialog = MDDialog(title ='Aguarde...', 
                                       type="custom", 
                                       content_cls = spinner,
                                       md_bg_color=(0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1),
                                       radius=[20, 7, 20, 7])
                self.dialog.size = [180, 100]
                self.dialog.open()
            # self.dialog.title = 'Aguarde: '+str(round(dif_time))
        except Exception as e:
            print('Erro: ', e)

    def todos(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=False)
        home = path.expanduser('~')
        location = path.join(home, 'Downloads')
        self.file_manager.show(location)  # output manager to the screen--
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

    def convert_all(self, *args):
        for i, item in enumerate(self.dados['container'].values):
            try:
                if i%5000 == 0 and bool(self.dialog):
                    self.dialog.title = 'Aguarde: ' + str(round(i/len(self.dados))) + '%'
                print('Aguarde: ' + str(round(i/len(self.dados))) + '%', i, len(self.dados))
                teste = eval(item)
                for key, value in teste['objetos'][0]['leituras'].items():
                    self.dados.loc[i,key+'_ug1'] = 0 if value['value'] is None else int(value['value'])
                for key, value in teste['objetos'][1]['leituras'].items():
                    self.dados.loc[i,key+'_ug2'] = 0 if value['value'] is None else int(value['value'])
            except Exception as e:
                raise Exception('Error convert data: ', e)
        
