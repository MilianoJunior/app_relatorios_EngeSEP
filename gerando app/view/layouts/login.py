from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from functools import partial
from collections import namedtuple


screensize = [360, 731]
background = get_color_from_hex('#565050')
widgets_login = [{'CardLogo':{'size':(329, 126),'pos':(16, 83)}},
                 {'InputEmail':{'size':(329, 65),'pos':(16, 247)}},
                 {'InputSenha':{'size':(329, 126),'pos':(16, 351)}},
                 {'ButtonEnviar':{'size':(172, 37),'pos':(94, 453)}}]


class Login(Screen):
    '''
    		description: class que compoem a interface login

    		return boxlayout com os widget
    '''
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __call__(self):
        print('background: ',background)
        # criar objeto layout
        layout = MDFloatLayout(md_bg_color=background)
        # compor o objeto layout com os widgets
        btn = Button(text='Logo',size_hint=(.2, .2), pos_hint={'x':.2, 'y':.5})
        btn1 = Button(text='play 3',size_hint=(.2, .3), pos_hint={'x':.5, 'y':.5})
        layout.add_widget(btn)
        layout.add_widget(btn1)
        # compor o layout no screen
        self.add_widget(layout)

        return self







