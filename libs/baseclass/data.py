from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex
from libs.baseclass.observer_db import Subject
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import ListProperty
from sys import getsizeof

list_a = {
                '[size=14]Nr. UG-01[/size]': 'id',
                '[size=14]Data[/size]': 'criado_em',
                '[size=14]Nível de água[/size]': 'nivel_agua_ug1',
                '[size=14]Energia[/size]': 'acumulada_ug1',
                '[size=14]Distribuidor[/size]': 'distribuidor_ug1',
                '[size=14]Potência ativa real[/size]': 'potencia_ar_ug1',
                '[size=14]Potência ativa solicitada[/size]': 'potencia_as_ug1',
                '[size=14]Fator de potência[/size]': 'fp_ug1',
                '[size=14]Pressão de óleo[/size]': 'pressao_oleo_ug1',
                '[size=14]Temperatura UHLM[/size]': 'temp_UHRLM_ug1',
                '[size=14]Temperatura UHRV[/size]': 'temp_UHRV_ug1',
                '[size=14]Velocidade[/size]': 'velocidade_ug1',
                '[size=14]Frequência[/size]': 'frequencia_ug1',
        }
list_b = {
                '[size=14]Nr. UG-02[/size]': 'id',
                '[size=14]Data[/size]': 'criado_em',
                '[size=14]Nível de água[/size]': 'nivel_agua_ug2',
                '[size=14]Energia[/size]': 'acumulada_ug2',
                '[size=14]Distribuidor[/size]': 'distribuidor_ug2',
                '[size=14]Potência ativa real[/size]': 'potencia_ar_ug2',
                '[size=14]Potência ativa solicitada[/size]': 'potencia_as_ug2',
                '[size=14]Fator de potência[/size]': 'fp_ug2',
                '[size=14]Pressão de óleo[/size]': 'pressao_oleo_ug2',
                '[size=14]Temperatura UHLM[/size]': 'temp_UHRLM_ug2',
                '[size=14]Temperatura UHRV[/size]': 'temp_UHRV_ug2',
                '[size=14]Velocidade[/size]': 'velocidade_ug2',
                '[size=14]Frequência[/size]': 'frequencia_ug2',
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
        for lista in subject._data[[value for name, value in list_a.items()]].values:
            dados = []
            for s in lista:
                dados.append(f"[size=12]{str(s)}[/size]")
            self.data_table_a.row_data.append(dados)
        for lista in subject._data[[value for name, value in list_b.items()]].values:
            dados = []
            for s in lista:
                dados.append(f"[size=12]{str(s)}[/size]")
            self.data_table_b.row_data.append(dados)


    def create_table(self):
        [print(name, len(name)) for name in list_a.keys()]
        self.data_table_a = MDDataTable(use_pagination=True,
                                   rows_num=10,
                                   column_data=[(name, dp(len(name))) for name in list_a.keys()])
        self.data_table_b = MDDataTable(use_pagination=True,
                                   rows_num=10,
                                   column_data=[(name, dp(len(name))) for name in list_b.keys()])
        self.add_widget(self.data_table_a)
        self.add_widget(self.data_table_b)


'''
1 passo: criar a tabela
'''
