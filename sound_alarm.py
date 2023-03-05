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


beenHighTime = 0
beenLowDelayCheck = 0
delayCheck = 6
ActiveInterval = 10
activeCheckTimes = 0
# 3 intervals check to make 30s all together
intervalsArray = [ActiveInterval, ActiveInterval, ActiveInterval]
timeToSetAlarm = 30
alarmIsONFor = 10

# testing remove for actual Pin value once connected
class Pin:
    HIGH = True


testingIncrement = 0
onOffVariationsTest = [
    [True] * 15,
    [False] * 4,
    [True] * 20,
    [False] * 3,
    [True] * 10,
    [False] * 3,
    [True] * 5,
    [False] * 3,
    [True] * 20,
    [False] * 3,
]
flat_onOffVariationsTest = sum(onOffVariationsTest, [])
# testing remove for actual Pin value once connected


def runTimingAlarm():
    global beenHighTime
    global firstLongState
    global beenLowDelayCheck
    global activeCheckTimes
    global testingIncrement
    global timeToSetAlarm

    # testing remove for actual Pin value once connected
    Pin.HIGH = flat_onOffVariationsTest[testingIncrement]
    # testing remove for actual Pin value once connected

    if Pin.HIGH == True:
        sleep(1)
        # testing
        testingIncrement = testingIncrement + 1
        # testing

        beenHighTime = beenHighTime + 1
        print(f"{Colors.WARNING} beenHighTime for: {beenHighTime}{Colors.ENDC}")

        # Pin hits check points secends in intervalsArray
        if beenHighTime == intervalsArray[activeCheckTimes]:
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
                sleep(alarmIsONFor)
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
            print(f"{Colors.OKGREEN} beenLowTime for: {beenLowDelayCheck}{Colors.ENDC}")
            if beenLowDelayCheck > delayCheck:
                beenLowDelayCheck = 0
                activeCheckTimes = 0
                print(f"{Colors.OKCYAN} delay has passed of more than {delayCheck}{Colors.ENDC}")
        else:
            print(f"{Colors.OKGREEN} has been OFF: {testingIncrement} second {Colors.ENDC}")

        runTimingAlarm()


runTimingAlarm()
