#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from controllers.excpetions.RootException import InterfaceException

class DropDownMenu(MDDropdownMenu):
    '''
    description: dropdow generic for widgets
    args: ancora: object, list_menu: list[str]
    return object
    '''
    def __init__(self, ancora, list_menu, *args, **kwargs):
        super(DropDownMenu, self).__init__()
        self.list_menu = list_menu
        self.ancora = ancora

    def __call__(self):
        try:
            menu_items = [
                {
                    "viewclass": "OneLineListItem",
                    "icon": "git",
                    "height": dp(46),
                    "text": f"{i}",
                    "on_release": lambda x=i: self.set_item(x),
                } for i in self.list_menu]
            self.items = menu_items
            self.caller = self.ancora
            self.width_mult = 2
            return self
        except Exception as e:
            raise InterfaceException(e)()

    def menu_callback(self, *args):
        print('EsperaDropMenu', args)

    def set_item(self, text_item):
        print('Execução do controller: ',text_item)
        self.dismiss()