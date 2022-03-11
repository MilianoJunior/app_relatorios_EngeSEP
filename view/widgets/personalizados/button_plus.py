#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.boxlayout import MDBoxLayout
# modulos internos
from controllers.excpetions.RootException import InterfaceException

class ButtonPlus(MDBoxLayout):

    def __init__(self, widget, *args, **kwargs):
        super(ButtonPlus, self).__init__(*args, **kwargs)
        self.md_bg_color = widget['cores']['background']
        self.widget = widget
        self.size_hint = widget['size']
        self.pos_hint = widget['pos']

    def __call__(self):
        try:
            data = { 'leitura': 'connection'}
            btn = MDFloatingActionButton(icon='plus',
                                         md_bg_color=self.widget['cores']['primary'])
            self.add_widget(btn)
            return self
        except Exception as e:
            raise InterfaceException(e)

    def metodo(self, *args):
        print('Button plus: ', args)

