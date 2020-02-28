# Client for Raspberry

import socket
import datetime

in_connection = False

def open_pdf(pdf_name):
    return f"open {pdf_name}.pdf"

def establish_connection():
    HOST = socket.gethostname()
    # HOST = "10.0.5.239"
    # HOST = "192.168.0.134"
    PORT = 4000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT)) 

    receive_msg = ''
    send_msg = open_pdf("present")

    s.sendall(bytes(send_msg, "utf-8"))
    receive_msg = s.recv(1024)
    s.close()

    receive_msg.decode("utf-8")
    print(receive_msg)
    in_connection = False


currentDT = datetime.datetime.now()

while True:
    if currentDT.hour == 20 and not in_connection:
        in_connection = True
        establish_connection()