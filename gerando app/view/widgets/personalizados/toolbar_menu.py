#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# módulos externos
from kivymd.uix.toolbar import MDToolbar

class ToolbarMenu(MDToolbar):

    def __init__(self, widget, *args, **kwargs):
        super(ToolbarMenu, self).__init__()
        self.widget = widget
#        self.size = ListProperty([])

    def __call__(self):
        self.title = 'EngeSEP' + '[color=03DAC6][size=26][sub]' + 'relatórios' + '[/sub][/size][/color]'
        self.left_action_items = [["menu"]]
        self.right_action_items = [["account-circle"]]
        self.type = 'top'
        self.size_hint = self.widget['size']
        self.pos_hint = self.widget['pos']
        self.md_bg_color = self.widget['cores']['primary']

        return self
