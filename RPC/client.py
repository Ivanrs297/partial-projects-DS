
import xmlrpc.client

PROXY_HOST = 'http://localhost'
PROXY_PORT = '4000'
PROXY_ENDPOINT = f'{PROXY_HOST}:{PROXY_PORT}'

proxy = xmlrpc.client.ServerProxy(PROXY_ENDPOINT)

if __name__ == '__main__':
	try:
		# print(proxy.open_pdf(r'present', 4))  # Raw string
		
		''' Add new course '''
		course = {
			"id": 1,
			"start": "8.50",
			"finish": "11",
			"day": "Monday",
			"class": "Distributed Systems",
			"professor": "Dr. Felix Corchado"
			}
		res = proxy.post(course)


		''' Get all courses '''
		# res = eval(proxy.get())  # eval to convert to obj

		''' Get course by ID '''
		# res = eval(proxy.get(1))  # eval to convert to obj

		''' Update course by ID '''
		# res = proxy.patch(1, 'day', 'Lunes')
		
		''' Deleted course by ID '''
		# res = proxy.delete(2)

		''' Deleted DB - WARNING'''
		# res = proxy.drop()
		
		print("RES: ", res)

	except xmlrpc.client.Fault as err:
		print("Error code: %d" % err.faultCode)
		print("Error string: %s" % err.faultString)

