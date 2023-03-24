from time import sleep
from testing_intervals import TestData

# testing remove for actual Pin value once connected
testData = TestData()
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


class Pin:
    # self means attribute
    def __init__(self, pinNumber):
        self.pinNumber = pinNumber
        self.beenHighTime = 0
        self.HIGH = False
        self.activeCheckTimes = 0
        self.beenLowDelayCheck = 0
        self.alarmIsOnFor = 10
        # delay check has to be at least 5 the value that sensor rest to Low
        self.delayCheck = 6
        # any number in seconds for single check interval
        self.activeInterval = 10
        # 3 intervals check to make 30s all together
        self.intervalsArray = [self.activeInterval, self.activeInterval, self.activeInterval]
        # self.timeToSetAlarm = len(self.activeInterval) * self.activeInterval

        # testing remove for actual Pin value once connected
        self.testingIncrement = 0
        # testing remove for actual Pin value once connected

    def runTimingAlarm(self):
        # testing remove for actual Pin value once connected
        self.HIGH = testData.getIndex(self.pinNumber)[self.testingIncrement]

        if self.HIGH == True:
            sleep(1)
            # testing
            self.testingIncrement += 1
            # testing
            self.beenHighTime += 1
            print(f"{Colors.WARNING} Pin {self.pinNumber} been High for: {self.beenHighTime}{Colors.ENDC}")

            # Pin hits check points secends in intervalsArray
            if self.beenHighTime == self.intervalsArray[self.activeCheckTimes]:
                self.activeCheckTimes += 1
                # reset beenHighTime for easier calculation based on activeCheckTimes
                self.beenHighTime = 0
                # reset counting for delay
                self.beenLowDelayCheck = 0
                print(f"{Colors.OKCYAN} Pin {self.pinNumber}  activeCheckTimes :---: {self.activeCheckTimes} :----:")

                if self.activeCheckTimes == 3:
                    print(f"{Colors.FAIL}!!! Pin {self.pinNumber} ALARM SET !!!!{Colors.ENDC}")
                    # set relay pin on for alarm and light
                    # alarm is on for 10s
                    # maybe check how many times alarm got off and decrease time for next check ?
                    sleep(self.alarmIsOnFor)
                    # reset everything but activeCheckTimes to 1 to set alarm now to 20s
                    self.beenHighTime = 0
                    self.activeCheckTimes = 1

            self.runTimingAlarm()
        else:
            sleep(1)
            # testing
            self.testingIncrement = self.testingIncrement + 1
            # testing

            # always reset beenHighTime cause activeCheckTimes tracks if was active before
            self.beenHighTime = 0

            if self.activeCheckTimes > 0:
                self.beenLowDelayCheck += 1
                print(f"{Colors.OKGREEN} Pin {self.pinNumber} been Low for: {self.beenLowDelayCheck}{Colors.ENDC}")
            if self.beenLowDelayCheck > self.delayCheck:
                self.beenLowDelayCheck = 0
                self.activeCheckTimes = 0
                print(
                    f"{Colors.OKCYAN}  Pin {self.pinNumber} delay has passed of more than {self.delayCheck}s RESET --- activeCheckTimes: {self.activeCheckTimes} -- {Colors.ENDC}"
                )
            else:
                print(
                    f"{Colors.OKGREEN} Pin {self.pinNumber} has been LOW--- activeCheckTimes: {self.activeCheckTimes} -- {Colors.ENDC}"
                )

        self.runTimingAlarm()
