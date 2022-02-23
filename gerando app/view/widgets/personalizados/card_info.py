#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# módulos externos
#from kivymd.uix.boxlayout import MDBoxLayout
#from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.list import IconLeftWidget, TwoLineAvatarIconListItem, MDList
#from kivy.graphics import Rectangle, Color
import os
# módulos da aplicação


class CardInfo(MDCard):

    def __init__(self, widget, *args, **kwargs):
        super(CardInfo, self).__init__()
        self.widget = widget
#        self.size = ListProperty([])

    def __call__(self):
        # configurações da base MDCard
        self.size_hint = self.widget['size']
        self.pos_hint = self.widget['pos']
        self.md_bg_color = self.widget['cores']['primary']
        self.orientation = 'vertical'
        # Configurações do titulo
        data = 'última medição: 22/02/2022 15:00'
        title = MDToolbar(title='UG-01')
        title.left_action_items = [["lightning-bolt"]]

        title.right_action_items = [["backup-restore", data]]
        title.md_bg_color = self.widget['cores']['primary']

#        title = MDLabel(text='UG-01',
#                        theme_text_color="Primary",
#                        font_style="H5")

        # Configurações do body
        img_path =os.path.join(os.environ['IMAGENS'], 'Ellipse.png')
        img = Image(source=img_path,size=[344, 250])

        # adicionando os elementos ao layout
        self.add_widget(title)
        self.add_widget(img)



        return self
