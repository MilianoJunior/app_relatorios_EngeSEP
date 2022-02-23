__all__ = ['EngeSEPRelatorios']
__version__ = '0.1'
__author__ = 'Miliano Fernandes de oliveira junior - EngeSEP'

# definição do modo de desenvolvimento
MODO = 'desenvolvimento'
if MODO == 'desenvolvimento':
    from controllers.mode.reload import run

# bibliotecas importadas
from kivy.core.window import Window
from kivymd.app import MDApp
from pathlib import Path
import os
# minhas classes
from view.composite import Composite

# configurações das variaveis de ambiente
SYSTEM_OPERACIONAL = os.uname()
BASE_DIR = Path(__file__).resolve().parent.parent
os.environ['IMAGENS'] = os.path.join(BASE_DIR,f"APPDB{os.sep}assets{os.sep}imagens")

class EngeSEPRelatorios(MDApp):

    def __init__(self, *args, **kwargs):
        super(EngeSEPRelatorios, self).__init__(*args, **kwargs)
        Window.system_size = [360, 731]
        Window.top = 40
        Window.left = 10

    def build(self):
        return Composite()()

    def on_start(self):
        if MODO == 'desenvolvimento':
            run(self)


if __name__ == "__main__":
    app = EngeSEPRelatorios()
    app.run()


#source /home/jrmfilho23/Documentos/EngeSEP/apps/APPDB/ambiente/ambienteDB/bin/activate