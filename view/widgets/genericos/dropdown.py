#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from controllers.excpetions.RootException import InterfaceException

class DropDownMenu(MDDropdownMenu):

    def __init__(self, widget, ancora, *args, **kwargs):
        super(DropDownMenu, self).__init__()
        self.widget = widget
        self.ancora = ancora

    def __call__(self):
        try:
            self.width_mult = 4
            self.background_color = self.widget['cores']['primary']
            menu_items = [
                            {
                                "viewclass": "OneLineListItem",
                                "text": f"Item {i}",
                                "height": dp(56),
                                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
                             } for i in range(5)
                        ]
            self.items = menu_items
            return self
        except Exception as e:
            raise InterfaceException(e)()


    def menu_callback(self, *args):
        print('DropMenu', args)