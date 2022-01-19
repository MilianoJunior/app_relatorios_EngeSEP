from kivymd.uix.picker import MDDatePicker
from libs.baseclass.connection_db import ConnectionDB
from libs.baseclass.observer_db import Subject
from kivymd.uix.menu import MDDropdownMenu
import datetime
from pytz import timezone
from kivy.utils import (get_random_color, get_color_from_hex)


class Relatorio():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = ConnectionDB()

    def update(self, subject: Subject):
        self.name_db = subject._name_db

    def button_start(self, period: str, ancora=None):
        # consulta ao banco de dados
        self.dados = self.db.consulta(self.name_db)
        # composicao para criação do relatorio
        print(period)
        [self.diario() if period == 'diario' else self.mensal(ancora)]

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
    def mensal(self, ancora):
        inicio = self.dados['criado_em'].values[0]
        fim = self.dados['criado_em'].values[-1]
        print(incio)
        print(fim)
        FULL_MONTHS = {'janeiro': 1,  'fevereiro': 2, u'março': 3,    'abril': 4,
                       'maio': 5,     'junho': 6,     'julho': 7,     'agosto': 8,
                       'setembro': 9, 'outubro': 10,  'novembro': 11, 'dezembro': 12}
        menu_items = []
        for key, value in FULL_MONTHS.items():
            if i[1] >= int(inicio[5:7]) and i[1] <= int(fim[5:7]):
                print(i)
                menu_items.append({"viewclass": "OneLineListItem","text": i[0],"height": dp(56),"on_release":lambda x=i: self.set_item(x)})
        self.menu = MDDropdownMenu(caller=ancora,items=menu_items,width_mult=4)
        self.menu.bind()
        self.menu.open()

    def on_save(self, instance, value, date_range):
        self.dia = value
        print('Dia escolhido: ',value)

    def on_cancel(self, instance, value):
        print('Evento cancelado')