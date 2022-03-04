#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# módulos externos
from kivymd.uix.toolbar import MDToolbar
# módulos internos
from controllers.excpetions.RootException import InterfaceException

class ToolbarMenu(MDToolbar):

    def __init__(self, widget, *args, **kwargs):
        super(ToolbarMenu, self).__init__()
        self.widget = widget

    def __call__(self):
        try:
            self.title = 'EngeSEP' + '[color=03DAC6][size=26][sub]' + 'relatórios' + '[/sub][/size][/color]'
            self.left_action_items = [["menu"]]
            self.right_action_items = [["account-circle"]]
            self.type = 'top'
            self.size_hint = self.widget['size']
            self.pos_hint = self.widget['pos']
            self.md_bg_color = self.widget['cores']['primary']
            self.specific_text_color= self.widget['cores']['line']
            return self
        except Exception as e:
            raise InterfaceException(e)()
