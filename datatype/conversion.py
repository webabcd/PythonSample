# python 数据类型转换

a = 1
b = 3.14
# 隐式转换，a 会被转换为 float 类型
c = a + b
print(c, type(c)) # 4.140000000000001 <class 'float'>

# 这个无法隐式转换的，会报错 can only concatenate str (not "int") to str
# print("123" + 123)
# 数字转换为字符串需要通过 str() 显示转换
print("123" + str(123)) # 123123

# 浮点型的显示转换
print(float("1")) # 1.0

# 整型的显示转换，取整数部分
print(int(1.2)) # 1
print(int(-1.2)) # -1
print(int("3")) # 3
# 注：无法像下面这样将其转换为整型，需要先将其转换为浮点型，然后再转为整型
# print(int("3.14"))

# 布尔型的显示转换
print(bool(1)) # True
print(bool(0)) # False
print(bool(-1.2)) # True

d = [1, 2, 3]
# 列表转换为集合
e = set(d) # {1, 2, 3}
print(e)
# 集合转换为列表
f = list(e) # [1, 2, 3]
print(f)
# 列表转换为元组
g = tuple(f) # (1, 2, 3)
print(g)
# 元组转换为列表
h = list(g) # [1, 2, 3]
print(h)



# python 解构

# 解构列表
i = [1, 2, 3]
i0, i1, i2 = i
print(i0) # 1
print(i1) # 2
print(i2) # 3

# 解构元组
j = (1, 2, 3)
j0, j1, j2 = j
print(j0) # 1
print(j1) # 2
print(j2) # 3

# 解构字典
k = {'name': 'webabcd', 'age': 43}
name, age = k.values()
print(name) # webabcd
print(age)  # 43

# 解构时通过 _ 忽略不需要的元素
l = [1, 2, 3, 4, 5]
l0, _, l2, _, l4 = l
print(l0) # 1
print(l2) # 3
print(l4) # 5