import threading
from Sensor_Class import Sensor


####### how it works ? #####

# this intervalsArray [2,3,4] length makes number of interval 
# the alarm will set when all intervals will pass 
# and sum of all seconds [2,3,4] = 9s will pass
# if there is a break of 6s between interval it will reset to 0
# will needs 3 consecutive intervals and sum of intervalsArray of 9 seconds ([2,3,4] = 9s) to set the alarm

########

#pinNumber, arrayOfSeconds
sensor1 = Sensor(1, [10,5,5]) 
sensor2 = Sensor(2, [8,1])

timer1 = threading.Thread(target=sensor1.runTimingAlarm)
timer1.start()
timer2 = threading.Thread(target=sensor2.runTimingAlarm)
timer2.start()
