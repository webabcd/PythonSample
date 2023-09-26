# 本例用于演示如何通过 async/await 实现异步编程
# 协程相当于轻量级的线程

import asyncio

# 通过 async 修饰的函数支持异步执行
async def func1():
    print('coroutine1')
async def func2():
    print('coroutine2')
# 构造需要并行执行的异步函数列表
task = [func1(), func2()]
# 创建事件循环
loop = asyncio.get_event_loop()
# 阻塞，直至所有异步函数执行完成
loop.run_until_complete(asyncio.wait(task))
# 关闭事件循环
loop.close()



async def func3(name, delay):
    await asyncio.sleep(delay)
    print(name)
async def sample1():
    # 并行执行多个异步函数
    await asyncio.gather(
        func3("a", 3),
        func3("b", 2),
        func3("c", 1),
    )
# 阻塞，直至指定的异步函数执行完成（不需要手写事件循环）
asyncio.run(sample1())



async def sample2():
    # 创建一个异步任务并立刻并行执行（下面的 task1,task2,task3 会并行执行）
    task1 = asyncio.create_task(func3("x", 1))
    task2 = asyncio.create_task(func3("y", 1))
    task3 = asyncio.create_task(func3("z", 1))
    # 阻塞，直至 task1,task2,task3 执行完成
    await task1
    await task2
    await task3
# 阻塞，直至指定的异步函数执行完成
asyncio.run(sample2())