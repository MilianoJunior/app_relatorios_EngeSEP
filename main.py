__all__ = ['EngeSEPDB']
__version__ = '0.1'
__author__ = 'Miliano Fernandes de oliveira junior - EngeSEP'

#token = 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

from kivy.config import Config
Config.set('kivy', 'desktop', 1)
Config.set('graphics', 'borderless', 1)
Config.set('graphics', 'show_cursor', [0,1][1])
Config.write()
import os
import sys
from pathlib import Path
from kivy.core.window import Window
from kivy.factory import Factory  # NOQA: F401
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.base import ExceptionManager, ExceptionHandler, EventLoopBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.uix.button import Button
import multiprocessing
Clock.max_iteration = 20
#from libs.baseclass.fonts import Fonts
from kivy.clock import mainthread
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from memory_profiler import memory_usage
from libs.baseclass.Exception_error import E

registrar_componentes = ['main.py', 'navigation_bar.py', 'form_new.py',
                         'table.py', 'date.py','navigation_bar.kv',
                         'function_form.py','clp_connection.py',
                         'connection_db.py','data.py','relatorio.py',
                         'periodo.py','pdf.py']


def abrir():
    os.system("clear")
    os.system("python3 main.py")


class KvHandler(FileSystemEventHandler):
    def __init__(self, callback, target, **kwargs):
        super(KvHandler, self).__init__(**kwargs)
        self.callback = callback
        self.target = target

    def on_modified(self, event):
        for s in registrar_componentes:
            if os.path.basename(event.src_path) == s:
                self.callback(os.path.basename(event.src_path))


os.environ["ENGESEP_LANG"] = "1"

if getattr(sys, "frozen", False):
    os.environ["ENGESEP_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__))
    os.environ["ENGESEP_ROOT"] = str(Path(__file__).parent)
os.environ["ENGESEP_ASSETS"] = os.path.join(
        os.environ["ENGESEP_ROOT"], f"assets{os.sep}")

os.environ['PATH']


class EngeSEPDB(MDApp):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ExceptionManager.add_handler(E(self))
        self.contador = 0
        self.title = "Sistema de relatórios - versão desenvolvimento"
        self.icon = os.path.join(os.environ["ENGESEP_ASSETS"], "logo.png")
        self.theme_cls.primary_palette = "Teal"
        Window.system_size = [900, 600]
        Window.top = 40
        Window.left = 10

    def build(self):
        TARGET = [files for files in os.listdir(
                f"{os.environ['ENGESEP_ROOT']}")]
        PATH = os.environ["ENGESEP_ROOT"]
        o = Observer()
        o.schedule(KvHandler(self.update, TARGET), PATH, recursive=True)
        o.start()
        KV_DIR = f"{os.environ['ENGESEP_ROOT']}/libs/kv/"
        for kv_file in os.listdir(KV_DIR):
            with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
                if kv_file == 'navigation_bar.kv':
                    build = Builder.load_string(kv.read())
        return build

    def minimizar(self, *largs, **kwargs):
#        self.on_stop()
        print(os.getpid())
        mem_usage = memory_usage(os.getpid(), interval=.2, timeout=1, max_usage=True)
        print(mem_usage)
        print('main')
#        Window.minimize()

    def rail_open(self):
        pass

    def on_stop(self, *args):
        print('on_stop: ativado')
        self.title = str(self.contador)
        print('objeto : ', id(self))
        Window.close()

    @mainthread
    def update(self, target, *args):
        print('executando update')
        self.stop()
        pc2 = multiprocessing.Process(target=abrir)
        pc2.start()
        pc2.join()
        self.stop()
        self.contador += 1
        print('executando update')


if __name__ == "__main__":
    app = EngeSEPDB()
    app.run()
