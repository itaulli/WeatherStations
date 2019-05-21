import time
import zmq
from Adafruit_BME280 import *

#setup the sensor
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

#identify the weather station
weather_id = "first"

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
    
    #get the weather info
	degrees = sensor.read_temperature()
	pascals = sensor.read_pressure()
	humidity = sensor.read_humidity()
    
    #save to a dictionary
    data = {'id':weather_id, 'timestamp':localtime, 'temp':degrees, 'pressure':pascals, 'humidity':humidity}
    
    print(data)
    
    #wait for 1 minute
    time.sleep(60)