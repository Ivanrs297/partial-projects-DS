import socket
import struct
import sys
import json
from receiving import *

def get_peers(multicast_group_ip, udp_port, alias, hostname):

    peers_table = []  # List of reachable peers
    hash_table = []  # List of hashes of DB

    multicast_group = (multicast_group_ip, udp_port)

    # Create the datagram socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse de PORT


    # Set a timeout so the socket does not block indefinitely when trying
    # to receive data.
    sock.settimeout(0.2)

    # Set the time-to-live for messages to 1 so they do not go past the
    # local network segment.
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    try:

        # message = "Hi, i´m ", alias
        message = "Hi, I`m: " + alias
        message = message.encode()

        # Send data to the multicast group
        print('Sending... "%s"' % message.decode('utf-8'))
        sent = sock.sendto(message, multicast_group)

        # Look for responses from all recipients
        while True:
            print('Waiting to receive ACK...')
            try:
                hash_data, peer_to_connect = sock.recvfrom(32) # size of buffer in characters

                if ( peer_to_connect[0] != hostname ):
                    # Add the peer in the table
                    peers_table.append(peer_to_connect)
                    hash_table.append(hash_data.decode('utf-8'))

            except socket.timeout:
                print('Timed out, no more responses')
                break
            else:
                if ( peer_to_connect[0] != hostname ):
                    print('Received "%s" from %s' % (hash_data.decode('utf-8'), peer_to_connect))

    finally:
        print('Closing socket')
        sock.close()
        return peers_table, hash_table

# Establish TCP Conection 
def get_db_from_peer(peer):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse de PORT

    s.connect(peer) 
    sending_msg = "GETDB"
    s.sendall(sending_msg.encode('utf-8'))
    incoming_db = s.recv(1024)  # receive message
    return incoming_db.decode('utf-8')

def update_db_to_peer(peer):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse de PORT

    s.connect(peer) 
    hash_db = get_hash_from_db()
    s.sendall(hash_db.encode('utf-8'))
    s.sendall(get_bytes_db())

    incoming_msg = s.recv(1024)  # receive message
    return incoming_msg.decode('utf-8')


if __name__ == '__main__':
    get_peers('224.3.29.71', 10000, 'Ivan')