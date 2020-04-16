from receiving import *
from sending import *
from tinydb import TinyDB, Query
import threading
import time



if __name__ == '__main__':

	db = TinyDB('db.json')

	MULTICAST_GROUP_IP = '224.3.29.71'
	UDP_PORT = 10000
	TCP_PORT = 5000
	ALIAS = 'Laptop Ivan' # Rasp1, Laptop 2, etc

	# Listener Threads
	UDP_LISTENER = threading.Thread(target=listen_udp, args=(MULTICAST_GROUP_IP, UDP_PORT,))
	TCP_LISTENER = threading.Thread(target=listen_tcp, args=(TCP_PORT,))
	UDP_LISTENER.start()
	TCP_LISTENER.start()

	time.sleep(3)

	# Get Peers by UDP
	peers_table = get_peers(MULTICAST_GROUP_IP, UDP_PORT, ALIAS)
	print("Peers: ", peers_table)

	if (len(peers_table) > 0):
		# select a peer
		peer_to_connect = peers_table.pop()

		# Get DB from the peer by TCP
		string_db = get_db_from_peer((peer_to_connect[0], TCP_PORT))

		# Convert the response string in JSON
		json_db = json.loads(string_db)

		# Write json in local DB
		with open('db.json', 'w') as outfile:
			json.dump(json_db, outfile)

