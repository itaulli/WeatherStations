import serial
import time

ser=serial.Serial('/dev/ttyACM0',115200)

count=0
while True:
	data=ser.readline()
	print data[:-1]
	count = count + 1
	if count >= 9 : 
		time.sleep(5)
		count = 0 
