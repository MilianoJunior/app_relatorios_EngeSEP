#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.boxlayout import MDBoxLayout
# modulos internos
from controllers.excpetions.RootException import InterfaceException

class ButtonPlus:

    def __init__(self, widget):
        self.widget = widget

    def __call__(self):
        try:
            btn = MDFloatingActionButton(icon='plus',
                                         md_bg_color=self.widget['cores']['primary'],
                                         pos_hint=self.widget['pos'])
            return btn
        except Exception as e:
            raise InterfaceException(e)

