import socket

HOST = socket.gethostname()
PORT = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    msg = "Welcome to the server!"
    clientsocket.send(bytes(msg, "utf-8"))
    clientsocket.close()  # Close the conection