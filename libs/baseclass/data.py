from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex
from libs.baseclass.observer_db import Subject
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import ListProperty
from sys import getsizeof

list_b = {
                'Nr. UG-02': 'id',
                'Data': 'criado_em',
                'Nível de água': 'nivel_agua_ug1',
                'Energia': 'acumulada_ug1',
                'Distribuidor': 'distribuidor_ug1',
                'Potência ativa real': 'potencia_ar_ug1',
                'Potência ativa solicitada': 'potencia_as_ug1',
                'Fator de potência': 'fp_ug1',
                'Pressão de óleo': 'pressao_oleo_ug1',
                'Temperatura UHRLM': 'temp_UHRLM_ug1',
                'Temperatura UHRV': 'temp_UHRV_ug1',
                'Velocidade': 'velocidade_ug1',
                'Frequência': 'frequencia_ug1',
        }
list_a = {
                'Nr. UG-01': 'id',
                'Data': 'criado_em',
                'Nível de água': 'nivel_agua_ug2',
                'Energia': 'acumulada_ug2',
                'Distribuidor': 'distribuidor_ug2',
                'Potência ativa real': 'potencia_ar_ug2',
                'Potência ativa solicitada': 'potencia_as_ug2',
                'Fator de potência': 'fp_ug2',
                'Pressão de óleo': 'pressao_oleo_ug2',
                'Temperatura UHRLM': 'temp_UHRLM_ug2',
                'Temperatura UHRV': 'temp_UHRV_ug2',
                'Velocidade': 'velocidade_ug2',
                'Frequência': 'frequencia_ug2',
        }


class Data(MDBoxLayout):
    dados_a = ListProperty()
    dados_b = ListProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orientation = 'vertical'
        self.md_bg_color = get_color_from_hex('#262626')

    def __call__(self):
        self.create_table()
        return self

    def update(self, subject: Subject) -> None:
        self.data_table_a.row_data = []
        self.data_table_b.row_data = []
        [self.data_table_a.row_data.append(d) for d in
                 subject._data[[value for name, value in list_a.items()]].values]

        [self.data_table_b.row_data.append(d) for d in
                 subject._data[[value for name, value in list_b.items()]].values]

    def on_start(self, *args):
        pass

    def create_table(self):
        self.data_table_a = MDDataTable(use_pagination=True,
                                   rows_num=10,
                                   column_data=[(name, dp(30)) for name in list_a.keys()])
        self.data_table_b = MDDataTable(use_pagination=True,
                                   rows_num=10,
                                   column_data=[(name, dp(30)) for name in list_b.keys()])
        self.add_widget(self.data_table_a)
        self.add_widget(self.data_table_b)


'''
1 passo: criar a tabela
'''
