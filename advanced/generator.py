# generator 生成器（通过 yield 实现生成器，生成器返回的是迭代器）

# 定义一个生成器（有 yield 的就是生成器）
def a(n):
    a = 0
    while True:
        if (a < n): 
            temp = a
            a += 1
            yield temp
        else:
            break

# 生成器返回的是迭代器
f = a(3) 
while True:
    try:
        print(next(f))
    except StopIteration:
        print("迭代完成")
        break
# 上面语句的运行结果如下
# 0
# 1
# 2
# 迭代完成