# python 字节类型

# 定义 5 个空字节
a = bytes(5)
print(a, type(a)) # b'\x00\x00\x00\x00\x00' <class 'bytes'>

# 下面是几种定义字节的方法，结果都是 b'abc'
b = bytes([97, 98, 99])
print(b) # b'abc'
c = b'\x61\x62\x63' # 这里 b 的意思就是将其后的字符串定义为字节类型
print(c) # b'abc'
d = bytes("abc", "utf-8")
print(d) # b'abc'
e = bytes.fromhex('61 62 63')
print(e) # b'abc'

# 字节是可迭代的，迭代出的数据是整型
print(e[0]) # 97
for x in e:
    print(x) # 迭代出的数据分别是 97 98 99

# 将字节类型转换为十六进制字符串
print(e.hex()) # 616263