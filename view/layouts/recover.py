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
widget_email = {'name':'Email',
                'pos':{'x': 16, 'y': 247},
                'size':(329,56),
                'size_g':(360,731),
                'tag': 'Email',
                'icon': "at",
                'value': False,
                'cores':cores[thema]}

widget_button = {'name':'Button',
                'pos':{'x': 94, 'y': 453},
                'size':(172,37),
                'size_g':(360,731),
                'tag': '        RECUPERAR        ',
                'icon': "location-enter",
                'cores':cores[thema]}

widget_print = {'name':'MenuPrint',
                'pos':{'x': 0, 'y': 667},
                'size':(360,64),
                'size_g':(360,731),
                'cores':cores[thema]}


widgets = [widget_email, widget_button]

class RecoverPassword(Screen):
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
            btn = Button(text='Recuperar senha')
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







