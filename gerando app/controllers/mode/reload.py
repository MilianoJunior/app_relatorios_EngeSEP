from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Thread
from kivy.core.window import Window
from datetime import datetime
from multiprocessing import Process
import os, signal

registro_modulos = ['main.py', 'composite.py', 'reload.py','login.py',
                    'interface.py','toolbar_menu.py','card_info.py',
                    'menu_print.py']

def aux(*args):
    os.system("gnome-terminal -- python3 main.py")

class KvHandler(FileSystemEventHandler):

    def __init__(self, app, **kwargs):
        super(KvHandler, self).__init__(**kwargs)
        self.app = app

    def on_modified(self, event):
        for s in registro_modulos:
            if os.path.basename(event.src_path) == s:
                print('####################################')
                print('Hora: ', datetime.now())
                print('Houve modificação no arquivo: ',s)
                print('pid aplicação: ',os.getppid())
                self.app.get_running_app().stop()
                p = Process(target=aux)
                p.start()
                p.join()
#                th = Thread(target=aux, args=(1,))
#                th.start()
#                os.system("clear")
#                os.system("ls -a")-
#                Window.close()-----

                exit()

#                print(self.app.get_running_app().stop())
#                os.system("gnome-terminal -- python3 main.py")---
#
#
#
#                os.kill(os.getppid(), signal.SIGHUP)---
                return
#                self.callback(os.path.basename(event.src_path))--

def run(app: object):
    PATH = "/home/jrmfilho23/Documentos/EngeSEP/apps_mvc/APPDB"
    o = Observer()
    o.schedule(KvHandler(app), PATH, recursive=True)
    o.start()

