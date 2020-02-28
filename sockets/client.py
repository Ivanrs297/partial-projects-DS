# Client for PC


import socket

# HOST = socket.gethostname()
# HOST = "10.0.5.239"
HOST = "192.168.0.134"
PORT = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) 

full_msg = ''

while True:
    msg = s.recv(8)  # size of buffer at time, bit stream
    if len(msg) <= 0:
        break

    full_msg += msg.decode("utf-8")


print(full_msg)