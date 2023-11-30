# python 语句

import random

# if/elif/else 语句
a = random.randint(0,2)
if a == 0:
    print("a==0")
elif a == 1:
    print("a==1")
else:
    print("a==2")

# if 会强制转换条件，非空字符串会转为 True
if 'abc':
    print("if 'abc':")

# if 会强制转换条件，空字符串会转为 False
if not '':
    print("if not '':")

# value1 if condtion else value2
print("奇数" if 1 % 2 else "偶数") # 奇数
print("奇数" if 2 % 2 else "偶数") # 偶数

# 其他语言一般通过 {} 或 ; 实现空语句
# python 可以通过 pass 实现空语句
if True:
    pass # 这里如果不想写任何代码的话，只空着是不行的，需要加上一个空语句，可以是 pass
# python 也可以通过 ... 实现空语句
if True:
    ... # 这里如果不想写任何代码的话，只空着是不行的，需要加上一个空语句，可以是 ...

# while 语句（支持 break, continue）
# 退出循环后会走到 else（不需要的话可以不写 else）
b = 0
while b < 10:
    print("while b", b)
    b +=2
else:
    print("else b", b)

# for 语句（支持 break, continue）
# 退出循环后会走到 else（不需要的话可以不写 else）
# 遍历 0 - 4 之间的整数
for c in range(5):
    print("while c", c)
else:
    print("else c", c)

# 遍历集合中的元素
for v in ['x', 'y', 'z']:
    print(v)
# 上面语句的运行结果如下
# x
# y
# z

# 如何在遍历时拿到值和值对应的索引位置？
for i, v in enumerate(['x', 'y', 'z']): # v 是遍历出的值，i 是其对应的索引位置
    print(i, v)
# 上面语句的运行结果如下
# 0 x
# 1 y
# 2 z

# 通过 for 语句构造一个 list
print([f'{i} {v}' for i, v in enumerate(['x', 'y', 'z'])]) # ['0 x', '1 y', '2 z']

# 通过 for 语句实现类似三目运算符 ? : 的效果（注：python 不支持三目运算符 ? :）
print("abc" if False else "xyz") # xyz

# try/except/else/finally 语句
try:
    raise Exception("异常信息") # 抛出一个异常
except Exception as ex: # 捕获指定类型的异常
    print(ex)
except: # 捕获之前的 except 没有捕获到的异常
    raise # 抛出当前异常
else:
    print("无异常时执行")
finally:
    print("无论发生什么都会执行")

# if/while/for/try 是不会引入新的作用域的（即这些语句内定义的变量，在外部也是可以访问的）
# class/function 是会引入新的作用域的（参见 function.py）
if True:
    d = "abc"
print(d) # abc