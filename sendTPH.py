import time
import zmq
from Adafruit_BME280 import *
"""
The reciever must already be running before the sender is started
"""

#setup the sensor
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

#identify the weather station
weather_id = "first"

#the function that sends data
#must already have created the data dictionary before calling producer()
def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://129.118.107.227:5556")
    zmq_socket.send_json(data)
    print("Sending data at time {}:{}".format(timelist[4],timelist[5]))

#read the TPH data and save it in a time-stamped dictionary
while True:
    #get the time as a time-tupple
    #localtime[0] is year
    #localtime[1] is month (1-12)
    #localtime[2] is day (1-31)
    #localtime[3] is hour (0-23)
    #localtime[4] is minute (0-59)
    #localtime[5] is second (0-59)
    localtime = time.localtime(time.time())
    #convert to a list so JSON can handle it
    timelist = [localtime[0],localtime[1],localtime[2],localtime[3],localtime[4],localtime[5]]
    
    #get the weather info
    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    humidity = sensor.read_humidity()
    
    #save to a dictionary
    data = {'idnum':weather_id, 'timestamp':timelist, 'temp':degrees, 'pressure':pascals, 'humidity':humidity}
    
    #send the data
    producer()
    
    #wait for 1 minute
    time.sleep(60)