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

    try:

        message = f"Hi, i´m {alias}"
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
                print('Received "%s" from %s' % (data.decode('utf-8'), peer))

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

# Run program
if __name__ == '__main__':

    peers_table = get_peers()
    print("Peers: ", peers_table)
    
    # select a peer
    peer_to_connect = peers_table.pop()

    # Get DB from the peer
    string_db = get_db_from_peer((peer_to_connect[0], 5000))

    # Convert the response string in JSON
    json_db = json.loads(string_db)

    # Write json in local DB
    with open('db2.json', 'w') as outfile:
        json.dump(json_db, outfile)

    # Update DB
