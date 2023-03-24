import threading
from Pin_Class import Pin

pin1 = Pin(1)
pin2 = Pin(2)

timer1 = threading.Thread(target=pin1.runTimingAlarm)
timer1.start()
timer2 = threading.Thread(target=pin2.runTimingAlarm)
timer2.start()

timer1.join()
