import socket
import threading
import time
from threading import Thread
import os
import platform
import cloudinary
import cloudinary.uploader


# Globals:
HOST = socket.gethostname()  # localhost
PORT = 4000

def open_pdf(pdf_name):
	if platform.system() == "Darwin":
		cmd_string = f'open -a "Adobe Acrobat Reader DC" ../{pdf_name}.pdf'
		os.system(cmd_string)
	elif platform.system() == "Windows":
		cmd_string = f'AcroRd32.exe /A "page=5=OpenActions" ../{pdf_name}.pdf'
		os.system(cmd_string)

# Function to switch the command in msg
def switch_cmd(cmd):
	cmd = cmd.split(' ')
	if cmd[0] == 'open':
		open_pdf(cmd[2])

# Function that triggers in case new client connection
def on_new_client_thread(client, connection):
	ip = connection[0]
	port = connection[1]
	print(f"New connection from IP: {ip}, and port: {port}!")
	msg = client.recv(1024)
	print(f"REQ: {msg.decode()}")
	switch_cmd(msg.decode())
	client.sendall("Ok".encode('utf-8'))
	client.close()

# Function to create the socket client
def create_client_socket(HOST, PORT):
	print(f"Connecting to server: {HOST} on port: {PORT}")
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
		try:
			sck.connect((HOST, PORT))
		except Exception as e:
			raise SystemExit(f"We have failed to connect to host: {HOST} on port: {PORT}, because: {e}")

		msg = "New Client"
		sck.sendall(msg.encode('utf-8'))

# Function to create the socket server
def create_server_socket(host, port):
	
	print(f"Running the server on: {HOST} and port: {PORT}\n\n")

	sck = socket.socket()
	sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse de PORT

	try: 
		sck.bind((host, port))
		sck.listen(5)
	except Exception as e:
		raise SystemExit(f"We could not bind the server on host: {host} to port: {port}, because: {e}")

	while True:
		try: 
			client, ip = sck.accept()
			threading._start_new_thread(on_new_client_thread,(client, ip))

		except KeyboardInterrupt:
			print(f"Shutting down the server...")
			exit()
		except Exception as e:
			print(f"Error: {e}")
	sck.close()


threading._start_new_thread(create_server_socket(HOST, PORT))


