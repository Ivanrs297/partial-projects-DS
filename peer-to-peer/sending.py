import socket
import struct
import sys
import json

def get_peers(multicast_group_ip, udp_port, alias):

    peers_table = []  # List of reachable peers

    multicast_group = (multicast_group_ip, udp_port)

    # Create the datagram socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout so the socket does not block indefinitely when trying
    # to receive data.
    sock.settimeout(0.2)

    # Set the time-to-live for messages to 1 so they do not go past the
    # local network segment.
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    print("In geetting peers!")
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
                data, peer_to_connect = sock.recvfrom(10)

                # Add the peer in the table
                peers_table.append(peer_to_connect)

            except socket.timeout:
                print('Timed out, no more responses')
                break
            else:
                print('Received "%s" from %s' % (data.decode('utf-8'), peer_to_connect))

    finally:
        print('Closing socket')
        sock.close()
        return peers_table

def get_db_from_peer(peer):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(peer) 
    full_msg = ''
    while True:
        msg = s.recv(8)  # size of buffer at time, bit stream
        if len(msg) <= 0:
            break
        full_msg += msg.decode("utf-8")
    return full_msg


if __name__ == '__main__':
    get_peers('224.3.29.71', 10000, 'Ivan')