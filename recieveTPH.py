import time
import zmq
import pickle
"""
The reciever must already be running before the sender is started
"""

#the function that recieves data
#saves incoming dictionary as "data"
def consumer():
    print("Reciever is operational")
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://129.118.107.227:5558")

    data = consumer_receiver.recv_json()
    print("Recieved data from weather station {} at time {}:{}".format(data['idnum'],data['timestamp'][4],data['timestamp'][5]))
    return data
    
#initialize a list of dictonaries
datalist = []

#set the number of data collections before saving
#run the collections
for i in range(2):
    data = consumer()
    datalist.append(data)
    
#pickle the data list
with open('weather.pkl', 'wb') as savefile:
    pickle.dump(datalist, savefile)