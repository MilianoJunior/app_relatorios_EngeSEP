#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# módulos externos
from kivymd.uix.boxlayout import MDBoxLayout
# módulos da aplicação


class MenuPrint(MDBoxLayout):

    def __init__(self, widget, *args, **kwargs):
        super(MenuPrint, self).__init__()
        self.widget = widget
#        self.size = ListProperty([])

    def __call__(self):
        self.size_hint = self.widget['size']
        self.pos_hint = self.widget['pos']
        self.md_bg_color = self.widget['cores']['primary']

        return self