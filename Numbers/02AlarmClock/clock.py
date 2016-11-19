# -*- coding:utf-8 -*-
import MyTimer
import time
import os


DueTime = []
Word = ""
End = False


def clock():
    # os.system('cls')
    global DueTime, Word, End
    t = time.localtime()
    print(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
    if (t.tm_year == DueTime[0] and
        t.tm_mon == DueTime[1] and
        t.tm_mday == DueTime[2] and
        t.tm_hour == DueTime[3] and
        t.tm_min == DueTime[4] and
        t.tm_sec >= DueTime[5]):
        print(Word)
        End = True

    # time.sleep(0.5)


def InitData():
    print("现在时间:")
    t = time.localtime()
    print(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
    print("输入你要约定的时间（格式:yyyy/mm/dd/hh/mm/ss)")
    duetime = input()
    print("输入你要显示的一句话：")
    word = input()
    return duetime, word

if __name__ == "__main__":
    DueTime, Word = InitData()
    DueTime = DueTime.split("/")
    DueTime = [int(x) for x in DueTime]
    timer = MyTimer.MyTimer()
    timer.start(1, clock)
    while True:
        time.sleep(1)
        if End == True:
            print("结束")
            # timer._timer.cancel()
            timer.stop()
            break
