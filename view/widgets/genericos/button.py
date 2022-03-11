from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.boxlayout import MDBoxLayout


class ButtonGeneric(MDBoxLayout):

    def __init__(self, widget, *args, **kwargs):
        super(ButtonGeneric, self).__init__(*args, **kwargs)
        self.md_bg_color = widget['cores']['linedestaque']
        # self.widget = widget
        # self.text = widget['tag']
        # self.icon = widget['icon']
        # self.theme_text_color = "Custom"
        # self.text_color = widget['cores']['line']
        # self.icon_color = widget['cores']['line']
        # self.line_color = widget['cores']['line']
        # self.line_width = 1
        self.size_hint = widget['size']
        self.pos_hint = widget['pos']

    def __call__(self):
        print(self.size)
        # self.update_text_color(self, self.widget['cores']['line'])
        return self