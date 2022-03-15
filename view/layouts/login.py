# módulos externos
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
# modulos da aplicação
from view.widgets.genericos.button import ButtonGeneric
from view.widgets.genericos.input import InputGeneric
from view.widgets.personalizados.menu_logo import MenuLogo
from view.widgets.personalizados.multi_button import MultiButton
from assets.themas_color import cores
from controllers.excpetions.RootException import InterfaceException
from routes.routes import Routes

# variaveis globais de configuração dos widgets

thema = 'dark'
widget_logo = {'name':'MenuLogo',
               'pos':{'x': 15, 'y': 76},
               'size':(329,126),
               'size_g':(360,730),
               'cores': cores[thema]}

widget_email = {'name':'Email',
                'pos':{'x': 15, 'y': 230},
                'size':(329,56),
                'size_g':(360,730),
                'tag': 'Email',
                'icon': "at",
                'value': False,
                'cores':cores[thema]}

widget_senha = {'name':'Password',
                'pos':{'x': 15, 'y': 314},
                'size':(329,56),
                'size_g':(360,730),
                'tag': 'Senha',
                'icon': "eye-outline",
                'value': True,
                'cores':cores[thema]}

widget_button = {'name':'Button',
                'pos':{'x': 93, 'y': 398},
                'size':(172,37),
                'size_g':(360,730),
                'tag': '        ENTRAR        ',
                'icon': "location-enter",
                'cores':cores[thema]}

widget_multi = {'name':'MultiButton',
                'pos':{'x': 61, 'y': 463},
                'size':(236,28),
                'size_g':(360,730),
                'tag': ['recuperar senha', 'criar usuário'],
                'cores':cores[thema]}


widgets = [widget_logo, widget_email, widget_senha, widget_button, widget_multi]

class Login(Screen):
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
            #----------------------------------
            logo = MenuLogo(widget_logo)()
            #----------------------------------
            input_email = InputGeneric(widget_email)()
            #---------------------------------
            input_senha = InputGeneric(widget_senha)()
            #------------------------------------
            enviar = ButtonGeneric(widget_button)()
            #----------------------------------
            multi = MultiButton(widget_multi)()
            # vinculando os metodos
            enviar.children[0].bind(on_press=self.logar)
            # adicionando os objetos no layout
            layout.add_widget(logo)
            layout.add_widget(input_email)
            layout.add_widget(input_senha)
            layout.add_widget(enviar)
            layout.add_widget(multi)
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

    def logar(self, *args):
        print('logando: ', args)
        data={'value':'principal'}
        Routes.redirect(data)







