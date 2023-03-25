#!/usr/bin/env python
# coding: utf-8

from glob import glob
import threading
import time


def test():
    print(time.time())
    time.sleep(1)
    a.pause()
    time.sleep(3)
    a.resume()


class Job(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        for value in kwargs.items():
            globals()["my_var"] = value
        # threading.Thread(target=test).start()  # <- note extra ','
        self.__flag = threading.Event()  # The flag used to pause the thread
        self.__flag.set()  # Set to True
        self.__running = threading.Event()  # Used to stop the thread identification
        self.__running.set()  # Set running to True/ starts thread

    def run(self):
        while self.__running.is_set():
            self.__flag.wait()  # return immediately when it is True, block until the internal flag is True when it is False
            print(globals()["my_var"])
            globals()["my_var"].method()

    def pause(self):
        print("pauzed")
        self.__flag.clear()  # Set to False to block the thread

    def resume(self):
        print("resumed")
        self.__flag.set()  # Set to True, let the thread stop blocking

    def stop(self):
        print("stopped")
        self.__flag.set()  # Resume the thread from the suspended state, if it is already suspended
        self.__running.clear()  # Set to False


#
# https://topic.alibabacloud.com/a/python-thread-pause-resume-exit-detail-and-example-_python_1_29_20095165.html
a = Job(kwargs={"method": test})
a.start()

# b = Job(target=test)
# b.start()


# time.sleep(3)
# a.pause()
# time.sleep(3)
# a.resume()
# time.sleep(3)
# a.pause()
# time.sleep(2)
# a.stop()


class Employee:
    "Common base class for all employees"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee("Zara", 2000)
