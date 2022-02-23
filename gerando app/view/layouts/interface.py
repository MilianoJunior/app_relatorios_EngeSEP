# módulos externos
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
# modulos da aplicação
from view.widgets.personalizados.toolbar_menu import ToolbarMenu
from view.widgets.personalizados.card_info import CardInfo
from view.widgets.personalizados.menu_print import MenuPrint
#from controllers.excpetions.RootException import InterfaceException

# variaveis globais de configuração dos widgets
cores = {'background':get_color_from_hex('#565050'),
         'primary': get_color_from_hex('#000000'),
         'line': get_color_from_hex('#F1F1F1'),
         'linedestaque': get_color_from_hex('#03DAC6')}

widget_menu = {'name':'ToolbarMenu',
               'pos':{'x': 0, 'y': 0},
               'size':(360,56),
               'size_g':(360,731),
               'cores': cores}

widget_card_info = {'name':'CardInfo',
                   'pos':{'x': 8, 'y': 84},
                   'size':(344,250),
                   'size_g':(360,731),
                   'cores':cores}

widget_print = {'name':'MenuPrint',
                'pos':{'x': 0, 'y': 667},
                'size':(360,64),
                'size_g':(360,731),
                'cores':cores}

widgets = [widget_menu, widget_card_info, widget_print]

class Interface(Screen):
    '''
        description: Screen com as configurações de layout para compor os widgets.

        return screen layout
    '''
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __call__(self):
        # criação do layout
        layout = MDFloatLayout()
        layout.md_bg_color = cores['background']
        [self.pos_porcent(w) for w in widgets]
        [self.size_porcent(w) for w in widgets]

        # criação dos objetos widgets
        toolbar = ToolbarMenu(widget_menu)()
        card = CardInfo(widget_card_info)()
        menu = MenuPrint(widget_print)()
#        self.propriedades(toolbar)
        # adicionando os objetos no layout
        layout.add_widget(toolbar)
        layout.add_widget(card)
        layout.add_widget(menu)
        # adicionando o layout no screen
        self.add_widget(layout)
        # métodos dos objetos
        return self

    def propriedades(self, widget):
        for s in dir(widget):
            print('name: ', s)
            try:
                print('Value: ',getattr(widget,s)())
            except Exception as e:
                print('Value: ',getattr(widget,s))
            print('---')

    def size_porcent(self, widget):
        size_x = widget['size'][0]/widget['size_g'][0]
        size_y = widget['size'][1]/widget['size_g'][1]
        widget.update({'size':(size_x, size_y)})

    def pos_porcent(self, widget):
        pos_y = 1-((widget['pos']['y'] + widget['size'][1])/widget['size_g'][1])
        pos_x = widget['pos']['x']/widget['size'][0]
        widget.update({'pos': {'x': pos_x, 'y': pos_y}})







