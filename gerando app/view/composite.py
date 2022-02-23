from view.layouts.interface import Interface
from view.layouts.login import Login
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
import random


class Composite(ScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cont = 0

    def __call__(self):
        self.add_widget(Login(name='login')())
        self.add_widget(Interface(name='interface')())
        self.current = 'interface'
#        Clock.schedule_interval(self.slide, 2)
        return self

    def slide(self, *args):
        self.current = random.choice(self.screen_names)
#        print(self.current_screen)

