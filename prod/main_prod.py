import threading
from Sensor_Class import Sensor
from Sound_Class import Sound
from GPIO_Pin_Class import GPIO_Pin


# ------ set up pins first ---- 

# pins out
detection_led = GPIO_Pin(4,'Output')
relay_output_1 = GPIO_Pin(25,'Output')

# pins in
front_sensor =  GPIO_Pin(23, 'Input', 'front_sensor')
back_sensor =  GPIO_Pin(24, 'Input', 'back_sensor')

#sound class init
sounds = Sound()

####### how it works ? #####

# this intervalsArray [2,3,4] length makes number of interval 
# the alarm will set when all intervals will pass 
# and sum of all seconds [2,3,4] = 9s will pass
# if there is a break of 6s between interval it will reset to 0
# will needs 3 consecutive intervals and sum of intervalsArray of 9 seconds ([2,3,4] = 9s) to set the alarm

########

# Sensor(id, sensorPin, detection_led, relayOutput1, intervalsArray, soundClass, debug=false) 
# experiment with how many seconds you need once installed


sensor1 = Sensor(1, front_sensor, detection_led, relay_output_1, [5,5,5], sounds, False)  # 10x3 series 30 seconds sound the alarm in 3 intervals
sensor2 = Sensor(2, back_sensor, detection_led, relay_output_1, [3], sounds, False )  # 5x2 series 10 seconds sound the alarm in 2 intervals



timer1 = threading.Thread(target=sensor1.runTimingAlarm)
timer1.start()
timer2 = threading.Thread(target=sensor2.runTimingAlarm)
timer2.start()
