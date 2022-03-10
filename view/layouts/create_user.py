# módulos externos
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
# modulos da aplicação
from view.widgets.personalizados.toolbar_menu import ToolbarMenu
from view.widgets.personalizados.card_info import CardInfo
from view.widgets.personalizados.menu_print import MenuPrint
from assets.themas_color import cores
from controllers.excpetions.RootException import InterfaceException

# variaveis globais de configuração dos widgets

thema = 'dark'
widget_menu = {'name':'ToolbarMenu',
               'pos':{'x': 0, 'y': 0},
               'size':(360,56),
               'size_g':(360,731),
               'cores': cores[thema]}

widget_card_info = {'name':'CardInfo',
                   'pos':{'center_x': .5, 'center_y': .5},
                   'size':(344,250),
                   'size_g':(360,731),
                   'tag': 'UG',
                   'value': 0,
                   'cores':cores[thema]}

widget_print = {'name':'MenuPrint',
                'pos':{'x': 0, 'y': 667},
                'size':(360,64),
                'size_g':(360,731),
                'cores':cores[thema]}


widgets = [widget_menu, widget_print]

class CreateUser(Screen):
    '''
        description: Screen com as configurações de layout para compor os widgets.

        return screen layout
    '''
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __call__(self):
        try:
            # criação do layout principal
            layout = MDFloatLayout()
            layout.md_bg_color = cores[thema]['background']
            [self.pos_porcent(w) for w in widgets]
            [self.size_porcent(w) for w in widgets]
            # criação dos objetos widgets
            btn = Button(text='Criar usuário')
            # adicionando os objetos no layout-
            layout.add_widget(btn)
            # adicionando o layout no screen
            self.add_widget(layout)
            # métodos dos objetos
            return self
        except Exception as e:
            raise InterfaceException(e)()

    def size_porcent(self, widget):
        size_x = widget['size'][0]/widget['size_g'][0]
        size_y = widget['size'][1]/widget['size_g'][1]
        widget.update({'size':(size_x, size_y)})

    def pos_porcent(self, widget):
        pos_y = 1-((widget['pos']['y'] + widget['size'][1])/widget['size_g'][1])
        pos_x = widget['pos']['x']/widget['size'][0]
        widget.update({'pos': {'x': pos_x, 'y': pos_y}})







