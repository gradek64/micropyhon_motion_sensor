import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print('class Pin')
class GPIO_Pin:
    def __init__(self, number, mode):
        self.number = number
        if mode == 'Output':
            GPIO.setup(number, GPIO.OUT)
        if mode == 'Input':
            GPIO.setup(number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            
    def writeOutPin(self,value):
        if value == 'LOW':
            GPIO.output(self.number, GPIO.LOW)
        else:
            GPIO.output(self.number, GPIO.HIGH)
            
    def readPinValue(self):
        return GPIO.input(self.number)
    
    
# this method belongs to file to be called only once
def cleanUp():
    print('cleanup')
    GPIO.cleanup()
              