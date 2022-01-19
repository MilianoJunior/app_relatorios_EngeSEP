from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import (ScreenManager, Screen)
from libs.baseclass.form_new import FormNew
from libs.baseclass.table import Table
from libs.baseclass.data import Data
from libs.baseclass.observer_db import ConcreteSubject
from libs.baseclass.Exception_error import Error
from libs.baseclass.relatorio import Relatorio
Clock.max_iteration = 20

subject = ConcreteSubject()
erro = Error()


class EngesepMenuRail(MDBoxLayout):
    central = ObjectProperty()
    menu = ObjectProperty()
    sm = ObjectProperty()
    dialog = None
    choice_period = 'mensal'
    dia = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.callback_func, 0)

    def callback_func(self, *args):
        self.sm = Composite()()
        self.relatorio = Relatorio()
        subject.attach(self.relatorio)
        self.ids['layout'].add_widget(self.sm)

    def on_checkbox_active(self, checkbox, value, name):
        if value:
            self.choice_period = name

    def gerar_relatorio(self):
        self.relatorio.button_start(self.choice_period, self.ids.field)

    def transition_screen(self, *args):
        self.sm.current = args[1]
        print(args)


class Composite():
    sm = ScreenManager()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self):
        return self.composicao()

    def composicao(self, *args):
        try:
            # criação dos screens: form, tabela, config
            screen_form = Screen(name='form_config')
            screen_table = Screen(name='table')
            screen_data = Screen(name='data')
            # criação das interfaces
            form_config = FormNew(subject)()
            table = Table()()
            data = Data()()
            # inscrevendo os objetos no observador
            subject.attach(form_config)
            subject.attach(table)
            subject.attach(data)
            # composicao screens com os objetos
            screen_form.add_widget(form_config)
            screen_table.add_widget(table)
            screen_data.add_widget(data)
            # composição do screemmaneger
            self.sm.add_widget(screen_form)
            self.sm.add_widget(screen_table)
            self.sm.add_widget(screen_data)

            form_config.subject = subject

            return self.sm
        except Exception as e:
            screen_error = Screen(name='error')
            screen_error.add_widget(erro.msg(e))
            self.sm.add_widget(screen_error)
            return self.sm
#            return erro.msg(e)



'''
    def on_checkbox_active(self, checkbox, value, name):
        if value:
            self.choice_period = name

    def on_save(self, instance, value, date_range):
        self.dia = value
        self.callback()

    def on_cancel(self, instance, value):
        print('Evento cancelado')

    def month_menu(self,val):
        try:
            if len(self.tabela.dados)<=0:
                self.msg("Banco de dados não tem informações salvas",self.callback_not)
                return
            if self.menu:
                self.menu.dismiss()
            inicio = self.tabela.dados[0][13][0:10]
            fim = self.tabela.dados[len(self.tabela.dados)-1][13][0:10]
            if self.choice_period == 'mensal':
                FULL_MONTHS = {'janeiro': 1,  'fevereiro': 2, u'março': 3,    'abril': 4,
                               'maio': 5,     'junho': 6,     'julho': 7,     'agosto': 8,
                               'setembro': 9, 'outubro': 10,  'novembro': 11, 'dezembro': 12}
                menu_items = []
                for i in FULL_MONTHS.items():
                    if i[1] >= int(inicio[5:7]) and i[1] <= int(fim[5:7]):
                        print(i)
                        menu_items.append({"viewclass": "OneLineListItem","text": i[0],"height": dp(56),"on_release":lambda x=i: self.set_item(x)})
                self.menu = MDDropdownMenu(caller=self.ids.field,items=menu_items,width_mult=4)
                self.menu.bind()
                self.menu.open()
            else:
                date_dialog = MDDatePicker(
                    min_date=datetime.date(int(inicio[0:4]), int(inicio[5:7]), int(inicio[8:10])),
                    max_date=datetime.date(int(fim[0:4]), int(fim[5:7]), int(fim[8:10])),
                    primary_color=get_color_from_hex("#363636"),
                    selector_color=get_color_from_hex("#A9A9A9"),
                    text_current_color =get_color_from_hex("#6495ED"),
                    text_button_color=get_color_from_hex("#363636"),
                    )
                date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
                date_dialog.open()
        except Exception as e:
            self.msg(f'Tente Novamente: {str(e)}',self.callback_not)

    def set_item(self, text__item):
        self.mes = text__item
        self.callback()
        self.menu.dismiss()

    def callback_not(self,dt):
        self.dialog.dismiss()

    def msg(self,texto,callback):
        if not self.dialog:
            self.dialog = MDDialog(text=texto,
                                   buttons=[MDFlatButton(text='Fechar', text_color=get_color_from_hex("#F72808"), on_release= callback)])
        self.dialog.open()
        Clock.schedule_once(callback, 5)

    def on_start(self, *args):
        pass
#        screen_tabela = Screen(name='screen1')
#        screen_form = Screen(name='screen2')
#        screen_config = Screen(name='screen3')
#        self.form = FormLayout()
#        screen_form.add_widget(self.form)
#        self.sm.add_widget(screen_form)
#        self.tabela = Tabela()
#        self.tabela.dados = self.form.dados
#        self.tabela.name_table = self.form.name_table
#        screen_tabela.add_widget(self.tabela)
#        self.sm.add_widget(screen_tabela)
#        self.ids.layout.add_widget(self.sm)
#        self.central = self.form
#        datafull = DataFull()()
#        screen_config.add_widget(datafull)
#        self.sm.add_widget(screen_config)

    def callback(self):

        if self.choice_period == 'mensal':
            pr_mes = Periodo(self.tabela.dados,self.mes)
            self.data_selection,self.descricao = pr_mes.mes_metodo()
        else:
            pr_dia = Periodo(self.tabela.dados,self.dia)
            self.data_selection,self.descricao = pr_dia.dia_metodo()
        pdf = PDF()
        pdf.gerar(self.data_selection,self.descricao)

'''





