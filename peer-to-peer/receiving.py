import socket
import struct
import sys
import json
import threading



def get_bytes_db():
    with open('db.json') as json_file:

        # Get json-dictionary from file
        json_data = json.load(json_file)

        # Converte Dictionary to bytes
        json_encode_data = json.dumps(json_data, indent = 2).encode('utf-8')

        return json_encode_data

# Function to listen UDP connections
def listen_udp(multicast_group, udp_port):
    # multicast_group = '224.3.29.71'
    server_address = ('', udp_port) # IP, PORT

    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to the server address
    sock.bind(server_address)

    # Tell the operating system to add the socket to the multicast group
    # on all interfaces.
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Receive/respond loop
    while True:
        print('\nListening UDP...')
        data, address = sock.recvfrom(1024)
        
        print('Received %s bytes from %s' % (len(data), address))
        print(data.decode('utf-8'))

        print('Sending ACK to', address)
        sock.sendto(b'ACK', address)


# Function to listen TCP conections
def listen_tcp(tcp_port):
    server_address = ('', tcp_port) # IP, PORT
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(server_address)
    s.listen(5)

    full_msg = ''
    send_msg = "Welcome"

    while True:
        print('\nListening TCP...')
        clientsocket, address = s.accept()
        print("Connection from ", address, "has been established")
        clientsocket.sendall(get_bytes_db())
        clientsocket.close()  # Close the conection
