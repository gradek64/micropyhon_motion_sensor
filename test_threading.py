# Python program showing
# how to kill threads
# using set/reset stop
# flag

import threading
import time


def run():
    while True:
        time.sleep(1)
        print("thread running")
        global stop_threads
        if stop_threads:
            break


stop_threads = False
t1 = threading.Thread(target=run)
t1.start()
time.sleep(3)
stop_threads = True
t1.join()
print("thread killed")
t1.start()
