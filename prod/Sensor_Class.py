from time import sleep
# from testing_intervals import TestData

# testing remove for actual Pin value once connected
# testData = TestData()
# testing remove for actual Pin value once connected


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
    # self means attribute
    def __init__(
        self,
        sensorPin,
        detectionLed,
        relayOutput1,
        activeIntervalCheck,
        activeSeriesNum,
        debug = False
        ):
        self.debug = debug
        self.sensorPin = sensorPin
        self.detectionLed = detectionLed
        self.relayOutput1 = relayOutput1
        self.beenHighTime = 0
        self.HIGH = False
        self.activeCheckTimes = 0
        self.beenLowDelayCheck = 0
        self.alarmIsOnFor = 10
        # delay check has to be at least 5-6 the value that sensor reset to Low
        self.delayCheck = 6
        # any number in seconds for single check interval
        self.activeInterval = activeIntervalCheck
        self.intervalsArray = []
        # x intervals check to make 30s all together for example 3 x activeIntervalCheck
        for x in range(activeSeriesNum):
            self.intervalsArray.append(self.activeInterval)

        # testing remove for actual Pin value once connected
        # self.testingIncrement = 0
        # testing remove for actual Pin value once connected
    def runTimingAlarm(self):
        self.HIGH = self.sensorPin.readPinValue()
        ledOff = not self.detectionLed.readPinValue()

        if self.HIGH == True:
            sleep(1)
            # testing
            # self.testingIncrement += 1
            # testing
            
            # sensor High set Led on if Not already on
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

                if self.activeCheckTimes == len(self.intervalsArray):
                    if self.debug:
                        print(f"{Colors.FAIL}!!! Pin {self.sensorPin.readPinName()} ALARM SET !!!!{Colors.ENDC}")
                    # set relay pin on for alarm and light
                    # alarm is on for 10s
                    # maybe check how many times alarm got off and decrease time for next check ?
                    sleep(self.alarmIsOnFor)
                    # reset everything
                    self.beenHighTime = 0
                    self.activeCheckTimes = 0

            self.runTimingAlarm()
        else:
            sleep(1)
            # testing
            # self.testingIncrement = self.testingIncrement + 1
            # testing
            
             # sensor Low set Led off if Not already off
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
        # run method in next second
        self.runTimingAlarm()
