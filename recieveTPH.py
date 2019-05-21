import time
import zmq
"""
The reciever must already be running before the sender is started
"""

#the function that recieves data
#saves incoming dictionary as "data"
def consumer():
    print("reciever is operational")
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://129.118.107.227:5556")

    data = consumer_receiver.recv_json()
    print("Recieved data from weather station {} at time {}:{}".format(data['idnum'],data['timestamp'][4],data['timestamp'][5]))
    
consumer()