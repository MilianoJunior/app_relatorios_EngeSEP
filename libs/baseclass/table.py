from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex
from libs.baseclass.connection_db import ConnectionDB
from kivymd.uix.datatables import MDDataTable
from libs.baseclass.observer_db import (ConcreteSubject, Subject)
from kivy.metrics import dp
from kivy.properties import ListProperty
from sys import getsizeof

class Table(MDBoxLayout):
    dados = ListProperty([])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orientation = 'vertical'
        self.md_bg_color = get_color_from_hex('#898989')

    def __call__(self):
        self.add_widget(self.create_table())
        return self

    def update(self, subject: Subject) -> None:
        dados_aux = subject._data[['id','criado_em',
                                  'name_usina','acumulada_ug1',
                                  'acumulada_ug2','nivel_agua_ug1']].values
        self.data_tables.row_data = []
        for lista in dados_aux:
            dados = []
            for s in lista:
                dados.append(f"[size=12]{str(s)}[/size]")
            self.data_tables.row_data.append(dados)
#        [self.data_tables.row_data.append(n) for n in dados_aux]

    def on_start(self, *args):
        pass

    def create_table(self):
        self.data_tables = MDDataTable(
            size_hint=(1, 0.7),
            use_pagination=True,
            rows_num=10,
            sorted_order='DSC',
            column_data=[
                ("No.", dp(10)),
                ("Data", dp(30)),
                ("Nome", dp(30)),
                ("Energia UG-01", dp(30)),
                ("Energia UG-02", dp(30)),
                ("Nível", dp(20)),
            ],
            )
        return self.data_tables
    def update_row_data(self, *dt):
        print(dt)

#subject.attach()
'''
1 passo: criar uma tabela e inserir no screen
2 passo: propagar os dados

'''