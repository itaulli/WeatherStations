import time
import zmq
from Adafruit_BME280 import *
"""
The reciever must already be running before the sender is started
"""

#the function that sends data
def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://129.118.107.227:5559")
    zmq_socket.send_json(data)
    print("Sending data for time {}:{}:{}".format(timelist[3],timelist[4],timelist[5]))

#######################################
#Config
#######################################
#identify the weather station
weather_id = "apple"

#how long to collect data (hours)
runtime = 12
#######################################

#setup the sensor
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

#calculate the time to end data collection
end_time = time.time() + 3600*runtime

#make reports for the required time
while time.time() < end_time:
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
    
    #synchornize the reports with the wall clock
    if timelist[5]==0:
    
        #get the weather info
        degrees = sensor.read_temperature()
        pascals = sensor.read_pressure()
        humidity = sensor.read_humidity()
    
        #save to a dictionary
        data = {'idnum':weather_id, 'timestamp':timelist, 'temp':degrees, 'pressure':pascals, 'humidity':humidity}
    
        #send the data
        producer()
    
    #wait for 1 second before checking time again
    time.sleep(1)