# python 集合类型（集合内元素可以是不同数据类型的，不可以重复的，无顺序的）

# 定义一个集合
# 注：因为集合是无序的，所以后续通过 print() 打印的集合的值每次运行都可能是不一样的
a = {"a", "b", 1, 2}
print(a) # {1, 'b', 2, 'a'}

# 通过 add() 添加元素
a.add(3) 
a.add(3)
a.add(3)
print(a) # {1, 'b', 3, 2, 'a'}
# 通过 update() 添加元素（参数值必须是可迭代的，update() 会将其迭代后的元素添加到集合）
a.update(["c", "d"])
print(a) # {1, 'b', 3, 2, 'c', 'd', 'a'}
# 通过 remove() 删除指定的元素
a.remove("d")
print(a) # {1, 'b', 3, 2, 'c', 'a'}
# 通过 pop() 随机删除一个元素
a.pop()
print(a) # {'b', 3, 2, 'c', 'a'}

# 通过 in, not in 判断集合中是否有指定的元素
print(1 in a, 1 not in a)
# 集合是可迭代的
for x in a:
    print(x)

b = {1, 2, 3}
c = {1, 2, 4}
# 获取 b 中有而 c 中没有的元素
print(b - c) # {3}
# 获取 b 中和 c 中的所有元素
print(b | c) # {1, 2, 3, 4}
# 获取 b 和 c 同时包含的元素
print(b & c) # {1, 2}
# 获取 b 和 c 不同时包含的元素
print(b ^ c) # {3, 4}

# 将字符串转换为集合
print(set("webabcd")) # {'d', 'b', 'c', 'e', 'w', 'a'}
# 定义一个空集合（注：{} 是空字典）
print(set()) # set()