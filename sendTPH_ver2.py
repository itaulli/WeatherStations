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
    zmq_socket.bind("tcp://129.118.107.227:5560")
    zmq_socket.send_json(data)
    print("Sending data")

#function for getparticles() to check for string 'nan'
def notNaN(num):
    return num != 'nan'

#function to get the particle counts
def getparticles():
    """
    returns a list
    [#, diam, #, diam, #, diam]
    # is number of particles with diameter greater than diam per 0.1 liter
    diam is in micrometers
    """
    
    output = [10000]*12
    
    for i in range(14):
        
        data=ser.readline()
        temp = data.split()
        
        if len(temp)==2:
            if temp[0].isdigit() and notNaN(temp[1]):
                count = int(temp[0])
                diam = float(temp[1])
            
                if diam==0.3:
                    output[0] = count
                    output[1] = diam
                if diam==0.5:
                    output[2] = count
                    output[3] = diam
                if diam==1.0:
                    output[4] = count
                    output[5] = diam
                if diam==2.5:
                    output[6] = count
                    output[7] = diam
                if diam==5.0:
                    output[8] = count
                    output[9] = diam
                if diam==10.:
                    output[10] = count
                    output[11] = diam
    
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
ser=serial.Serial('/dev/ttyACM1',115200)

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