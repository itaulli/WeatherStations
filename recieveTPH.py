import time
import zmq
"""
The reciever must already be running before the sender is started
"""

#the function that recieves data
#accepts ip and port number as arguments
#saves incoming dictionary as "data"
def consumer(ip, port):
    print("reciever is operational")
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://{}:{}".format(ip,port))

    data = consumer_receiver.recv_json()
    print("Recieved data from weather station {} at time {}:{}".format(data[idnum],data[timestamp][4],data[timestamp][5]))
    
consumer(129.118.107.227,5556)