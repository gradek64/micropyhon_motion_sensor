from time import sleep
from testing_intervals import TestData


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


beenHighTime = 0
beenLowDelayCheck = 0
activeCheckTimes = 0


# delay check has to be at least 5 the value that sensor rest to Low
delayCheck = 6

# any number in seconds for single check interval
activeIntervalS1 = 7
# 3 intervals check to make 30s all together
intervalsArrayS1 = [activeIntervalS1 + 4, activeIntervalS1, activeIntervalS1]
timeToSetAlarm = len(intervalsArrayS1) * activeIntervalS1
alarmIsOnFor = 10

# testing remove for actual Pin value once connected
testingIncrement = 0
# testing remove for actual Pin value once connected
class Pin:
    HIGH = True


def runTimingAlarm():
    global beenHighTime
    global firstLongState
    global beenLowDelayCheck
    global activeCheckTimes
    global testing_intervals
    global timeToSetAlarm
    global testingIncrement

    # testing remove for actual Pin value once connected
    testData = TestData()
    Pin.HIGH = testData.flat_onOffVariationsTestS1[testingIncrement]
    # testing remove for actual Pin value once connected

    if Pin.HIGH == True:
        sleep(1)
        # testing
        testingIncrement = testingIncrement + 1
        # testing

        beenHighTime = beenHighTime + 1
        print(f"{Colors.WARNING} Pin been High for: {beenHighTime}{Colors.ENDC}")

        # Pin hits check points secends in intervalsArrayS1
        if beenHighTime == intervalsArrayS1[activeCheckTimes]:
            activeCheckTimes = activeCheckTimes + 1
            # reset beenHighTime for easier calculation based on activeCheckTimes
            beenHighTime = 0
            # reset counting for delay
            beenLowDelayCheck = 0
            print(f"{Colors.OKCYAN}    activeCheckTimes :---: {activeCheckTimes} :----:")

            if activeCheckTimes == 3:
                print(f"{Colors.FAIL}!!! ALARM SET !!!!{Colors.ENDC}")
                # set relay pin on for alarm and light
                # alarm is on for 10s
                # maybe check how many times alarm got off and decrease time for next check ?
                sleep(alarmIsOnFor)
                # reset everything but activeCheckTimes to 1 to set alarm now to 20s
                beenHighTime = 0
                activeCheckTimes = 1

        runTimingAlarm()
    else:
        sleep(1)
        # testing
        testingIncrement = testingIncrement + 1
        # testing

        # always reset beenHighTime cause activeCheckTimes tracks if was active before
        beenHighTime = 0
        # someone already been there for at lest 10s
        if activeCheckTimes > 0:
            beenLowDelayCheck = beenLowDelayCheck + 1
            print(f"{Colors.OKGREEN} been Low for: {beenLowDelayCheck}{Colors.ENDC}")
            if beenLowDelayCheck > delayCheck:
                beenLowDelayCheck = 0
                activeCheckTimes = 0
                print(
                    f"{Colors.OKCYAN} delay has passed of more than {delayCheck}s RESET --- activeCheckTimes: {activeCheckTimes} -- {Colors.ENDC}"
                )
        else:
            print(f"{Colors.OKGREEN} Pin has been LOW--- activeCheckTimes: {activeCheckTimes} -- {Colors.ENDC}")

        runTimingAlarm()


runTimingAlarm()
