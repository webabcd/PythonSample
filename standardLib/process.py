# 本例用于演示 python 的多进程
# 
# 在 cpython 解释器中，GIL 是一把互斥锁，用来保证进程中同一个时刻只有一个线程在执行
# 所以你即使在一个进程中开了多线程，他们也无法并行执行
#
# coroutine(async/awawit) 要比 thread 简单，并且一个进程中同一个时刻只有一个线程或协程在执行，他们的运行效率没区别，所以尽量都用 coroutine
# 一个进程只能在一个核上运行，如果要充分利用多核 cpu 则需要用多进程
#
# io（网络请求，硬盘存储等）密集型建议用 coroutine，因为它的 cpu 占用率不高，一个核也足够支撑多个 io 任务的同时高效运行
# 计算密集型建议用多进程，否则会因为单核 cpu 占用极高，而阻塞其他线程或协程的运行

from multiprocessing import Process
import time
import os

def func1(x, y):
    print(x, y, os.getpid())
    time.sleep(1)

if __name__ == '__main__':
    now = time.time()
    l=[]

    for i in range(10):
        p = Process(target=func1, args=(1, 2))
        p.start()
        l.append(p)

    for p in l:
        p.join()

    print('完成', time.time() - now)