from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
from multiprocessing import Process
import os

arquivos = []
def modulos(path):
    global arquivos
    for obj in os.listdir(path):
        if obj.endswith(".py") and os.path.isfile(obj):
            arquivos.append(obj)
        elif os.path.isdir(obj):
            print(obj)
            print(path)
            path_recursive = os.path.join(path,obj)
            print(path_recursive)
            modulos(path_recursive)

registro_modulos = ['main.py','composite.py','login.py','reload.py','interface.py',
                    'config.py','button_plus.py','button.py','dropdown.py','input.py',
                    'font.py','button_plus.py','card_info.py','menu_logo.py','menu_print.py',
                    'toolbar_menu.y'] # register module

def aux(*args):
    os.system("gnome-terminal -- python3 main.py")

class KvHandler(FileSystemEventHandler):

    def __init__(self, app, **kwargs):
        super(KvHandler, self).__init__(**kwargs)
        self.app = app

    def on_modified(self, event):
        for s in registro_modulos:
            if os.path.basename(event.src_path) == s:
                print('######################################')
                print(arquivos)
                print('Hora: ', datetime.now())
                print('Houve modificação no arquivo: ',s)
                print('pid aplicação: ',os.getppid())
                self.app.get_running_app().stop()
                p = Process(target=aux)
                p.start()
                p.join()
                exit()
                return

def run(app: object):
    PATH = os.getcwd()
    # modulos(os.environ['PWD'])
    o = Observer()
    o.schedule(KvHandler(app), PATH, recursive=True)
    o.start()












