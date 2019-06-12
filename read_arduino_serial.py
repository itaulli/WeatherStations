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
    
    output = ['fail']*12
    diamlist = ['0.30','0.50','1.00','2.50','5.00','10.00']
    max_tries = 10
    
    #function will retry if filling the list fails
    for attempt in range(max_tries):
        
        #this for loop fills the list
        for i in range(14):
        
            data=ser.readline()
            temp = data.split()
        
            if len(temp)==2:
                if temp[0].isdigit() and (temp[1] in diamlist):
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
        
        if 'fail' in output:
            print('failure')
            time.sleep(1)
        else:
            print('success on attempt {}'.format(attempt))
            return output
            break

while True:
    out = getparticles()
    print(out)
    time.sleep(5)
            