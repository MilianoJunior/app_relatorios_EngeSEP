from controllers.excpetions.RootException import InterfaceException
from view.layouts.interface import Interface
from view.layouts.login import Login
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
from kivy.uix.button import Button
import random


class Composite(ScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cont = 0

    def __call__(self):
        try:
            self.add_widget(Login(name='login')())
            self.add_widget(Interface(name='interface')())
            self.current = 'interface'
#            Clock.schedule_interval(self.slide, 2)
            return self
        except Exception as e:
            return InterfaceException(e)()

    def slide(self, *args):
        self.current = random.choice(self.screen_names)
#        print(self.current_screen)
