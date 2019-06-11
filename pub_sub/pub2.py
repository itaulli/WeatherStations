import zmq
import random
import sys
import time

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://192.58.125.12:{}".format(port))

while True:
    topic = 202
    messagedata = random.randrange(1,215) - 80
    print("{} {}".format(topic, messagedata))
    socket.send("{} {}".format(topic, messagedata))
    time.sleep(10)