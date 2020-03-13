from datetime import datetime
import serial, time
import Pyro4

arduino = serial.Serial('/dev/ttyACM0', 9600)


server = Pyro4.Proxy('PYRO:monoide.server@10.0.5.239:4000')

def send():
    now = datetime.now()
    rawString = arduino.readline()  # Get String from Serial Port
    classroom_id = 1
    server.change_temp(rawString.decode('utf-8'), classroom_id, datetime.now())

try:
    send()
except (KeyboardInterrupt, EOFError):
    print('Closing! (:')
