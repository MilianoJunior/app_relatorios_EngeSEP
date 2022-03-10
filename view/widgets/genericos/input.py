from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
import os
# modulos internos
from controllers.excpetions.RootException import InterfaceException

# font_path =os.path.join(os.environ['FONTS'], 'Spectral','Spectral-Regular.ttf')

class InputGeneric(MDBoxLayout):

    def __init__(self, widget, *args, **kwargs):
        super(InputGeneric, self).__init__(*args, **kwargs)
        self.widget = widget
        self.size_hint = widget['size']
        self.pos_hint = widget['pos']
        self.padding = [12,0,12,0]

    def __call__(self):
        try:
            input_widget = MDTextField(hint_text=self.widget['tag'],
                                    mode="rectangle",
                                    icon_right=self.widget['icon'],
                                    opacity=.9)

            input_widget.opposite_colors = True
            input_widget.text_color = self.widget['cores']['linedestaque']
            input_widget.password = self.widget['value']
            input_widget.icon_right_color = self.widget['cores']['linedestaque']
            input_widget.hint_text_color = self.widget['cores']['line']
            input_widget.current_hint_text_color = self.widget['cores']['line']
            # input_widget.font_name_hint_text = font_path
            self.add_widget(input_widget)
            return self
        except Exception as e:
            raise InterfaceException(e)()

