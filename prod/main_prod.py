import threading
from Sensor_Class import Sensor
from GPIO_Pin_Class import GPIO_Pin


# ------ set up pins first ---- 

# pins out
detection_led = GPIO_Pin(4,'Output')
relay_output_1 = GPIO_Pin(25,'Output')

# pins in
front_sensor =  GPIO_Pin(23, 'Input', 'front_sensor')
back_sensor =  GPIO_Pin(24, 'Input', 'back_sensor')

# Sensor(sensorPin, detection_led, relayOutput1, activeIntervalCheck, activeSeriesNum, debug=false) 
sensor1 = Sensor(front_sensor, detection_led, relay_output_1, 10, 3, True)  # 10x3 series 30 seconds sound the alarm
sensor2 = Sensor(back_sensor, detection_led, relay_output_1, 7, 1, True)  # 7x1 series 7 seconds sound the alarm



timer1 = threading.Thread(target=sensor1.runTimingAlarm)
timer1.start()
timer2 = threading.Thread(target=sensor2.runTimingAlarm)
timer2.start()
