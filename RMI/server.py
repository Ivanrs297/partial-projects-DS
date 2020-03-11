from datetime import datetime
import Pyro4

@Pyro4.expose
class Chat(object):
    def send_message(self, text):
        now = datetime.now()
        print(f'{text} - received at {now:%H:%M:%S} \n')

def start_server():
    daemon = Pyro4.Daemon()  # Make a Pyro daemon
    ns = Pyro4.locateNS()  # First run 'python -m Pyro4.naming' on other terminal
    uri = daemon.register(Chat)  # register the object as a Pyro object, to access remoteley
    ns.register('rmi.server', str(uri))
    print(f'Listen on {uri}')
    daemon.requestLoop()


if __name__ == '__main__':
    try:
        start_server()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit