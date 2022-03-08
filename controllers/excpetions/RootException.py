from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from os import path
import sys

class InterfaceException(BaseException):

    data_: list = []
    box: object = MDBoxLayout(orientation='vertical')

    def __init__(self, data='objeto inicial'):
        self.data_.append(data)

    def __call__(self):
        exc_type, exc_value, exc_tb = sys.exc_info()
        fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        details = {
                      'arquivo': fname,
                      'linha'  : exc_tb.tb_lineno,
                      'type'    : exc_type.__name__,
                      'message' : self.data_[-1],
                      'path'    : path.abspath(__file__),
                    }
        texto = ''
        for name, value in details.items():
            texto += f'\n{str(name)} : {value}'
        self.box.add_widget(MDLabel(text=str(texto),
                                        halign="center"))








