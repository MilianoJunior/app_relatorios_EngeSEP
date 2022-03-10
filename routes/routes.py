
def define_manager(objeto):
    global screen_manager
    screen_manager = objeto

class Routes:
    '''
    description: gerenciador de rotas e autenticação
    args: None
    return None
    '''
    def redirect(data: dict):
        print('Name screen: ',data)
        print('screen atual: ',screen_manager.current)
        screen_manager.current = data.get('value')

    def get(data: dict):
        print('get: ',data)
