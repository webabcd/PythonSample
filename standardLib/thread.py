# 通过 import threading 实现多线程（注：一个进程同一个时刻只有一个线程在执行，要想利用多核 cpu 则需要用多进程）

import threading
import time
from threading import Timer

# 继承 threading.Thread
class MyThread(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.name = threadName

    # 需要在新开线程中执行的逻辑
    def run(self):
        myPrint(self.name + " 开始")

        temp = 0
        start = time.perf_counter() # 获取设备开机到现在经过的秒数
        while True:
            if temp < 10:
                myPrint(self.name + " 运行中")
                time.sleep(0.2) # 阻塞 0.2 秒
                temp += 1
            else:
                break

        end = time.perf_counter()
        myPrint(f"{self.name} 运行了 {end-start} {start}秒，退出")

# 通过 threading.Lock() 实现线程同步
lock = threading.Lock()
def myPrint(message):
    # 获取锁
    lock.acquire()
    print(message) # 自己可以测试一下，不用锁的话打印会比较乱，用了锁就不会了
    # 释放锁
    lock.release()


# 创建新线程
thread1 = MyThread("thread_1")
thread2 = MyThread("thread_2")
thread3 = MyThread("thread_3")

# 启动新线程
thread1.start()
thread2.start()
thread3.start()

# 在当前线程等待新开线程执行完毕
thread1.join()
thread2.join()
thread3.join()



def after():
    print('after')
# 通过 timer 实现在指定时间后执行指定函数的功能
timer = Timer(1, after)
timer.start()
timer.join()
