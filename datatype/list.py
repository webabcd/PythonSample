# python 列表类型（列表内元素可以是不同数据类型的，可以重复的，有顺序的）

# 定义一个列表
a = [1, "b", "c", "d", True]
print(a) # [1, 'b', 'c', 'd', True]

# 修改列表的第 1 个元素
a[0] = "a"
# 修改列表的最后一个元素
a[-1] = "f"
# 在列表的第 5 个元素之前插入指定的元素
a.insert(4, "e")
# 在列表的结尾插入指定的元素
a.append("g")
# 删除列表的最后一个元素
del a[-1]
print(a) # ['a', 'b', 'c', 'd', 'e', 'f']
# 另外，删除列表中的元素也可以通过如下方式实现
# a[0:3] = []

# 取第 1 个元素
print(a[0]) # a
# 取最后一个元素
print(a[-1]) # f
# 取第 2 个元素到最后一个元素
print(a[1:]) # ['b', 'c', 'd', 'e', 'f']
# 取第 1 个元素到倒数第 3 个元素（注：范围不包含冒号右边的值）
print(a[:-2]) # ['a', 'b', 'c', 'd']
# 取第 1 个元素到第 2 个元素（注：范围包含冒号左边的值，但是不包含冒号右边的值）
print(a[0:2]) # ['a', 'b']
# 取第 1 个元素到第 5 个元素，且步长为 2（第 2 个冒号右边的值用于定义步长）
print(a[0:5:2]) # ['a', 'c', 'e']
# 通过如下方式可以对数组做反向排序（第 2 个冒号右边的值用于定义步长）
print(a[-1::-1]) # ['f', 'e', 'd', 'c', 'b', 'a']

# 列表内元素可以是不同数据类型的，可以重复的，有顺序的
# 列表之间可以相加，列表可以乘以一个整数
b = [1, 2]
c = ["a", "b"]
d = (b + c) * 2
print(d) # [1, 2, 'a', 'b', 1, 2, 'a', 'b']
# 通过 in, not in 判断列表中是否有指定的元素
print(1 in d, 1 not in d) # True False
# 列表是可遍历的
for x in d:
    print(x)

# 将字符串转换为列表
print(list("webabcd")) # ['w', 'e', 'b', 'a', 'b', 'c', 'd']
# 将列表转换为字符串
print(",".join(list("webabcd"))) # w,e,b,a,b,c,d
# 定义一个空列表
print(list()) # []
# 定义一个空列表
print([]) # []


# 如何在遍历时拿到值对应的索引位置？
for i, v in enumerate(['x', 'y', 'z']): # v 是遍历出的值，i 是其对应的索引位置
    print(i, v)
# 上面语句的运行结果如下
# 0 x
# 1 y
# 2 z

# 如何同时遍历 2 个列表？
e = ['a', 'b', 'c']
f = ['x', 'y', 'z']
for x, y in zip(e, f):
    print(x, y)
# 上面语句的运行结果如下
# a x
# b y
# c z

# 如果列表中的是元组，那么可以这么遍历
g = [('a', 'b', 'c'), ('x', 'y', 'z')]
for i, j, k in g:
    print(i, j, k)
# 上面语句的运行结果如下
# a b c
# x y z

# filter 的用法
l = range(10)
m = list(filter(lambda x: x < 3, l))
print(m) # [0, 1, 2]

# map 的用法
n = [{"k":"a"},{"k":"b"},{"k":"c"}]
o = list(map(lambda p: p["k"], n))
print(o) # ['a', 'b', 'c']

# reduce 的用法
from functools import reduce
p = range(101)
q = reduce(lambda x, y: x + y, p)
print(q) #5050