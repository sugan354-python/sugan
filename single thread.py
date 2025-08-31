'''import time
from threading import Thread
def sleepFun(x):
    print("thread",x,"is going sleep for 5 second")
    print("thread",x,"is active now:")
th=Thread(target=sleepfun,args=(1,))
th.start()
time.sleep(2)
print("hello i am executing parallel to thread")'''

import time
from threading import Thread  # Correct class name

def sleepFun(x):
    print("Thread", x, "is going to sleep for 5 seconds")
    time.sleep(5)  # Actually sleep
    print("Thread", x, "is active now")

# Start the thread
th = Thread(target=sleepFun, args=(1,))
th.start()

# Main thread sleeps for 2 seconds
time.sleep(2)
print("Hello, I am executing parallel to the thread")

