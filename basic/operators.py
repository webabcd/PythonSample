# python 运算符

# 算术运算符 + - * / % ** //
# a ** b 返回 a 的 b 次幂
print(2 ** 8) # 256
# a // b 返回 a 除以 b 的结果，如果结果不是整数则向下取整
print(5 // 2) # 2
print(-5 // 2) # -3

# 比较运算符 == != > < >= <=

# 赋值运算符 = += -= *= /= %= **= //=

# 位运算符 & | ^ ~ << >>
# & 与，两位都为 1 则结果为 1
# | 或，两位有一个为 1 则结果为 1
# ^ 异或，两位不同则结果为 1
# ~ 取反，0 变为 1，1 变为 0
# << 左移，左移指定的位数，高位丢弃，低位补 0
# >> 右移，右移指定的位数，高位补 0（不一定？），低位丢弃

# 逻辑运算符 and, or, not
print(True and False) # False
print(True or False) # True
print(not False) # True

# 成员运算符 in, not in
list = [1, 2, 3, 4, 5]
print(1 in list) # True
print(1 not in list) # False

# 身份运算符（identity operator） is, is not
# is 和 is not 用于判断两个变量的指针地址是否相同，== 和 != 用于判断两个变量引用的值是否相同
# 对于不可变类型（Number, String, Tuple）来说，如果他们的值相同，则他们的指针相同
a = "abc"
b = "abc"
print(id(a), id(b), a == b, a is b, a is not b) # 1587785078192 1587785078192 True True False
b = "xyz"
print(id(a), id(b), a == b, a is b, a is not b) # 1587785078192 1587785086000 False False True
# 对于可变类型（List, Set, Dictionary）来说，他们的值相同，并不意味着他们的指针相同
c = [1, 2, 3]
d = [1, 2, 3]
print(id(c), id(d), c == d, c is d, c is not d) # 1587785132928 1587785135808 True False True
# is, is not 也常用于判断某数据是否是指定的类型
print(type(3.14) is float) # True

# 通过 for 语句实现类似三目运算符 ? : 的效果（注：python 不支持三目运算符 ? :）
print("abc" if False else "xyz") # xyz