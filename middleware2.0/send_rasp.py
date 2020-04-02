# send a single message to the queue

import pika

# establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a hello queue to which the message will be delivered:
channel.queue_declare(queue='slides')

# Message to send
msg = '1'

channel.basic_publish(exchange = '', routing_key = 'slides', body = msg)

print(f" Raspberry sent message: {msg}")
connection.close()
