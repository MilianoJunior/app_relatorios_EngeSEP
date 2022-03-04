#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# módulos externos
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDToolbar, MDBottomAppBar
#from view.widgets.genericos.dropdown import DropDownMenu
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
# módulos da aplicação
from controllers.excpetions.RootException import InterfaceException


class MenuPrint(MDBoxLayout):

    def __init__(self, widget, *args, **kwargs):
        super(MenuPrint, self).__init__()
        self.widget = widget
#        self.size = ListProperty([])

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
            toolbar.left_action_items = [["cogs", lambda x: self.active_dropdow(x)]]
#            toolbar.on_action_button = self.active_dropdow(toolbar.icon)
            toolbar.specific_text_color= self.widget['cores']['line']
            toolbar.type='bottom'
#            self.ids['toolbar'] = toolbar
            # adicionando os widgtes
            layout.add_widget(toolbar)
            self.add_widget(layout)
            return self
        except Exception as e:
            raise InterfaceException(e)()

    def active_dropdow(self, button):
        try:
            print(button)
            menu_items = [
                {
                    "viewclass": "OneLineListItem",
                    "icon": "git",
                    "height": dp(56),
                    "text": f"{i}",
                } for i in ['Diário', 'Mensal']]
            print(menu_items)
            print(self.ids)
            self.menu = MDDropdownMenu(
                caller=button,
                items=menu_items,
                width_mult=2,
            )
            self.menu.open()
        except Exception as e:
            raise InterfaceException(e)()
    def set_item(self, args):
        print(args)
