import socket 
import time
import datetime
import pymongo
from pymongo import MongoClient
import cloudinary
import cloudinary.uploader
import os
import webbrowser


# Globals:
in_connection = False

# DB Config:
connection_params = {
    'user': 'cinv',
    'password': "cinv123",
    'host': 'ds037175.mlab.com',
    'port': 37175,
    'namespace': 'cinvestav',
}

connection = MongoClient(
    'mongodb://{user}:{password}@{host}:'
    '{port}/{namespace}?retryWrites=false'.format(**connection_params)
)

db = connection.cinvestav
db = db["schedule"]

cloudinary.config(
  cloud_name = 'dv0bco9rw',  
  api_key = '621813665726586',  
  api_secret = '5zNWkLE3ii-a1MrmC7jziLv6WOE'  
)

def upload_img_to_cloudinary(img_name):
	cloudinary.uploader.upload(img_name, public_id = img_name)

def get_img_from_cloudinary(img_name):
	return cloudinary.utils.cloudinary_url(img_name)


def get_schedule():
	schedules = db.find()
	return schedules

def insert_data_to_db():
	db.insert_many([
		{"start": "8.50", "finish": "11", "day": "Monday", "class": "Distributed Systems", "professor": "Dr. Felix Corchado"},
		{"start": "8.50", "finish": "11", "day": "Wednesday", "class": "Distributed Systems", "professor": "Dr. Felix Corchado"},
		{"start": "8.50", "finish": "11", "day": "Friday", "class": "Distributed Systems", "professor": "Dr. Felix Corchado"},
	])

# Function to create the client message
def create_client_msg(HOST, PORT, msg):	
	print(f"Connecting to server: {HOST} on port: {PORT}")
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
		try:
			sck.connect((HOST, PORT))
		except Exception as e:
			raise SystemExit(f"We have failed to connect to host: {HOST} on port: {PORT}, because: {e}")

		sck.sendall(msg.encode('utf-8'))
		
		data = sck.recv(1024)
		if data:
			print(f"RES: {data.decode()}")

# Function send command of open PDF
def open_pdf(pdf_name):
	return f"open pdf {pdf_name}"

def is_time_of_assignement():
	now = datetime.datetime.now()
	assignatures_schedule = get_schedule()
	for a in assignatures_schedule:
		if now.today().strftime("%A") == a["day"] and now.hour >= float(a["start"]) and now.hour <= float(a["finish"]):
		# if now.today().strftime("%A") == a["day"]:
			print(f"Assignature: {a['class']}" )
			return True
	return False

while False:
	time.sleep(3)

	# If its time of a assignature, then show de PDF presentation
	if not in_connection and is_time_of_assignement() :
		in_connection = True
		create_client_msg(socket.gethostname(), 4000, open_pdf("present"))




		
# upload_img_to_cloudinary("anime.jpeg")
img = get_img_from_cloudinary("anime.jpeg")
img = f'{img[0]}.jpeg'
webbrowser.open(img)  # Go to example.com





