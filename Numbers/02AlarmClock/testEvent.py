# -*- coding:utf-8 -*-
from threading import Timer
import time

timer_interval = 1
j = 0


def delayrun():
    global j
    j = j + 1
    print("running", j)

t = Timer(timer_interval, delayrun)
t.start()
i = 0
while True:
    time.sleep(0.1)
    i = i + 1
    print("main running", i)
