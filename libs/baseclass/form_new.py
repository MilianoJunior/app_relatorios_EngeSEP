#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivy.utils import (get_random_color, get_color_from_hex)
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
import asynckivy as ak
from libs.baseclass.Exception_error import Error
from libs.baseclass.function_form import (inicializacao,
                                          conectar_aux,
                                          painel_aviso)
from libs.baseclass.observer_db import Subject
from kivy.properties import (NumericProperty, StringProperty,
                             ObjectProperty, ListProperty)

erro = Error()

inputs = {
            'inputs_nome'  : 'Nome da usina hidrelétrica',
            'inputs_local' : 'Localização',
            'inputs_ip_a'  : 'IP Gerador 1',
            'inputs_ip_b'  : 'IP Gerador 2',
            'inputs_port_a': 'Registro CLP: Energia gerador 1',
            'inputs_port_b': 'Registro CLP: Energia gerador 2',
            'inputs_id_a'  : 'Identificação gerador 1',
            'inputs_id_b'  : 'Identificação gerador 2',
            'inputs_nivel' : 'Registro CLP nível reservatório',
            'inputs_time' :  'Tempo',
        }
entrada = ['Usina D','Chapecó','192.168.10.2','192.168.10.2','MW1200',
           'MW1200','UG-01','UG-02','MW1000','15']

class FormNew(MDFloatLayout):
    spinner = None
    subject = None
    def __init__(self,objeto: object, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subject = objeto
        Clock.schedule_once(self.load_data,3)

    def __call__(self, *args, **kwargs):
        try:
            self.grid_inputs()
            return self
        except Exception as e:
            erro.msg(e)

    def load_data(self, *args):
        inicializacao(self)

    def update(self, subject: Subject) -> None:
        painel_aviso('Atualizando o banco de dados',
                     'ligado',
                     button=False,
                     auto_close=True,
                     tempo=1)


    def grid_inputs(self):
        layout = GridLayout(cols=2)
        i = 0
        for chave, value in inputs.items():
            box = MDBoxLayout(orientation='horizontal',
                              padding=[20, 10, 10, 10],
                              md_bg_color=get_color_from_hex('#1E1F23'),
                              spacing=10)
            input_text = MDTextField(hint_text=value,
#                                     text=entrada[i],
                                     current_hint_text_color=
                                     get_color_from_hex("#27979d"))
            self.ids[chave] = input_text
            box.add_widget(input_text)
            layout.add_widget(box)
            i += 1
        enviar = MDRaisedButton(text='Conectar',
                                pos_hint={"x": .2, "center_y": .5},
                                md_bg_color=get_color_from_hex("#27979d"),
                                on_release=self.conectar)
        self.ids['button_enviar'] = enviar
        layout.children[0].add_widget(enviar)
        self.ids['layout'] = layout
        self.add_widget(layout)

    def conectar(self, *args):
        entradas = {}
        for name, value in self.ids.items():
            if name in inputs.keys():
                entradas[name] = value
        state = conectar_aux(entradas,self)



























