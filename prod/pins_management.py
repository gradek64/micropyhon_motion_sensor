import RPi.GPIO as GPIO

def initiate(n):    
    GPIO.setmode(GPIO.BCM) # use Board Pin Number not (0-40 from bottom top)

def setup(pins):
    #argument should be an array with pins to set up either as INPUT or OUTPUT
    for pin in pins:
        if hasattr(pin, 'pinNumber'):
            if hasattr(pin, 'OUTPUT'):
                GPIO.setup(pin.pinNumber, GPIO.OUT)
            elif hasattr(pin, 'INPUT'):
                GPIO.setup(pin.pinNumber, GPIO.OUT)
        else:

def set_pin_on(pinNumber):   # this takes pinNumber
    GPIO.output(pinNumber, GPIO.HIGH)

def is_pin_high(pinNumber):   # this takes pinNumber
    return GPIO.input(pinNumber)

def set_pin_Off(pinNumber):  # this takes pinNumber
    GPIO.output(pinNumber, GPIO.LOW)

def clean_up():
    GPIO.cleanup()