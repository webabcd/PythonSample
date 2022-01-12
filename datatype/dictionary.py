# python 字典类型（key 不可重复，value 可重复；key 必须是不可变变量，value 可以是任意变量）

# 定义一个字典
a = {"k1":"v1", 2:100}
print(a) # {'k1': 'v1', 2: 100}

# 获取指定 key 的 value
print(a["k1"]) # v1
print(a[2]) # 100

# 添加或修改（有则更新无则添加）指定 key 的 value
a["k1"] = "v111"
print(a["k1"]) # v111

# 添加活修改（有则更新无则添加）指定 key 的 value
a["k2"] = "v222"
print(a["k2"]) # v222

# 删除指定 key
del a["k2"]
print(a) # {'k1': 'v111', 2: 100}

# 迭代字典的 key
for x in a.keys():
  print(x)
# 迭代字典的 value
for x in a.values():
  print(x)
# 迭代字典的 key/value
for k, v in a.items():
  print(k, v)
# 直接迭代字典，实际迭代出的是 key
for x in a:
  print(x)

# 定义一个空字典
print(dict()) # {}
# 定义一个空字典
print({}) # {}


