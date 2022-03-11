from re import M
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.boxlayout import MDBoxLayout


class ButtonGeneric(MDBoxLayout):

    def __init__(self, widget, *args, **kwargs):
        super(ButtonGeneric, self).__init__(*args, **kwargs)
        self.md_bg_color = widget['cores']['background']
        self.widget = widget
        self.size_hint = widget['size']
        self.pos_hint = widget['pos']

    def __call__(self):
        btn = MDRectangleFlatIconButton(text=self.widget['tag'],
                                        icon=self.widget['icon'],
                                        theme_text_color='Custom',
                                        text_color=self.widget['cores']['line'],
                                        icon_color = self.widget['cores']['line'],
                                        line_color = self.widget['cores']['line'])
        self.add_widget(btn)
        return self

    def metodo(self,*args):
        print('Button generic: ', args)