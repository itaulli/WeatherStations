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
    zmq_socket.bind("tcp://129.118.107.227:5556")
    zmq_socket.send_json(data)
    print("Sending data")

#function to get the particle counts
def getparticles():
    """
    returns a list
    [#,#,#,#,#,#]
    # is number of particles with diameter greater than diam per 0.1 liter
    diam is in micrometers
    """
    
    output = ['fail']*6
    diamlist = ['0.30','0.50','1.00','2.50','5.00','10.00']
    max_tries = 10
    
    #function will retry if filling the list fails
    for attempt in range(max_tries):
        
        #this loop fills the list
        for i in range(14):
        
            data=ser.readline()
            temp = data.split()
        
            if len(temp)==2:
                if temp[0].isdigit() and (temp[1] in diamlist):
                    count = int(temp[0])
            
                    if temp[1]=='0.30':
                        output[0] = count
                    if temp[1]=='0.50':
                        output[1] = count
                    if temp[1]=='1.00':
                        output[2] = count
                    if temp[1]=='2.50':
                        output[3] = count
                    if temp[1]=='5.00':
                        output[4] = count
                    if temp[1]=='10.00':
                        output[5] = count
        
        #check for success and retry
        if 'fail' in output:
            time.sleep(1)
        else:
            return output
            break
        
    print('catastophic failure, seek shelter')

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