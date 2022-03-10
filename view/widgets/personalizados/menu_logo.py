#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# módulos externos
from kivymd.uix.boxlayout import MDBoxLayout
#from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.card import MDSeparator
#from kivy.graphics import Rectangle, Color
import os
# módulos da aplicação
from controllers.excpetions.RootException import InterfaceException

class MenuLogo(MDBoxLayout):

    def __init__(self, widget, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = widget
        self.md_bg_color = self.widget['cores']['primary']
        self.orientation = 'horizontal'
        # self.size_hint = (None, None)
        self.size_hint = self.widget['size']
        self.pos_hint = self.widget['pos']
        self.padding = [10,10,10,10]
        self.radius = [10,10,10,10]

    def __call__(self):
        try:
            # configurações da base MDCard
            box_img = MDBoxLayout(orientation = 'horizontal',
                                  size_hint=(.4, 1),
                                  md_bg_color = self.widget['cores']['primary'],
                                  radius = [10,10,10,10])
            box_label = MDBoxLayout(orientation = 'vertical',
                                  size_hint=(.6, 1),
                                  md_bg_color = self.widget['cores']['primary'],
                                  radius = [10,10,10,10],
                                  padding = [0,0,0,0])
            texto = """[size=24]EngeSEP[/size]
          [size=12][color=03DAC6]Relatórios[/color][/size]"""
            font_path =os.path.join(os.environ['FONTS'], 'Spectral','Spectral-Regular.ttf')
            title1 = Label(text=texto, 
                           font_name=font_path, 
                           text_size=self.size,
                           halign='center',
                           valign='middle',
                           markup=True)
            img_path =os.path.join(os.environ['IMAGENS'], 'Ellipse_small.png')
            img = Image(source = img_path)

            box_img.add_widget(img)
            box_label.add_widget(title1)
            # box_label.add_widget(subtitle)

            self.add_widget(box_img)
            self.add_widget(box_label)

            return self

        except Exception as e:
            raise InterfaceException(e)()

    def resize(self, *args):
        print('resize: ',args)
    
'''
class MenuLogo(MDCard):

    def __init__(self, widget, *args, **kwargs):
        super(MenuLogo, self).__init__()
        self.widget = widget

    def __call__(self):
        try:
            # configurações da base MDCard
            print(self.widget['pos'])
            print(self.widget['size'])
            # self.size_hint = (None, None)
            self.size_hint = self.widget['size']
            self.pos_hint = self.widget['pos']
            self.md_bg_color = self.widget['cores']['primary']
            self.orientation = 'vertical'
            self.elevation = 10
            # Configurações do logo
            img_path =os.path.join(os.environ['IMAGENS'], 'card_logo.png')
            img = Image(source=img_path) #size=[329, 126])
            # adicionando os elementos ao layout
            self.add_widget(img)

            return self

        except Exception as e:
            raise InterfaceException(e)()

'''
