'''import time
from threading import Thread  # Correct class name

def calculation():
    a=10
    b=20
    res=a+b
    return res
def sleepFun(x):
    print("Thread", x, "is going to sleep for",20," seconds")
    time.sleep(20)  # Actually sleep
    print("Thread", x, "is active now")

for i in range(1,11):
    th=Thread(target=sleepFun,args=(i,))
    th.start()
    time.sleep()
    res=calculation()
    print("res=",res)'''
    

import time
from threading import Thread  # Correct class name

def calculation():
    a = 10
    b = 20
    res = a + b
    return res

def sleepFun(x):
    print("Thread", x, "is going to sleep for", 20, "seconds")
    time.sleep(20)
    print("Thread", x, "is active now")

# Launch 10 threads
for i in range(1, 11):
    th = Thread(target=sleepFun, args=(i,))  # Fixed args
    th.start()
    
    # Optional: Sleep main thread briefly to stagger thread start
    time.sleep(1)  # Fixed: add a duration
    
    res = calculation()
    print("res =", res)
