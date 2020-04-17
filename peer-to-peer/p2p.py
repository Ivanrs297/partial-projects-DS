from sending import *
from receiving import *
from tinydb import TinyDB, Query
import threading
import time

def check_db(string_db, hash_to_compare):

	# Convert the response string in JSON
	json_db = json.loads(string_db)
	data_json = json.dumps(json_db, sort_keys=True, indent=2)

	# Get Hash from Received DB
	hash = hashlib.md5(data_json.encode("utf-8")).hexdigest()
	# hash = '68b67e4f9944a00b3a6c38b03c110206' # Wrong hash
	
	# Check if the DB hashes are equal
	if (hash == hash_to_compare):
		print("Success! The DB Hashes are equal")
		return json_db, True
	else:
		print("Error: The Hashes are not equal")
		return None, False

def updates_peers_db(peers_table, tcp_port):
	for peer in peers_table:
		update_process = threading.Thread(target=update_db_to_peer, args=((peer[0], tcp_port),))
		update_process.start()

if __name__ == '__main__':

	db = TinyDB('db.json')

	MULTICAST_GROUP_IP = '224.3.29.71'
	UDP_PORT = 10000
	TCP_PORT = 5000
	ALIAS = 'Laptop Ivan' # Rasp1, Laptop 2, etc

	# Get IP of Host
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	print("Host IP: ", s.getsockname()[0])
	HOSTNAME = s.getsockname()[0]
	s.close()

	# Listenings Threads
	UDP_LISTENER = threading.Thread(target=listen_udp, args=(MULTICAST_GROUP_IP, UDP_PORT, HOSTNAME,))
	TCP_LISTENER = threading.Thread(target=listen_tcp, args=(TCP_PORT,))
	UDP_LISTENER.start()
	TCP_LISTENER.start()

	time.sleep(3)

	# Get Peers by UDP
	peers_table, hash_table = get_peers(MULTICAST_GROUP_IP, UDP_PORT, ALIAS, HOSTNAME)
	print("Peers Table: ", peers_table)
	print("Hash Table: ", hash_table)

	if (len(peers_table) > 0):
		# select a peer
		peer_to_connect = peers_table[0]

		# select the hash DB of peer
		hash_to_compare = hash_table[0]

		# # Get DB from the peer by TCP
		string_db = get_db_from_peer((peer_to_connect[0], TCP_PORT))
		db_processed, is_correct = check_db(string_db, hash_to_compare)

		if (is_correct):
			# Write json in local DB
			with open('db.json', 'w') as outfile:
				json.dump(db_processed, outfile)
			print("DB Updated!")
		
		# updates_peers_db(peers_table, TCP_PORT)
		# update_db_to_peer((peer_to_connect[0], TCP_PORT))

