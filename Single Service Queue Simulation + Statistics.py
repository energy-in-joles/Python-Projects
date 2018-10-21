import time
from random import randint
from random import choice
import numpy as np

ar = []
com = [0]
wait = [0] 
com_counter = 0
ar_counter = 0
opening_time = 28800 #time converted to seconds (0800 = 800 x 60 x 60)
closing_time = 75600 

wait_cap = 300 #generate percentage of customers who waited less than this duration (in seconds)

def clock(y):
    n = time.strftime('%H:%M:%S', time.gmtime(y))
    return n

arrival_time = randint(60,600) #gap between arrivals in seconds
arrival_time += opening_time
while arrival_time <= closing_time:
    ar.append(arrival_time)
    arrival_time += randint(60,600)

else:
    completion_time = randint(270,330) #time taken to complete service
    com.append((completion_time + ar[0]))
    for x in range(1,len(ar)):
        complete = randint(270,330)
        if com[x] < ar[x]:
            com.append((completion_time + ar[x]))
            wait.append(0)
        else:
            com.append((completion_time + com[x]))
            wait.append(com[x]-ar[x])
            
    com.remove(0)
    com_ar = ar + com
    while min(com_ar) < closing_time: #closing time used to displace used numbers
        if com_ar.index(min(com_ar)) >= int(len(com_ar)/2):
            com_counter += 1
            print(clock(min(com_ar)) + "  Customer %d has been served" % (com_counter))
            com_ar[com_ar.index(min(com_ar))] = closing_time
		
        else:
            ar_counter += 1
            print(clock(min(com_ar)) + "  Customer %d arrived." % (ar_counter))
            com_ar[com_ar.index(min(com_ar))] = closing_time

    else:
        print("")
        print("Average Waiting Time: " + str(round(np.mean(wait))) + "s")
        counter = 0
        for n in wait:
            if n < wait_cap: 
                counter += 1
        print("Percentage of customers who waited 5 minutes or less: " + str(round((counter/len(wait) * 100), 1)) + "%")
