# python 字符串类型

# 定义字符串可以用 ""
a = "web"
# 定义字符串也可以用 ''
b = 'abcd'
# 字符串相加
c = a + b
print(c) # webabcd
# 取第 1 个字符
print(c[0]) # w
# 取最后一个字符
print(c[-1]) # d
# 取第 2 个字符到最后一个字符
print(c[1:]) # ebabcd
# 取第 1 个字符到倒数第 2 个字符（注：范围不包含冒号右边的值）
print(c[:-1]) #webabc
# 取第 2 个字符到第 4 个字符（注：范围包含冒号左边的值，但是不包含冒号右边的值）
print(c[1:4]) # eba
# 取第 2 个字符到倒数第 3 个字符（注：范围包含冒号左边的值，但是不包含冒号右边的值）
print(c[1:-2]) # ebab
# 像下面这样修改字符串是不允许的，因为字符串是不可变类型
# c[0] = "x"

# 通过 * 可以指定字符串重复的次数
print(c * 2) # webabcdwebabcd
# in 是否包含
print("ab" in c) # True
# not in 是否不包含
print("ab" not in c) # False
# 字符串是可遍历的
for x in "abc":
    print(x)

# 转义符 \ 的用法和其他语言差不多
# \x 就是将十六进制字符串转为对应的 ascii 字符
d = "\"\x77\x65\x62\""
print(d) # "web"
# 通过 r 取消转义符的功能
e = r"\"\x77\x65\x62\""
print(e) # \"\x77\x65\x62\"
# \u 就是将 unicode 编码转为对应的字符
print("\u738b") # 王

# 定义字符串时如果需要换行，可以像下面这样通过 \n 实现
f = "111\n222\n333"
# 定义字符串时如果需要换行，也可以像下面这样通过 '''''' 或 """""" 实现
g = '''111
222
333'''
print(f) # f 和 g 的输出结果是一样的
print(g) # f 和 g 的输出结果是一样的

# 通过 % 格式化字符串
h = "webabcd"
i = 40
j = "我是 %s, 今年 %d 岁" % (h, i)
print(j) # 我是 webabcd, 今年 40 岁
# 保留 2 位小数
print("%.2f" % 3.141592) # 3.14

# 通过 f 格式化字符串
k = f"我是 {h}, 今年 {i} 岁"
print(k) # 我是 webabcd, 今年 40 岁

# 通过 format() 格式化字符串
print('{}, {}'.format('web', 'abcd')) # web, abcd
print('{1}, {0}, {age}'.format('abcd', 'web', age=40)) # web, abcd, 40
print('{0:.2f}'.format(3.1415926)) # 3.14