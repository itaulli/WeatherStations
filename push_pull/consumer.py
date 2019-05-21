import time
import zmq
import random

def consumer():
    consumer_id = "apple"
    print("I am consumer {}".format(consumer_id))
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://129.118.107.227:5557")

    work = consumer_receiver.recv_json()
    data = work['num']
    print(data)

consumer()