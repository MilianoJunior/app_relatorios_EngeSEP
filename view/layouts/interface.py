# módulos externos
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
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

class Interface(Screen):
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
            b += 1
            layout = MDFloatLayout()
            layout.md_bg_color = cores[thema]['background']
            [self.pos_porcent(w) for w in widgets]
            [self.size_porcent(w) for w in widgets]
            # criação do layout secundário
            grid = MDBoxLayout(orientation='vertical',
                               md_bg_color=cores[thema]['background'],
                               size_hint_y=None,
                               spacing=20)
            grid.bind(minimum_height=grid.setter('height'))
            root = ScrollView(size_hint=(1,.9))
            # criação dos objetos widgets
            #----------------------------------
            toolbar = ToolbarMenu(widget_menu)()
            #----------------------------------
            widget_card_info.update({'tag':'UG-01'})
            widget_card_info.update({'value':'35'})
            card1 = CardInfo(widget_card_info)()
            #-----------------------------------
            toolbar = ToolbarMenu(widget_menu)()
            widget_card_info.update({'tag':'UG-02'})
            widget_card_info.update({'value':'93'})
            card2 = CardInfo(widget_card_info)()
            #-----------------------------------
            menu = MenuPrint(widget_print)()
            #---------------------------------
            # adicionando os objetos no layout
            grid.add_widget(card1)
            grid.add_widget(card2)
            root.add_widget(grid)
            #--------------------
            layout.add_widget(toolbar)
            layout.add_widget(root)
            layout.add_widget(menu)
            # adicionando o layout no screen
            self.add_widget(layout)
            # métodos dos objetos
            return self
        except Exception as e:
            raise InterfaceException(e)()
#            return e


    def size_porcent(self, widget):
        size_x = widget['size'][0]/widget['size_g'][0]
        size_y = widget['size'][1]/widget['size_g'][1]
        widget.update({'size':(size_x, size_y)})

    def pos_porcent(self, widget):
        pos_y = 1-((widget['pos']['y'] + widget['size'][1])/widget['size_g'][1])
        pos_x = widget['pos']['x']/widget['size'][0]
        widget.update({'pos': {'x': pos_x, 'y': pos_y}})







