#!/usr/bin/env python 3
import xmlrpc.client
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time 
import datetime
GPIO.setwarnings(False)
reader=SimpleMFRC522()

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(13, GPIO.OUT)
#GPIO.output(13,GPIO.LOW)
#para conectarse cliente
PROXY_HOST="http://10.0.5.234"
PROXY_PORT='4000'
PROXY_ENDPOINT=f'{PROXY_HOST}:{PROXY_PORT}'
proxy = xmlrpc.client.ServerProxy(PROXY_ENDPOINT)
if __name__=='__main__':
	
	try:
		
		id, text=reader.read()
		now=datetime.datetime.now()
		result=text.split(",")
		course={
		  "id":3,
		  "start":now.strftime("%X"),
		  "finish":result[0],
		  "day":now.strftime("%A"),
		  "class":result[1],
		  "professor":result[2]
		}
		
		
		print("ID:        ",id)
		print("id:        ",3)
		print("start:     ",now.strftime("%X"))
		print("finish:    ",result[0])
		print("day:       ",now.strftime("%A"))
		print("class:     ",result[1])
		print("professor: ",result[2])
		
		GPIO.setup(11, GPIO.OUT)
		GPIO.output(11,GPIO.HIGH)
		time.sleep(.5)
		GPIO.output(11,GPIO.LOW)
	
		res=proxy.post(course)
		#res=proxy.drop()
		print("RES: ",res)
    
 

	except xmlrpc.client.Fault as err:
		print("Error code: %d"%err.faultCode)
		print("Error string: %s"%err.faultString)

		 

    
