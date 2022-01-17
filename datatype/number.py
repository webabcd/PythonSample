# python 数字类型

a = 1       # 整型
b = 3.14    # 浮点型
c = True    # 布尔型，其实是整型（True 是 1，False 是 0）
d = a + b + c
print(a, b, c, d) # 1 3.14 True 5.140000000000001

e = 30          # 十进制
f = 0o36        # 八进制
g = 0x1E        # 十六进制
h = 0b00011110  # 二进制
print(e, f, g, h) # 30 30 30 30

# 通过 complex() 定义数学中的复数（由实数部分和虚数部分组成）
i = complex(3.14)       # 实数部分 3.14，虚数部分 0
j = complex(3.14, 1.2)  # 实数部分 3.14，虚数部分 1.2
k = i + j
print(i, j, k) # (3.14+0j) (3.14+1.2j) (6.28+1.2j)
# real - 取复数的实数部分
# imag - 取复数的虚数部分
print(k.real, k.imag) # 6.28 1.2

# 格式化浮点型数据
print(format(3.1415926, '.2f'))