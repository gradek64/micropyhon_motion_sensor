from time import sleep
import testing_intervals


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


secondsOfBeenHigh = 0
beenLowDelayCheck = 0
activeCheckTimesPin1 = 0
activeCheckTimesPin2 = 0

# delay check has to be at least 5 the value that sensor rest to Low
delayCheck = 6

# any number in which second will do check
# if single check it will sound alarm if multiple check will increase
# activeCheckTimes increment


# 1 interval check to make 5s all together for Pin1 second check sound alarm after 3s
activeIntervalS1 = 5
intervalsInWhichSecondHighCheckArrayS1 = [activeIntervalS1, activeIntervalS1 - 2]
timeToSetAlarmPin1 = len(intervalsInWhichSecondHighCheckArrayS1) * activeIntervalS1

# 3 intervals check to make 30s all together for Pin2
activeIntervalS2 = 7
intervalsInWhichSecondHighCheckArrayS2 = [activeIntervalS2 + 4, activeIntervalS2, activeIntervalS2]
timeToSetAlarmPin2 = len(intervalsInWhichSecondHighCheckArrayS2) * activeIntervalS2

# alarm will sound for 10s
alarmIsOnFor = 2

# testing remove for actual Pin1 value once connected
testingIncrement = 0
# testing remove for actual Pin1 value once connected
class Pin1:
    HIGH = True


class Pin2:
    HIGH = True


def runTimingAlarm():
    global secondsOfBeenHigh
    global firstLongState
    global beenLowDelayCheck
    global activeCheckTimesPin1
    global activeCheckTimesPin2
    global testing_intervals
    global timeToSetAlarmPin1
    global testingIncrement
    global pinActive

    # testing remove for actual Pin1 value once connected
    Pin1.HIGH = testing_intervals.flat_onOffVariationsTestS1[testingIncrement]
    Pin2.HIGH = testing_intervals.flat_onOffVariationsTestS2[testingIncrement]
    # testing remove for actual Pin1 value once connected

    if Pin1.HIGH == True or Pin2.HIGH == True:
        sleep(1)
        # testing
        testingIncrement = testingIncrement + 1
        # testing

        secondsOfBeenHigh = secondsOfBeenHigh + 1
        print(f"{Colors.WARNING} short Pin1.HIGH: {Pin1.HIGH} longPin2.HIGH: {Pin2.HIGH} {Colors.ENDC}")

        # Pin2 hits check points seconds in intervalsInWhichSecondHighCheckArrayS2 [11,7,7]
        if Pin2.HIGH == True and secondsOfBeenHigh == intervalsInWhichSecondHighCheckArrayS2[activeCheckTimesPin2]:
            activeCheckTimesPin2 = activeCheckTimesPin2 + 1
            # reset secondsOfBeenHigh for easier calculation based on activeCheckTimesPin1
            secondsOfBeenHigh = 0
            # reset counting for delay
            beenLowDelayCheck = 0
            print(f"{Colors.OKCYAN}    activeCheckTimesPin2 :---: {activeCheckTimesPin2} :----:")

            if activeCheckTimesPin2 == len(intervalsInWhichSecondHighCheckArrayS2):
                print(f"{Colors.FAIL}!!! ALARM SET !!!! from PIN 2{Colors.ENDC}")
                # set relay pin1 on for alarm and light
                # alarm is on for 10s
                # maybe check how many times alarm got off and decrease time for next check ?
                sleep(alarmIsOnFor)
                # reset secondsOfBeenHigh for next interval check
                secondsOfBeenHigh = 0
                # activeCheckTimesPin2 to 0 to set alarm again to 3s
                activeCheckTimesPin2 = 0

        # Pin1 hits check points seconds in intervalsInWhichSecondHighCheckArrayS1 [5,3]
        if Pin1.HIGH == True and secondsOfBeenHigh == intervalsInWhichSecondHighCheckArrayS1[activeCheckTimesPin1]:
            activeCheckTimesPin1 = activeCheckTimesPin1 + 1
            # reset secondsOfBeenHigh for easier calculation based on activeCheckTimesPin1
            secondsOfBeenHigh = 0
            # reset counting for delay
            beenLowDelayCheck = 0
            print(f"{Colors.OKCYAN}    activeCheckTimesPin1 :---: {activeCheckTimesPin1} :----:")

            if activeCheckTimesPin1 == 1 or activeCheckTimesPin1 == 2:
                print(f"{Colors.FAIL}!!! ALARM SET  !!!! from PIN 1{Colors.ENDC}")
                # set relay pin1 on for alarm and light
                # alarm is on for 10s
                # maybe check how many times alarm got off and decrease time for next check
                sleep(alarmIsOnFor)
                # reset secondsOfBeenHigh for next interval check
                secondsOfBeenHigh = 0
                # reset everything but activeCheckTimesPin1 to 1 to set alarm now to 20s
                activeCheckTimesPin1 = 1

        runTimingAlarm()
    else:
        sleep(1)
        # testing
        testingIncrement = testingIncrement + 1
        # testing

        # always reset secondsOfBeenHigh cause activeCheckTimesPin1 tracks if was active before
        secondsOfBeenHigh = 0
        # someone already been there for at lest 10s
        if activeCheckTimesPin1 > 0:
            beenLowDelayCheck = beenLowDelayCheck + 1
            print(f"{Colors.OKGREEN} been Low for: {beenLowDelayCheck}{Colors.ENDC}")
            if beenLowDelayCheck > delayCheck:
                beenLowDelayCheck = 0
                activeCheckTimesPin1 = 0
                print(
                    f"{Colors.OKCYAN} delay has passed of more than {delayCheck}s RESET --- activeCheckTimesPin1: {activeCheckTimesPin1} -- {Colors.ENDC}"
                )
        elif activeCheckTimesPin2 > 0:
            beenLowDelayCheck = beenLowDelayCheck + 1
            print(f"{Colors.OKGREEN} been Low for: {beenLowDelayCheck}{Colors.ENDC}")
            if beenLowDelayCheck > delayCheck:
                beenLowDelayCheck = 0
                activeCheckTimesPin2 = 0
                print(
                    f"{Colors.OKCYAN} delay has passed of more than {delayCheck}s RESET --- activeCheckTimesPin2: {activeCheckTimesPin2} -- {Colors.ENDC}"
                )
        else:
            print(
                f"{Colors.OKGREEN} Pin1  has been LOW--- activeCheckTimesPin1: {activeCheckTimesPin1} -- {Colors.ENDC}"
            )
            print(
                f"{Colors.OKGREEN} Pin2 has been LOW--- activeCheckTimesPin1: {activeCheckTimesPin2} -- {Colors.ENDC}"
            )

        runTimingAlarm()


runTimingAlarm()
