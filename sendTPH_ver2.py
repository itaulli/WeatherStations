import time
import zmq
from Adafruit_BME280 import *
import serial

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

#function to get the particle counts
def getparticles():
    """
    returns a list
    [#, diam, #, diam, #, diam]
    # is number of particles with diameter greater than diam per 0.1 liter
    diam is in micrometers
    """
    
    output = [None]*6
    
    for i in range(14):
        
        data=ser.readline()
        temp = data.split()
        
        if len(temp)==9:
            count = int(temp[0])
            diam = float(temp[3])
            
            if diam==0.3:
                output[0] = count
            if diam==0.5:
                output[1] = count
            if diam==1.0:
                output[2] = count
            if diam==2.5:
                output[3] = count
            if diam==5.0:
                output[4] = count
            if diam==10.:
                output[5] = count
    
    return output

#######################################
#Config
#######################################
#identify the weather station (integer)
weather_id = 106
#######################################

#setup the TPH sensor
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

#setup the PC sensor
ser=serial.Serial('/dev/ttyACM0',115200)

#make reports
while True:
    #get the time as a time-tupple
    localtime = time.localtime(time.time())
    
    #synchornize the reports with the wall clock
    if localtime[5]==0:
    
        #get the weather info
        degrees = sensor.read_temperature()
        pascals = sensor.read_pressure()
        humidity = sensor.read_humidity()
        particles = getparticles()
    
        #save to a dictionary
        data = {'idnum':weather_id, 'temp':degrees, 'pressure':pascals, 'humidity':humidity, 'part':particles}
    
        #send the data
        producer()
    
    #wait for 1 second before checking time again
    time.sleep(1)