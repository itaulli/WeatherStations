import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://192.168.0.6:5559")
socket.setsockopt_string(zmq.SUBSCRIBE, "")

print("Collecting updates from weather server...")

while True:
    print(socket.recv())