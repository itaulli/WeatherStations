import time

while True:
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    time.sleep(10)