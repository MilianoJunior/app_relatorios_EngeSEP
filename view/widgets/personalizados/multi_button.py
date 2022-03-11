from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton
from kivymd.uix.card import MDSeparator
import os
# modulos internos
from controllers.excpetions.RootException import InterfaceException

# font_path =os.path.join(os.environ['FONTS'], 'Spectral','Spectral-Regular.ttf')

class MultiButton(MDBoxLayout):

    def __init__(self, widget, *args, **kwargs):
        super(MultiButton, self).__init__(*args, **kwargs)
        self.orientation = 'horizontal'
        self.spacing = 10
        self.padding = [1,1,1,1]
        self.widget = widget
        self.size_hint = widget['size']
        self.pos_hint = widget['pos']
        self.md_bg_color = widget['cores']['linedestaque']

    def __call__(self):
        try:
            linha = MDSeparator(orientation = 'vertical', color=self.widget['cores']['line'])
            box1 = MDBoxLayout(md_bg_color = self.widget['cores']['primary'])
            box2 = MDBoxLayout(md_bg_color = self.widget['cores']['primary'])
            label_a = MDTextButton(text='criar usuário', 
                                   theme_text_color='Custom',
                                   text_color = self.widget['cores']['line'],
                                   pos_hint={'x': 0.9,'center_y': 0.5})
            label_b = MDTextButton(text='recuperar senha', 
                                   theme_text_color='Custom',
                                   text_color = self.widget['cores']['line'],
                                   size_hint=(.5, 1),
                                   pos_hint={'center_x': 0.5,'center_y': 0.5})
            label_a.bind(on_press=self.redirecionar)
            label_b.bind(on_press=self.redirecionar)
            box1.add_widget(label_a)
            # self.add_widget(linha)
            # self.add_widget(label_b)
            self.add_widget(box1)
            self.add_widget(box2)
            return self
        except Exception as e:
            raise InterfaceException(e)()

    def redirecionar(self, *args):
        print('redirecionar', args[0].text)
