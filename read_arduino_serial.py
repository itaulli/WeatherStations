import serial
import time

ser=serial.Serial('/dev/ttyACM1',115200)

def notNaN(num):
    return num != 'nan'

def getparticles():
    """
    returns a list
    [#, diam, #, diam, #, diam]
    # is number of particles with diameter greater than diam per 0.1 liter
    diam is in micrometers
    """
    
    output = [10000]*12
    diamlist = ['0.30','0.50','1.00','2.50','5.00','10.00']
    
    for i in range(14):
        
        data=ser.readline()
        temp = data.split()
        print("i is {}".format(i))
        print("raw temp is")
        print(temp)
        
        if len(temp)==2:
            if temp[0].isdigit() and (temp[1] in diamlist):
                print("temp has passed")
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
                if diam==10.0:
                    output[10] = count
                    output[11] = diam
    
    return output

while True:
    out = getparticles()
    print(out)
    time.sleep(5)
            