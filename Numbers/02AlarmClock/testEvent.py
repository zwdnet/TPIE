# -*- coding:utf-8 -*-
# from threading import Timer
# import time
#
# timer_interval = 1
# j = 0
#
#
# def delayrun():
#     global j
#     j = j + 1
#     print("running", j)
#
# t = Timer(timer_interval, delayrun)
# t.start()
# i = 0
# while True:
#     time.sleep(0.1)
#     i = i + 1
#     print("main running", i)

# import time, gevent
#
#
# def print_time(sleep_time, tag):
#     print(time.time(), tag)
#     time.sleep(sleep_time)
#
#
# def run_regularly(function, intervals, sleep_time=0.1, round_length=1):
#     _, init = divmod(time.time(), 1)
#     gevent.sleep(1 - init)
#     while True:
#         before = time.time()
#         _, offset = divmod(before, round_length)
#         for div in intervals:
#             function(sleep_time, div)
#             after = time.time() - before
#             if after < (div * round_length):
#                 gevent.sleep((div * round_length) - after - (offset/len(intervals)))
#
# gevent.spawn(run_regularly(), print_time, [0.2, 0.8, 1.0])
#
# while True:
#     gevent.sleep(0.1)
from MyTimer import MyTimer


def hello():
    from datetime import datetime
    print("hello world", datetime.now())


if __name__ == "__main__":
    mt = MyTimer()
    mt.start(2, hello)
    for i in range(10):
        import time
        time.sleep(1)
    mt.stop()