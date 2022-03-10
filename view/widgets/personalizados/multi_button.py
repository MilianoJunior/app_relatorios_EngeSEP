from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.card import MDSeparator
from kivy.properties import ObjectProperty, StringProperty
import os

from matplotlib.pyplot import text
# modulos internos
from controllers.excpetions.RootException import InterfaceException

# font_path =os.path.join(os.environ['FONTS'], 'Spectral','Spectral-Regular.ttf')

class MultiButton(MDBoxLayout):
    recover_pass = StringProperty('recuperar senha')
    create_user = StringProperty('criar usuário')

    def __init__(self, widget, *args, **kwargs):
        super(MultiButton, self).__init__(*args, **kwargs)
        self.orientation = 'horizontal'
        self.widget = widget
        self.size_hint = widget['size']
        self.pos_hint = widget['pos']
        self.md_bg_color = widget['cores']['background']

    def __call__(self):
        try:
            label_a = MDLabel(text='recuperar senha',
                              halign='center',
                              theme_text_color='Custom',
                              text_color = self.widget['cores']['line'])
            linha = MDSeparator(orientation = 'vertical', color=self.widget['cores']['line'])
            label_b = MDLabel(text='criar usuário',
                              halign='center',
                              theme_text_color='Custom',
                              text_color = self.widget['cores']['line'])
            # label_a.bind('on_press', self.redirecionar)
            self.add_widget(label_a)
            self.add_widget(linha)
            self.add_widget(label_b)
            return self
        except Exception as e:
            raise InterfaceException(e)()

    def redirecionar(self, *args):
        print('redirecionar', args)
