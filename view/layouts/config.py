# módulos externos
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from functools import partial
# modulos da aplicação
from view.widgets.personalizados.toolbar_menu import ToolbarMenu
from view.widgets.personalizados.button_plus import ButtonPlus
from view.widgets.genericos.button import ButtonGeneric
from view.widgets.genericos.input import InputGeneric
from view.widgets.personalizados.menu_logo import MenuLogo
from view.widgets.personalizados.multi_button import MultiButton
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
                    'pos':{'center_x': .5, 'center_y': .5},
                    'size':(329,56),
                    'size_g':(360,731),
                    'tag': 'ID',
                    'icon': "table-row",
                    'value': False,
                    'cores':cores[thema]}
widget_register = {'name':'Registro',
                    'pos':{'center_x': .5, 'center_y': .5},
                    'size':(329,56),
                    'size_g':(360,731),
                    'tag': 'Registro',
                    'icon': "code-tags",
                    'value': False,
                    'cores':cores[thema]}

widget_button_plus= {'name':'Button',
                    'pos':{'x': 281, 'y': 578},
                    'size':(56,56),
                    'size_g':(360,731),
                    'tag': {'adicionar leitura': 'connection'},
                    'icon': "plus",
                    'cores':cores[thema]}


widgets = [widget_menu, widget_usina, widget_localizacao, widget_button_plus]

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
            self.grid = MDBoxLayout(orientation='vertical',
                               md_bg_color=cores[thema]['linedestaque'],
                               size_hint_y=None,
                               spacing=20)
            self.grid.bind(minimum_height=self.grid.setter('height'))
            root = ScrollView(size_hint=(1,1)) #, height=Window.height, width=Window.width)
            # criação dos objetos widgets
            toolbar = ToolbarMenu(widget_menu)()
            #----------------------------------
            input_usina = InputGeneric(widget_usina)()
            #---------------------------------
            input_localizacao = InputGeneric(widget_localizacao)()
            #------------------------------------
            input_id = InputGeneric(widget_id)()
            #------------------------------------
            input_register = InputGeneric(widget_register)()
            #--------------------------------------
            nova_leitura = ButtonPlus(widget_button_plus)()
            # vinculando métodos
            nova_leitura.children[0].bind(on_release=partial(self.create_input,root))
            # adicionando os objetos no layout
            self.grid.add_widget(input_id)
            self.grid.add_widget(input_register)
            root.add_widget(self.grid)
            #-----------------------------
            layout.add_widget(toolbar)
            layout.add_widget(input_usina)
            layout.add_widget(input_localizacao)
            layout.add_widget(nova_leitura)
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

    def create_input(self, root, *args):
        print('adicionando elementos',args)
        input_id = InputGeneric(widget_id)()
        input_register = InputGeneric(widget_register)()
        self.grid.add_widget(input_id)
        self.grid.add_widget(input_register)
        