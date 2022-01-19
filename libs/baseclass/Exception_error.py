from kivymd.uix.label import MDLabel
from typing import NoReturn
from kivymd.uix.boxlayout import MDBoxLayout
from sys import exc_info
from os import path
from kivy.base import ExceptionHandler, EventLoopBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.base import ExceptionManager

class Singleton(type):

    __instances ={}
    contador = 0

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
            cls.contador = 0
        return cls.__instances[cls]

class E(ExceptionHandler):
    dialog = None

    def __init__(self, obj):
        self.obj = obj

    def callback_not(self, dt):
        self.stopTouchApp()
        self.dialog.dismiss()

    def msg(self, texto, callback):
        if not self.dialog:
            self.dialog = MDDialog(
                text=texto,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=get_color_from_hex("#27979d"),
                        on_release=callback,
                    ),
                ],
            )
        self.dialog.open()
        Clock.schedule_once(callback, 7)

    def stopTouchApp(self):
        EventLoop = EventLoopBase()
        '''Stop the current application by leaving the main loop'''
        if EventLoop is None:
            return
        if EventLoop.status in ('stopped', 'closed'):
            return
        if EventLoop.status != 'started':
            if not EventLoop.stopping:
                EventLoop.stopping = True
                Clock.schedule_once(lambda dt: self.stopTouchApp(), 0)
            return
        EventLoop.close()

    def handle_exception(self, inst):
        self.msg(str(inst), self.callback_not)
        return ExceptionManager.PASS

class Error(metaclass=Singleton):

    error_msg = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def msg(self, e)->NoReturn:
        layout_error = MDBoxLayout()
        exc_type, exc_value, exc_tb = exc_info()
        fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        details = {
                      'arquivo': fname,
                      'linha'  : exc_tb.tb_lineno,
                      'type'    : exc_type.__name__,
                      'message' : e,
                      'path'    : path.abspath(__file__),
                    }

        print('##################')
        print('Classe error: ',self.contador)
        print(e)
        print(details)
        print('##################')

        if self.error_msg is None:
            self.error_msg = True
            texto = ''
            for name, value in details.items():
                texto += f'\n{str(name)} : {value}'
            layout_error.add_widget(MDLabel(text=str(texto),
                                            halign="center"))
        return layout_error

#class ExceptionError():
#
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#
#    def notify(self):
#        exc_type, exc_value, exc_tb = exc_info()
#        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#        details = {
#                      'arquivo': fname,
#                      'linha'  : exc_tb.tb_lineno,
#                      'type'    : exc_type.__name__,
#                      'message' : e,
#                      'path'    : path.abspath(__file__),
#                    }
#        for name,value in details.items():
#            texto += f'\n{str(name)} : {value}'
#        snackbar = Snackbar(text=texto,
#                            snackbar_x="10dp",
#                            snackbar_y="10dp")
#        a = (Window.width - (snackbar.snackbar_x * 2))
#        snackbar.size_hint_x = a / Window.width
#        snackbar.buttons = [MDFlatButton(text="OK",
#                                         text_color=(1, 1, 1, 1),
#                                         on_release=snackbar.dismiss)]
#        snackbar.open()