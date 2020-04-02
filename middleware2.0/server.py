# START with rabbitmq-server

# Example of slide object
# slide = {
# 	"id": 1,
# 	"url": "https://docs.google.com/presentation/d/1OmEUbalmSrcmRlBVO3oPQKWJRsTYPFMx/edit#slide=id.p1"
# }

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
from tinydb import TinyDB, Query
import pika

# CRUD for Slides:
# Create
def post(slide):
	Slide_query = Query()
	if db.search(Slide_query.id == slide['id']):
		return "Error, slide ID already in DB"
	else:
		db.insert(slide)
		return "slide Added"

# Read
def get(id = None):
	if id:
		Slide_query = Query()
		data = db.search(Slide_query.id == id)
		return str(data)
	else:
		return str(db.all())

# Update
def patch(id, key, value):
	Slide_query = Query()
	if db.update({key: value}, Slide_query.id == id):
		return "Modified"
	else:
		return "Error, slide not found on DB"

# Delete
def delete(id):
	Slide_query = Query()
	if db.remove(Slide_query.id == id):
		return "Deleted"
	else:
		return "Error, slide not found on DB"

# Delete DB ***WARNING***
def drop():
	db.purge()
	return "DB deleted"

def open_and_listen_url(url, id):
	try:
		# Get the driver to manage Chrome
		driver = webdriver.Chrome(ChromeDriverManager().install())
		driver.get(url)

		while True:
			# Get the current url in the browser
			current_url = driver.current_url

			# If the current url is diferent from the last one
			if current_url != url:
				# Update de url in database
				patch(id, "url", current_url)
				url = current_url
			time.sleep(5)

	except KeyboardInterrupt:
		print("Error...")

	driver.close()

# this function will catch the messages from middleware
def callback(ch, method, properties, body):
	msg_id = body.decode('utf-8')
	print("Received Slide ID: ", msg_id )

	# Get the last slide object by ID
	slide = eval(get(int(msg_id)))
	print("RES slide: ", slide)
	slide_id = slide[0]["id"]
	slide_url = slide[0]["url"]

	open_and_listen_url(slide_url, slide_id)

# Run program
if __name__ == '__main__':

	# Open connection with DB
	db = TinyDB('db.json')

	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()

	# make sure that the queue exists
	channel.queue_declare(queue='slides')

	# Tell RabbitMQ that this particular callback function should receive messages from our 'slides' queue:
	channel.basic_consume(queue='slides', on_message_callback=callback, auto_ack=True)

	# enter a never-ending loop that waits for data and runs callbacks whenever necessary.
	print('Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()


	









	

