# python 基础
# python 是脚本语言（即不需要编译，而是通过解释器解释运行）
# python 的变量都是指针，引用数据通过 GC 清理（没有被引用的数据会被清理）
#        不可变类型有 Number数字, String字符串, Bytes字节，Tuple元组（指针不变，则值肯定无法改变；若要修改值，则指针必会改变）
#        可变类型有 List列表, Set集合, Dictionary字典（指针不变，值可以发生变化）
# python 文档 https://docs.python.org/3/
#
#
# python 安装
# 1、https://code.visualstudio.com/ 下载并安装 visual studio code
# 2、在 visual studio code 中安装 Python 扩展
# 3、https://www.python.org/downloads/windows/ 下载并安装 Python
# 4、安装第三方包就类似这么安装 pip install openpyxl


# 单行注释

'''
多行注释
多行注释
多行注释
这里实际上是代表字符串，但当其没有被赋值给任何变量，也没有被当作函数的参数，则可以将其视为注释
'''

"""
多行注释
多行注释
多行注释
这里实际上是代表字符串，但当其没有被赋值给任何变量，也没有被当作函数的参数，则可以将其视为注释
"""

# 通过缩进表示代码块，而不是 {}
if True:
    print("aaa")
else:
    print("bbb")

# 代码块缩进的空格数是可变的，但是同一代码块中的缩进空格数必须是相同的
if False:
    print("ccc")
else:
  print("ddd")
    # 下面这句去掉注释符就会报错，因为在同一代码块中缩进空格数不一致
    # print("eee") 

# 可以通过 + \ 实现多行语
a = "111" + \
    "222" + \
    "333"
print(a)

# 在 [] 或 {} 或 () 中的多行语句，是不需要 + \ 的
b = ['1', '2', '3', 
    '4', '5']
print(b)

# 在同一行中使用多条语句（用 ; 分隔）
c = "abc"; d = "xyz"
print(c)
print(d)

# 同时为多个变量赋值
e = f = "123"
print(e)
print(f)

# 同时为多个变量赋不同的值（允许通过 \ 换行）
g, h, i = 1, \
    "a", True
print(g) # 1
print(h) # a
print(i) # True

# 请注意 python 的变量都是指针，通过 del 删除的是变量（指针），而不是引用的数据（引用的数据是通过 GC 清理的）
j = 123
k = j
l = k
print(j)
print(k)
# 删除 j 变量和 k 变量
del j, k
# j 变量和 k 变量被删除，但是他们引用的对象不会被删除，所以下面这句会输出 123
print(l)
# 下面这句会报错 name 'j' is not defined
# print(j) 
# 下面这句会报错 name 'k' is not defined
# print(k)

# 请注意 python 的变量都是指针，对变量重新赋值则意味着使用新的指针地址
m = 123
# id() 用于获取变量的指针地址，我运行时此值为 1371834486832
print(id(m))
m = 456
# id() 用于获取变量的指针地址，我运行时此值为 1371881654544（可以发现指针发生了变化）
print(id(m))
n = 456
# id() 用于获取变量的指针地址，我运行时此值为 1371881654544（可以发现对于不可变类型来说，如果他们的值相同，则他们的指针相同）
print(id(n))