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
socket = context.socket(zmq.SUB)

print "Collecting updates from weather server..."

socket.connect ("tcp://129.118.107.231:{}".format(port))
socket.connect ("tcp://192.58.125.12:{}".format(port1))
    

# Process 5 updates
while True:
    string = socket.recv()
    topic, messagedata = string.split()
    print(topic, messagedata)
