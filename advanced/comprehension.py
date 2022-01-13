# comprehension 推导式
# 一种简单的“把一个或多个列表或集合或字典通过指定的规则生成一个新的列表或集合或字典”的方法

a = [1, 2, 3, 4, 5]
b = {1, 2, 3, 4, 5}
c = {"k1":1, "k2":2, "k3":3, "k4":4, "k5":5}

# 取出列表 a 中的偶数，并生成一个新的列表
d = [x for x in a if x % 2 == 0]
# 取出集合 b 中的偶数，并生成一个新的集合
e = {x for x in b if x % 2 == 0}
# 取出字典 c 中的 value 为偶数的 k/v，并生成一个新的字典
f = {k:v for k,v in c.items() if v % 2 == 0}
print(d) # [2, 4]
print(e) # {2, 4}
print(f) # {'k2': 2, 'k4': 4}

# 通过嵌套循环生成一个元组列表
g = [(x,y) for x in range(2) for y in range(3)] 
print(g) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

# 通过嵌套循环生成一个元组列表，同时指定规则
h = [(x,y) for x in range(2) if x % 2 == 0 for y in range(3) if y % 2 == 0] 
print(h) # [(0, 0), (0, 2)]

# 通过嵌套循环生成一个字典
i = {f"k{x}_{y}":f"v{x}_{y}" for x in range(2) for y in range(3)}
print(i) # {'k0_0': 'v0_0', 'k0_1': 'v0_1', 'k0_2': 'v0_2', 'k1_0': 'v1_0', 'k1_1': 'v1_1', 'k1_2': 'v1_2'}

# 通过嵌套推导式生成一个二维列表
j = [[0 for col in range(2)] for row in range(3)] # 推导式也是可以嵌套的
print(j) # [[0, 0], [0, 0], [0, 0]]

# 可以在推导式中使用函数
def plus(a, b):
    return a + b
k = [plus(x,y) for x in range(2) for y in range(3)] 
print(k) # [0, 1, 2, 1, 2, 3]