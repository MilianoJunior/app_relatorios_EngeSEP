# módulos externos
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from functools import partial

from numpy import select
# modulos da aplicação
from view.widgets.personalizados.toolbar_menu import ToolbarMenu
from view.widgets.personalizados.button_plus import ButtonPlus
from view.widgets.genericos.button import ButtonGeneric
from view.widgets.genericos.input import InputGeneric
from view.widgets.personalizados.menu_logo import MenuLogo
from view.widgets.personalizados.input_config import InputConfig
from assets.themas_color import cores
from controllers.excpetions.RootException import InterfaceException

# variaveis globais de configuração dos widgets

thema = 'dark'
widget_menu = {'name':'ToolbarMenu',
               'pos':{'x': 0, 'y': 0},
               'size':(360,56),
               'size_g':(360,731),
               'cores': cores[thema]}

widget_usina = {'name':'Usina',
                'pos':{'x': 16, 'y': 82},
                'size':(329,56),
                'size_g':(360,731),
                'tag': 'Usina',
                'icon': "tag",
                'value': False,
                'cores':cores[thema]}

widget_localizacao = {'name':'Localizacao',
                    'pos':{'x': 16, 'y': 163},
                    'size':(329,56),
                    'size_g':(360,731),
                    'tag': 'Localização',
                    'icon': "google-maps",
                    'value': False,
                    'cores':cores[thema]}
widget_id = {'name':'Identificacao',
                    'pos': None,
                    'size':(329,56),
                    'size_g':(360,731),
                    'tag': 'ID',
                    'icon': "table-row",
                    'value': False,
                    'cores':cores[thema]}

widget_button_plus = {'name':'Button_plus',
                    'pos':{'x': 289, 'y': 624},
                    'size':(56,56),
                    'size_g':(360,731),
                    'tag': {'adicionar leitura': 'connection'},
                    'icon': "plus",
                    'cores':cores[thema]}

widget_conectar = {'name':'Conectar',
                    'pos':{'x': 94, 'y': 652},
                    'size':(172,37),
                    'size_g':(360,731),
                    'tag': '      CONECTAR      ',
                    'icon': "lan-connect",
                    'cores':cores[thema]}


widgets = [widget_menu, widget_usina, widget_localizacao, widget_button_plus, widget_conectar]

class Config(Screen):
    '''
        description: Screen com as configurações de layout para compor os widgets.

        return screen layout
    '''
    def __init__(self, name, *args, **kwargs):
        super(Config, self).__init__(*args, **kwargs)
        self.name = name

    def __call__(self):
        try:
            # criação do layout principal
            layout = MDFloatLayout()
            layout.md_bg_color = cores[thema]['background']
            [self.pos_porcent(w) for w in widgets]
            [self.size_porcent(w) for w in widgets]
            # layout secundario auxiliar
            #---------------------------------------------------------------
            self.grid = MDGridLayout(cols=1,spacing=10, size_hint_y=None)
            self.grid.bind(minimum_height=self.grid.setter('height'))
            root = ScrollView(size_hint=(329/360, None), height= Window.height *(374/730), pos_hint= {'x': 16/360,'y': 113/730})
            root.add_widget(self.grid)
            # widgets
            #-----------------------------------------------------------------
            toolbar = ToolbarMenu(widget_menu)()
            #----------------------------------
            input_usina = InputGeneric(widget_usina)()
            #---------------------------------
            input_localizacao = InputGeneric(widget_localizacao)()
            #--------------------------------------
            new_read = ButtonPlus(widget_button_plus)()
            #---------------------------------------
            conectar = ButtonGeneric(widget_conectar)()
            # vinculando métodos
            new_read.bind(on_release=self.create_input)
            conectar.children[0].bind(on_release=self.conectar)
            # adicionando os objetos no layout
            layout.add_widget(toolbar,1)
            layout.add_widget(input_usina,2)
            layout.add_widget(input_localizacao,3)
            layout.add_widget(new_read,4)
            layout.add_widget(root,0)
            layout.add_widget(conectar,0)
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
        pos_x = widget['pos']['x']/widget['size_g'][0]
        widget.update({'pos': {'x': pos_x, 'y': pos_y}})

    def create_input(self,*args):
        input_id = InputConfig(widget_id)()
        self.grid.add_widget(input_id)

    def conectar(self,*args):
        request=[{'name': item.children[0].text, 'value': item.children[1].text}
                        for item in self.grid.children]
        print('Conectando CLP: ',request)