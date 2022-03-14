from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
import os
# modulos internos
from controllers.excpetions.RootException import InterfaceException

# font_path =os.path.join(os.environ['FONTS'], 'Spectral','Spectral-Regular.ttf')

class InputConfig(MDBoxLayout):

    def __init__(self, widget, *args, **kwargs):
        super(InputConfig, self).__init__(*args, **kwargs)
        self.orientation='vertical'
        self.widget = widget
        self.size_hint_y = None
        self.spacing = 10
        self.height = 125
        self.padding = [12,0,12,0]

    def __call__(self):
        try:
            self.widget.update({'tag': 'ID', 'icon':'table-row'})
            input_id = InputMy(self.widget)
            self.widget.update({'tag': 'Registro', 'icon':'code-tags'})
            input_register = InputMy(self.widget)
            self.add_widget(input_id)
            self.add_widget(input_register)
            return self
        except Exception as e:
            raise InterfaceException(e)()


class InputMy(MDTextField):

    def __init__(self, widget, *args, **kwargs):
        super(InputMy, self).__init__(*args, **kwargs)
        self.hint_text=widget['tag']
        self.mode="rectangle"
        self.icon_right=widget['icon']
        self.icon_right_color = widget['cores']['linedestaque']
        self.hint_text_color = widget['cores']['line']
        self.current_hint_text_color = widget['cores']['line']