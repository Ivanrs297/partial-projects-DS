import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# make sure that the queue exists
channel.queue_declare(queue='slides')

# this function will print on the screen the contents of the message.
def callback(ch, method, properties, body):
    msg = body.decode('utf-8')
    print("Received: ", msg )

# Tell RabbitMQ that this particular callback function should receive messages from our 'slides' queue:
channel.basic_consume(queue='slides', on_message_callback=callback, auto_ack=True)

# enter a never-ending loop that waits for data and runs callbacks whenever necessary.
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming() 