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

import multiprocessing
import time
import os

def func1(i, lock):
    # 获取锁
    lock.acquire()
    print(i, os.getpid())
    # 释放锁
    lock.release()
    time.sleep(1)

# 通过 Process() 开启多进程
def sample1():
    now = time.time()
    l=[]

    # 通过 multiprocessing.Lock() 实现进程同步
    # 需要把这个 lock 传给每个进程，然后在每个进程里 acquire/release
    lock = multiprocessing.Lock()
    for i in range(10):
        p = multiprocessing.Process(target=func1, args=(i,lock))
        p.daemon = True # 是否是守护进程
        p.start()
        l.append(p)

    for p in l:
        p.join() # 阻塞并等待指定的进程执行完毕
        # 强制杀死指定的进程
        # p.kill()

    print('sample1 ok', time.time() - now)



def func2(i, lock):
    # 获取锁
    lock.acquire()
    print(i, os.getpid())
    # 释放锁
    lock.release()
    time.sleep(1)

# 通过进程池开启多进程
def sample2():
    now = time.time()

    # 通过 multiprocessing.Manager().Lock() 实现进程同步
    # 注：在 multiprocessing.Pool() 中不能用 multiprocessing.Lock()
    lock = multiprocessing.Manager().Lock()
    # 注：在 multiprocessing.Pool() 中创建的进程只能是用户进程，而不能创建为守护进程
    pool = multiprocessing.Pool(processes=2) # 池中最大进程数
    for i in range(10):
        pool.apply_async(func=func2, args=(i,lock)) # 从池中申请进程，如果暂时无可用的进程就排队等待

    pool.close() # 关闭进程池，关闭后就不能再申请了
    pool.join() # 阻塞并等待池中进程全部执行完毕

    print('sample2 ok', time.time() - now)


if __name__ == '__main__':
    sample1()
    sample2()


# 另外，关于进程同步，除了 multiprocessing.Lock() 之外，还有
# multiprocessing.Semaphore()
#   可以将 Semaphore 理解为一个许可证中心，该许可证中心的许可证数量是有限的
#   进程想要执行就要先从许可证中心获取一个许可证（如果许可证中心的许可证已经发完了，那就等着，等着其它进程归还许可证），执行完了再还回去
# multiprocessing.Barrier()
#   有个屏障，当所有参与者都到达屏障后，屏障解除
