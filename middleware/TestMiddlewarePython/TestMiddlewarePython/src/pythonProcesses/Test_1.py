import IDHelper
from Process import Process

class Test_1(Process):

    nodeID = ["TestArea",1]

    def __init__(self):
        print("hola")

    def init(self):
        print("init")

    def receive(self, id, message):
        print(message)
        print("asd")
        self.send(IDHelper.getID("TestArea"),bytearray(b'Print it'))