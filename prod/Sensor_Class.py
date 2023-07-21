from time import sleep

class Colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Sensor:
    # self means private Class attribute
    def __init__(
        self,
        id,
        sensorPin,
        detectionLed,
        relayOutput1,
        activeIntervalCheck,
        activeSeriesNum,
        sounds,
        debug = False
        ):
        self.id = id
        self.debug = debug
        self.sensorPin = sensorPin
        self.detectionLed = detectionLed
        self.relayOutput1 = relayOutput1
        self.beenHighTime = 0
        self.HIGH = False
        self.sounds = sounds
        self.activeCheckTimes = 0
        self.beenLowDelayCheck = 0
        self.alarmIsOnFor = 10
        # delay check has to be at least 5-6 the value that sensor reset to Low
        self.delayCheck = 6
        # any number in seconds for single check interval
        self.activeInterval = activeIntervalCheck
        self.intervalsArray = []
        self.activeSeriesNum = activeSeriesNum
        # x intervals check to make 30s all together for example 3 x activeIntervalCheck
        for x in range(activeSeriesNum):
            self.intervalsArray.append(self.activeInterval)
        
        #play(audio_notify) when second sensor is engaged
        if self.id == 2:
            self.sounds.playSound('notify_ready')

        if self.debug:
            print('audio notification should have played')
        
    def runTimingAlarm(self):
        while True:
            self.HIGH = self.sensorPin.readPinValue()
            ledOff = not self.detectionLed.readPinValue()

            if self.HIGH == True:
                # check pin ON every second
                sleep(1)
                
                # sensor High, set Led ON if Not already ON
                if ledOff:
                    self.detectionLed.writeOutPin('HIGH')
                    
                self.beenHighTime += 1
                if self.debug:
                    print(f"{Colors.WARNING} Pin {self.sensorPin.readPinName()} been High for: {self.beenHighTime}{Colors.ENDC}")
                
                # Pin hits check points secends in intervalsArray
                if self.beenHighTime == self.intervalsArray[self.activeCheckTimes]:
                    self.activeCheckTimes += 1
                    # reset beenHighTime for easier calculation based on activeCheckTimes
                    self.beenHighTime = 0
                    # reset counting for delay
                    self.beenLowDelayCheck = 0
                    if self.debug:
                        print(f"{Colors.OKCYAN} Pin {self.sensorPin.readPinName()}  activeCheckTimes :---: {self.activeCheckTimes} :----:")
                    
                    # play warning audio when all intervals are greater than 1
                    if self.activeSeriesNum !=1 and self.activeCheckTimes == len(self.intervalsArray) -1:
                        if self.debug:
                            print('dog barking warning')
                        
                        #start warning audio
                        self.sounds.playSound('dog_barking')

                    if self.activeCheckTimes == len(self.intervalsArray):
                        if self.debug:
                            print(f"{Colors.FAIL}!!! Pin {self.sensorPin.readPinName()} ALARM SET !!!!{Colors.ENDC}")
                            print(f"{Colors.FAIL}!!! me shouting")
                        
                        #start warning audio
                        self.sounds.playSound('let_me_sleep')
                        
                        # set relay pin on for alarm if not already on
                        relayOff = not self.relayOutput1.readPinValue()
                        if relayOff:
                            if self.debug:
                                print(f"{Colors.FAIL}!!! ===> relay set ON")
                            self.relayOutput1.writeOutPin('HIGH')
                        
                        # alarm is on for 10s
                        # maybe check how many times alarm got off and decrease time for next check ?
                        sleep(self.alarmIsOnFor)
                        #turn off the relay
                        if self.debug:
                            print(f"{Colors.FAIL}!!! ===> relay set OFF")
                        self.relayOutput1.writeOutPin('LOW')
                        # reset everything
                        self.beenHighTime = 0
                        self.activeCheckTimes = 0

                # do not use recursive it has limit of 1000 repeats
                # run method in next second
                # self.runTimingAlarm()
            else:
                # check pin OFF every second
                sleep(1)

                # sensor Low, set Led OFF if Not already OFF
                if not ledOff:
                    self.detectionLed.writeOutPin('LOW')
                    
                # always reset beenHighTime cause activeCheckTimes tracks if was active before
                self.beenHighTime = 0

                if self.activeCheckTimes > 0:
                    self.beenLowDelayCheck += 1
                    if self.debug:
                        print(f"{Colors.OKGREEN} Pin {self.sensorPin.readPinName()} been Low for: {self.beenLowDelayCheck}{Colors.ENDC}")
                if self.beenLowDelayCheck > self.delayCheck:
                    self.beenLowDelayCheck = 0
                    self.activeCheckTimes = 0
                    if self.debug:
                        print(
                        f"{Colors.OKCYAN}  Pin {self.sensorPin.readPinName()} delay has passed of more than {self.delayCheck}s RESET --- activeCheckTimes: {self.activeCheckTimes} -- {Colors.ENDC}"
                        )
                else:
                    if self.debug:
                        print(
                        f"{Colors.OKGREEN} Pin {self.sensorPin.readPinName()} has been LOW--- activeCheckTimes: {self.activeCheckTimes} -- {Colors.ENDC}"
                        )

            # do not use recursive it has limit of 1000 repeats
            # run method in next second
            # self.runTimingAlarm()
