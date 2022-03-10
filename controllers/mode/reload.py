from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
from multiprocessing import Process
import os

registro_modulos = ['main.py','composite.py','login.py','reload.py','interface.py',
                    'config.py','button_plus.py','button.py','dropdown.py','input.py',
                    'font.py','button_plus.py','card_info.py','menu_logo.py','menu_print.py',
                    'toolbar_menu.py','routes.py','create_user.py','config.py','themas_color.py',
                    'RootException.py','multi_button.py'] # register module

def aux(*args):
    print('abrindo novo app')
    module = 'main.py'
    commands = {'nt': f"start python {module}",
                'posix': f"gnome-terminal -- python3 {module}"}
    os.system(commands[os.name])

class KvHandler(FileSystemEventHandler):

    def __init__(self, app, **kwargs):
        super(KvHandler, self).__init__(**kwargs)
        self.app = app

    def on_modified(self, event):
        for s in registro_modulos:
            if os.path.basename(event.src_path) == s:
                print('##########################################')
                print('Hora: ', datetime.now())
                print('Houve modificação no arquivo: ',s)
                print('pid aplicação: ',os.getppid())
                self.app.get_running_app().stop()
                os.system('exit()')
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












