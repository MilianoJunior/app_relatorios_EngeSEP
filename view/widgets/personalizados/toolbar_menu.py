#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# módulos externos
from kivymd.uix.toolbar import MDToolbar
# módulos internos
from controllers.excpetions.RootException import InterfaceException
from view.widgets.genericos.dropdown import DropDownMenu


list_screen = [{'route': 'redirect',
                'value': 'login',
                'data' : 'login'},
                {'route': 'redirect',
                'value': 'principal',
                'data' : 'principal'},
                {'route': 'redirect',
                'value': 'config',
                'data' : 'configurações'}]

list_user =  [{'route': 'get',
                'value': 'dark',
                'data' : 'modo escuro'},
                {'route': 'get',
                'value': 'sair',
                'data' : 'sair'}]


class ToolbarMenu(MDToolbar):

    def __init__(self, widget, *args, **kwargs):
        super(ToolbarMenu, self).__init__()
        self.widget = widget

    def __call__(self):
        try:
            self.title = 'EngeSEP' + '[color=03DAC6][size=26][sub]' + 'relatórios' + '[/sub][/size][/color]'
            self.left_action_items = [["menu", lambda x: self.set_menu(x, list_screen)]]
            self.right_action_items = [["account-circle",lambda x: self.set_menu(x, list_user)]]
            self.type = 'top'
            self.size_hint = self.widget['size']
            self.pos_hint = self.widget['pos']
            self.md_bg_color = self.widget['cores']['primary']
            self.specific_text_color= self.widget['cores']['line']
            return self
        except Exception as e:
            raise InterfaceException(e)()

    def set_menu(self, ancora, list_menu):
        try:
            self.menu = DropDownMenu(ancora, list_menu)()
        except Exception as e:
            raise InterfaceException(e)()