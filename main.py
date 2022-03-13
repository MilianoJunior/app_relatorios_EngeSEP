__all__ = ['EngeSEPRelatorios']
__version__ = '0.1'
__author__ = 'Miliano Fernandes de oliveira junior - EngeSEP'

# definição do modo de desenvolvimento
MODO = 'desenvolvimento'
if MODO == 'desenvolvimento':
    from controllers.mode.reload import run

# bibliotecas importadas
#from kivy.base import ExceptionManager
from kivy.core.window import Window
from kivy.uix.button import Button
from kivymd.app import MDApp
from pathlib import Path
import os
# minhas classes
from view.composite import Composite
from assets.fonts.font import font_choice
from controllers.excpetions.RootException import InterfaceException

# configurações das variaveis de ambiente
SYSTEM_OPERACIONAL = os.uname()
BASE_DIR = os.getcwd()
os.environ['ROOT_ENGESEP'] = BASE_DIR
os.environ['IMAGENS'] = os.path.join(BASE_DIR,f"assets{os.sep}imagens")
os.environ['FONTS'] = os.path.join(BASE_DIR,f"assets{os.sep}fonts")

# instancia principal do APP
class EngeSEPRelatorios(MDApp):

    def __init__(self, *args, **kwargs):
        super(EngeSEPRelatorios, self).__init__(*args, **kwargs)
        self.theme_cls.font_styles.update(font_choice('Spectral'))
        Window.system_size = [360, 731]
        Window.top = 40
        Window.left = 1600

    def build(self):
        try:
            return Composite()()
            # return Button(text='oi')
        except:
            return InterfaceException.box

    def on_stop(self):
        return super().on_stop()

    def on_start(self):
        if MODO == 'desenvolvimento':
            run(self)


if __name__ == "__main__":
    app = EngeSEPRelatorios()
    app.run()


#source /home/jrmfilho23/Documentos/EngeSEP/apps/APPDB/ambiente/ambienteDB/bin/activate