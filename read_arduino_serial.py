import serial
import time

ser=serial.Serial('/dev/ttyACM0',115200)

"""
count=0
while True:
	data=ser.readline()
	print data[:-1]
	count = count + 1
	if count >= 9 : 
		time.sleep(5)
		count = 0 
"""

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
        
        if len(temp)==9:
            count = int(temp[0])
            diam = float(temp[3])
            
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

while True:
    out = getparticles()
    print(out)
    time.sleep(10)
            