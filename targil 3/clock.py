#I want to make a digital clock that every time it is updated it stays in the same terminal lane and does not go down

import datetime
import time
def clock():
    while True: 
        print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")  
        time.sleep(1)

clock()