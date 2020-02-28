# Server for PC

import socket
import os
import platform


def open_pdf():
    if platform.system() == "Darwin":
        os.system('open -a "Adobe Acrobat Reader DC" ../present.pdf')
    elif platform.system() == "Windows":
        os.system('AcroRd32.exe /A "page=5=OpenActions" ../present.pdf')
        

# HOST = socket.gethostname()
HOST = "10.0.5.234"
PORT = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

full_msg = ''
send_msg = "Welcome"

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")

    clientsocket.sendall(bytes(send_msg, "utf-8"))
    msg = clientsocket.recv(1024)
    full_msg += msg.decode("utf-8")
    clientsocket.close()  # Close the conection

    if full_msg == "open present.pdf":
        open_pdf()

    print(full_msg)
    full_msg = ""

