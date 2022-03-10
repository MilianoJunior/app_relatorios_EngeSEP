from kivy.uix.screenmanager import ScreenManager
import random
# meus modulos
from controllers.excpetions.RootException import InterfaceException
from view.layouts.interface import Interface
from view.layouts.login import Login
from view.layouts.config import Config
from view.layouts.create_user import CreateUser
from view.layouts.error import Error
from view.layouts.recover import RecoverPassword
from routes.routes import define_manager


class Composite(ScreenManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # screen_manager = self

    def __call__(self):
        try:
            self.add_widget(Login(name='login')())
            self.add_widget(Interface(name='principal')())
            self.add_widget(Config(name='config')())
            self.add_widget(CreateUser(name='createuser')())
            self.add_widget(Error(name='error')())
            self.add_widget(RecoverPassword(name='recover')())
            self.current = 'login'
            define_manager(self)
            return self
        except Exception as e:
            raise InterfaceException(e)()

    def slide(self, *args):
        self.current = random.choice(self.screen_names)

