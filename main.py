import threading
from Pin_Class import Pin

# pin number, activeCheckInterval, how many in series
pin1 = Pin(1, 10, 3)  # 10x3 series 30 seconds sound the alarm
pin2 = Pin(2, 7, 1)  # 7x1 series 7 seconds sound the alarm

timer1 = threading.Thread(target=pin1.runTimingAlarm)
timer1.start()
timer2 = threading.Thread(target=pin2.runTimingAlarm)
timer2.start()
