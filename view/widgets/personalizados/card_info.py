#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# módulos externos
from kivymd.uix.boxlayout import MDBoxLayout
#from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.card import MDSeparator
#from kivy.graphics import Rectangle, Color
import os
# módulos da aplicação


class CardInfo(MDCard):

    def __init__(self, widget, *args, **kwargs):
        super(CardInfo, self).__init__()
        self.widget = widget

    def __call__(self):
        # configurações da base MDCard
        self.size_hint = (None, None)
        self.size = self.widget['size']
        self.pos_hint = self.widget['pos']
        self.md_bg_color = self.widget['cores']['primary']
        self.orientation = 'vertical'
        self.elevation = 10
        # Configurações do titulo
        data = 'última medição: 22/02/2022 15:00'
        title = MDToolbar(title=self.widget['tag'])
        title.left_action_items = [["lightning-bolt"]]
        title.right_action_items = [["backup-restore", data]]
        title.md_bg_color = self.widget['cores']['primary']
        title.specific_text_color= self.widget['cores']['line']
        # Separação
        sp = MDSeparator(height="1dp", color=self.widget['cores']['line'])
        # Configurações Body
        box = MDBoxLayout(orientation='vertical', md_bg_color=self.widget['cores']['primary'])
        box_relative = MDRelativeLayout()
        info = MDLabel(text= f'{self.widget["value"]} KW',
                        theme_text_color="Custom",
                        text_color=self.widget['cores']['line'],
                        halign="center",
                        font_style="H5")
        img_path =os.path.join(os.environ['IMAGENS'], 'Ellipse.png')
        img = Image(source=img_path,size=[344, 250])
        box_relative.add_widget(img)
        box_relative.add_widget(info)
        box.add_widget(box_relative)
        # adicionando os elementos ao layout
        self.add_widget(title)
        self.add_widget(sp)
        self.add_widget(box)

        return self
