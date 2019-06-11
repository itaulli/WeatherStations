import sys
import zmq

"""
START PUBLISHERS BEFORE STARTING SUBSCRIBER
"""

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

port1 = "5556"
if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket1 = context.socket(zmq.SUB)
socket2 = context.socket(zmq.SUB)

print("Collecting updates from weather server...")

socket1.connect ("tcp://129.118.107.231:{}".format(port))
socket2.connect ("tcp://192.58.125.12:{}".format(port1))

print("Connected successfully")

while True:
    string1 = socket1.recv()
    string2 = socket2.recv()
    topic1, messagedata1 = string1.split()
    topic2, messagedata2 = string2.split()
    print(topic, messagedata)
