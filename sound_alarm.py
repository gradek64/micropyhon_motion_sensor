from email.policy import default
from tabnanny import check
from time import sleep, time


isTriggered = False
defaultReset = 6
checkInSeconds = [defaultReset]


class Pin:
    HIGH = False


# this function recursively check if montion sensor is triggered
def runTimingAlarm():
    global isTriggered

    # first check if pin is High => sensor is triggered
    if Pin.HIGH == True:
        print("sensor IS Triggered")
    else:
        sleep(1)
        print("sensor NOT triggered")
        runTimingAlarm()

    if isTriggered == False:
        isTriggered = True
        startTime = time()
        for seconds in checkInSeconds:
            print("run started")
            sleep(seconds)
            print("time after deafult")
            print(Pin.HIGH)
            # first condition is not triggered after defaultReset time (6s)
            if Pin.HIGH == False:
                print("is off")
        endTime = time()
        elapsedTime = endTime - startTime
        print("Elapsed Time = %s" % elapsedTime)


runTimingAlarm()

i = 1
# infinite loop
# while i < 20:
# print(i)
# if Pin.HIGH == True:
#  runTimingAlarm()
#  if i > 4 and i < 10:
#  Pin.HIGH = False
#  else:
#  Pin.HIGH = True
# sleep(1)
#  i += 1
