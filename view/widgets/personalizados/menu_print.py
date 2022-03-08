#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# módulos externos
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDToolbar, MDBottomAppBar
from view.widgets.genericos.dropdown import DropDownMenu
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
# módulos da aplicação
from controllers.excpetions.RootException import InterfaceException

class MenuPrint(MDBoxLayout):

    def __init__(self, widget, *args, **kwargs):
        super(MenuPrint, self).__init__()
        self.widget = widget

    def __call__(self):
        try:
            # configurações gerais
            self.size_hint = self.widget['size']
            self.pos_hint = self.widget['pos']
            # configurações do layout para o toolbar
            layout = MDBottomAppBar(md_bg_color = self.widget['cores']['primary'])
            # criação do objeto toolbar
            toolbar = MDToolbar(title='semanal',
                                icon='file-pdf-box',
                                mode='end',
                                icon_color= self.widget['cores']['linedestaque'])
                                # on_action_button = self.print_relatorio(self))
            #------ metodo configuração impressão
            list_menu = ['diário','mensal']
            toolbar.left_action_items = [["cogs", lambda x: self.active_dropdow(x, list_menu)]]
            toolbar.specific_text_color= self.widget['cores']['line']
            #------ metodo impressão
            toolbar.type='bottom'
            toolbar.on_action_button = self.print_relatorio
            # toolbar.action_button.bind('on_release',self.on_action_button)
            # adicionando os widgtes
            layout.add_widget(toolbar)
            self.add_widget(layout)
            return self
        except Exception as e:
            raise InterfaceException(e)()

    def active_dropdow(self, ancora, list_menu):
        try:
            self.menu = DropDownMenu(ancora, list_menu)()
            self.menu.open()
        except Exception as e:
            raise InterfaceException(e)()
    def print_relatorio(self):
        # print(args)
        print('excutando print')
