# 本例用于演示如何在 python 的多进程中做数据通信

import os, time
import multiprocessing
import multiprocessing.connection
import queue
 
# 子进程的示例（继承自 multiprocessing.Process）
class MyChildProcess1(multiprocessing.Process):
    def __init__(self, conn):
        multiprocessing.Process.__init__(self)
        self.conn = conn
 
    def run(self):
        try:
            # poll() 阻塞，直到可以确定连接对象中是否有数据可以读取
            #   None 代表永不超时；如果指定一个数字则代表最大阻塞秒数
            while self.conn.poll(None):
                # 接收另一个连接发来的数据
                data = self.conn.recv()
                print(f'child recv:{data}')
                time.sleep(0.1)
                # 发送数据给另一个连接
                self.conn.send(data.upper())
        except EOFError:
            print("EOFError")

# 通过管道的方式，即 multiprocessing.Pipe() 实现进程间通信的示例
def sample1():
    # 实例化一个 multiprocessing.Pipe() 并返回一对连接，用于通信
    # 子进程用 conn1
    # 主进程用 conn2
    conn1, conn2 = multiprocessing.Pipe()
    p1 = MyChildProcess1(conn1) # 在 MyChildProcess1() 的 __init__() 中通过 multiprocessing.Process() 启动新的进程
    p1.daemon = True
    p1.start()
    for data in ['a', 'b', 'c', 'd']:
        # conn2 发数据给 conn1
        conn2.send(data)
        # conn2 接收 conn1 发来的数据
        recv_data = conn2.recv()
        print(f'main recv:{recv_data}')

    time.sleep(2)

    # 关闭连接
    conn1.close()
    conn2.close()

    p1.join()



# 子进程的示例（继承自 multiprocessing.Process）
class MyChildProcess2(multiprocessing.Process):
    # 注：主进程的发送队列就是子进程的接收队列，主进程的接收队列就是子进程的发送队列
    def __init__(self, recv_queue, send_queue):
        multiprocessing.Process.__init__(self)
        self.recv_queue = recv_queue
        self.send_queue = send_queue
 
    def run(self):
        try:
            while True:
                # 从队列中读取数据（阻塞，并指定超时时间为 2 秒。超时时间为 None 则永不超时）
                data = self.recv_queue.get(block=True, timeout=2)
                print(f'子进程 {os.getpid()} recv:{data}')
                time.sleep(0.1)
                # 把数据放入队列
                self.send_queue.put(data.upper())
        except queue.Empty:
            print(f'子进程 {os.getpid()} 超过 2 秒未收到数据')
    
# 通过队列的方式，即 multiprocessing.Queue() 实现进程间通信的示例
def sample2():
    # 创建发送队列和接收队列
    # 另外，如果想判断队列中的任务是否执行完毕的话可以使用 multiprocessing.JoinableQueue([maxsize])，它增加了 join() 和 task_done()
    #   比如，主进程向一个 queue 放入了多条数据，然后调用 queue.join() 阻塞，子进程从 queue 中每处理一条数据就调用一次 queue.task_done()，这样数据都处理完成后 queue.join() 就会停止阻塞
    send_queue = multiprocessing.Queue()
    recv_queue = multiprocessing.Queue()
    # 队列可以交给多个进程处理，自带并发处理逻辑，不用担心多个进程同时接收或发送的问题
    p1 = MyChildProcess2(send_queue, recv_queue) # 在 MyChildProcess2() 的 __init__() 中通过 multiprocessing.Process() 启动新的进程
    p2 = MyChildProcess2(send_queue, recv_queue) # 在 MyChildProcess2() 的 __init__() 中通过 multiprocessing.Process() 启动新的进程
    p1.daemon = True
    p2.daemon = True
    p1.start()
    p2.start()
    for data in ['a', 'b', 'c', 'd']:
        # 把数据放入队列
        send_queue.put(data)
        # 从队列中读取数据
        recv_data = recv_queue.get()
        print(f'main recv():{recv_data}')

    time.sleep(3)
    
    # 关闭队列
    send_queue.close()
    recv_queue.close()
    
    # 强制杀死指定的进程
    # p1.kill()
    # p2.kill()

    # 阻塞并等待指定的进程执行完毕
    p1.join()
    p2.join()


if __name__ == '__main__':
    sample1()
    sample2()
    