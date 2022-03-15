from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton, MDFlatButton
from kivymd.uix.card import MDSeparator
import os
# modulos internos
from controllers.excpetions.RootException import InterfaceException
from routes.routes import Routes 

# font_path =os.path.join(os.environ['FONTS'], 'Spectral','Spectral-Regular.ttf')

class MultiButton(MDBoxLayout):

    def __init__(self, widget, *args, **kwargs):
        super(MultiButton, self).__init__(*args, **kwargs)
        self.orientation = 'horizontal'
        self.spacing = 2
        self.padding = [0,0,0,0]
        self.widget = widget
        self.size_hint = widget['size']
        self.pos_hint = widget['pos']
        self.md_bg_color = widget['cores']['line']

    def __call__(self):
        try:
            box1 = MDBoxLayout(md_bg_color = self.widget['cores']['background'],
                                orientation= 'vertical')
            box2 = MDBoxLayout(md_bg_color = self.widget['cores']['background'],
                                orientation= 'vertical')
            btn_a = MDTextButton(text='criar usuário',
                                 theme_text_color='Custom',
                                 text_color = self.widget['cores']['line'],
                                 pos_hint={'x': 0.2,'y': 0.1})
            btn_b = MDTextButton(text='recuperar senha',
                                 theme_text_color='Custom',
                                 text_color = self.widget['cores']['line'],
                                 pos_hint={'x': 0.1,'y': 0.1},
                                 md_bg_color = self.widget['cores']['background'])
            btn_a.bind(on_press=self.redirecionar)
            btn_b.bind(on_press=self.redirecionar)
            box1.add_widget(btn_a)
            box2.add_widget(btn_b)
            self.add_widget(box1)
            self.add_widget(box2)
            return self
        except Exception as e:
            raise InterfaceException(e)()

    def redirecionar(self, *args):
        
        Routes.redirect()
        print('redirecionar', args[0].text)
