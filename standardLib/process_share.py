# 本例用于演示如何在 python 的多进程中做数据共享

import multiprocessing
from multiprocessing import shared_memory
from ctypes import c_char_p

def func1(i, lock, sm_name):
    lock.acquire()
    # 根据指定的名称获相关的 SharedMemory 对象
    sm = shared_memory.SharedMemory(sm_name)

    # 获取共享内存中的数据
    s = bytes(sm.buf[0:]).decode().strip("\x00")
    i = 0 if s == '' else int(s)
    i += 1
    b = str(i).encode()
    # 设置共享内存中的数据
    sm.buf[0:len(b)] = b

    # 关闭共享内存（数据不会被销毁，可以随时再打开）
    sm.close()
    lock.release()

# 通过 SharedMemory() 在多进程之间共享内存
def sample1():
    l=[]

    # 创建一个新的 SharedMemory 实例，大小为 256 字节
    sm = shared_memory.SharedMemory(create=True, size=256)
    lock = multiprocessing.Lock()
    for i in range(10):
        p = multiprocessing.Process(target=func1, args=(i,lock,sm.name))
        p.daemon = True
        p.start()
        l.append(p)
    for p in l:
        p.join()

    # 获取共享内存中的数据
    result = bytes(sm.buf[0:]).decode().strip("\x00")
    # 关闭共享内存（数据不会被销毁，可以随时再打开）
    sm.close()
    # 释放共享内存（数据会被销毁）
    sm.unlink()

    print('sample1 ok', result)



def func2(i, lock,v_i, v_d,v_c_char_p,m_dict,m_list):
    with v_i.get_lock(): # 支持通过 get_lock() 加锁
        v_i.value += 1
    with v_d.get_lock(): # 支持通过 get_lock() 加锁
        v_d.value += 1.1

    # 需要手动加锁
    lock.acquire()
    v_c_char_p.value += str(i)
    m_dict["k"] += str(i)
    m_list.append(i)
    lock.release()

# 通过 multiprocessing.Value() 和 multiprocessing.Manager() 在多进程之间共享整型，浮点型，字符串，字典，列表等数据
def sample2():
    v_i = multiprocessing.Value('i', 0) # 整型
    v_d = multiprocessing.Value('d', 0.0) # 浮点型
    v_c_char_p = multiprocessing.Manager().Value(c_char_p, "hello") # 字符串
    m_dict = multiprocessing.Manager().dict() # 字典表
    m_dict["k"] = "hello"
    m_list = multiprocessing.Manager().list() # 列表

    lock = multiprocessing.Lock()
    p_list = [multiprocessing.Process(target=func2, args=(i,lock,v_i,v_d,v_c_char_p,m_dict,m_list)) for i in range(10)]
    for p in p_list:
        p.start()
    for p in p_list:
        p.join()

    print('sample2 ok', v_i.value, v_d.value, v_c_char_p.value, m_dict["k"], m_list)


if __name__ == '__main__':
    sample1()
    sample2()
