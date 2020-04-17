import socket
import struct
import sys
import json
import hashlib
from p2p import check_db


# Return JSON DB encoded in bytes utf-8
def get_bytes_db():
    with open('db.json') as json_file:

        # Get json-dictionary from file
        json_data = json.load(json_file)
        

        # Converte Dictionary to bytes
        json_encode_data = json.dumps(json_data, indent = 2).encode('utf-8')

        return json_encode_data

# Return the hash of JSON DB
def get_hash_from_db():
    with open('db.json') as json_file:
        data = json.load(json_file)
        data_json = json.dumps(data, sort_keys=True, indent=2)
        hash = hashlib.md5(data_json.encode("utf-8")).hexdigest()
        return hash

# Function to listen UDP connections
def listen_udp(multicast_group, udp_port, hostname):
    multicast_group = '224.3.29.71'
    server_address = ('', 10000) # IP, PORT

    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse de PORT


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
        data, peer_to_connect = sock.recvfrom(1024)

        if ( peer_to_connect[0] != hostname ):
            print('Received %s bytes from %s' % (len(data), peer_to_connect))
            print(data.decode('utf-8'))

            print('Sending HASH to', peer_to_connect)
            sock.sendto(bytes(get_hash_from_db(), 'utf-8'), peer_to_connect)

# Function to listen TCP conections
def listen_tcp(tcp_port):
    server_address = ('', tcp_port) # IP, PORT
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(server_address)
    s.listen(20)

    while True:
        print('\nListening TCP...')
        peer_socket, address = s.accept()
        print("Connection from ", address, "has been established")

        msg = peer_socket.recv(1024)  # size of buffer at time, bit stream
        msg = msg.decode('utf-8')

        # Return DB
        if (msg == "GETDB"):
            peer_socket.sendall(get_bytes_db())
        else:
            # Update the local DB

            # Get the hash from peer
            hash_from_peer = msg;

            # Get the DB from peer
            incoming_db = peer_socket.recv(1024)
            
            db_processed, is_correct = check_db(incoming_db.decode('utf-8'), hash_from_peer)
            if (is_correct):
                # Write json in local DB
                with open('db.json', 'w') as outfile:
                    json.dump(db_processed, outfile)
                print("DB Updated!")

        peer_socket.close()  # Close the conection


if __name__ == '__main__':
    listen_udp('224.3.29.71', 10000)