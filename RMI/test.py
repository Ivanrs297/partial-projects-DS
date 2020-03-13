from datetime import datetime

import Pyro4

server = Pyro4.Proxy('PYRO:monoide.server@10.0.5.239:4000')

def send():
	now = datetime.now()
	server.change_temp('27', '1', datetime.now())
	print(f'sent at {now:%H:%M:%S} \n')

try:
	print("hola")
	send()
except (KeyboardInterrupt, EOFError):
	print('Goodbye! (:')
