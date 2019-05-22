import time

#calculate the time to end data collection
end_time = time.time() + 60*5

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
    
    #print the time every minute
    if timelist[5]==0:
        print("time is {}:{}:{}".format(timelist[3],timelist[4],timelist[5]))
        
    time.sleep(1)