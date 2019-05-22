import zmq
import random
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://192.168.0.6:5559")

while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,215) - 80
    print("{:d} {:d}".format(topic, messagedata))
    socket.send_string("{:d} {:d}".format(topic, messagedata))
    time.sleep(1)