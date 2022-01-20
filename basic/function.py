# python 函数

# 无参数，无返回值的函数
def a():
    # 如果需要在函数执行完之前退出函数，那么就直接 return 即可
    # return
    print("aaa")
# 无返回值函数返回的数据是 None，其类型为 <class 'NoneType'>
print(a(), type(a())) # None <class 'NoneType'>

# 无参数，有返回值的函数
def b():
    return "bbb"
print(b())

# 有参数，有返回值的函数
def c(a, b):
    if (b == 0):
        return None # None 的作用相当于其他语言的 null
    return a / b
print(c(1, 2)) # 0.5
print(c(1, 0), c(1, 0) == None, type(None)) # None True <class 'NoneType'>

# 支持在定义函数的时候为函数指定默认值
def d(a, b, c = "ccc"):
    return a + b + c
print(d("1", "2"))
print(d("1", "2", "3"))
# 调用函数的时候可以指定参数名称，这样就可以不按参数顺序传参了
print(d(c="3", b="2", a="1"))

# 下面这个函数有 4 个参数
# / 不是参数，传参时对于 / 左面的参数必须不能指定参数名称
# * 不是参数，传参时对于 * 右面的参数必须指定参数名称
def f(a, /, b, *, c, d):
    print(a + b + c + d)
# 下面这么调用会报错，因为传参时对于 * 右面的参数必须指定参数名称
# f(1, 2, 3, 4)
# 下面这么调用会报错，因为传参时对于 / 左面的参数必须不能指定参数名称
# f(a=1, b=2, c=3, d=4)
f(1, 2, c=3, d=4)

# 不定长参数（一个星号代表不定长参数会以元组的形式传入）
def f(a, *b):
   print(a, b)
f(1) # 1 ()
f(1, 2, 3) # 1 (2, 3)

# 不定长参数（两个星号代表不定长参数会以字典的形式传入）
def g(a, **b):
   print(a, b)
g(1) # 1 {}
g(2, k1="v1", k2="v2") # 2 {'k1': 'v1', 'k2': 'v2'}

# 匿名函数（即不用 def 定义函数，而是通过 lambda 表达式实现）
h = lambda x, y: x * y
print(h(2, 3))

# python 都是引用类型，传参传的都是指针，那么在函数内修改参数，是否会影响函数外的对应的变量？
def i(a, b, c):
    a = 100             # 指针变了，所以此参数的变化不会影响函数外的对应的变量
    b = [1, 2, 3, 4]    # 指针变了，所以此参数的变化不会影响函数外的对应的变量
    c.append(4)         # 指针没变，所以此参数的变化会影响函数外的对应的变量
i_a = 0
i_b = [1, 2, 3]
i_c = [1, 2, 3]
print(i_a, i_b, i_c) # 0 [1, 2, 3] [1, 2, 3]
i(i_a, i_b, i_c)
print(i_a, i_b, i_c) # 0 [1, 2, 3] [1, 2, 3, 4]


# 函数的内部变量和外部变量是有作用域的概念的
num = 1 # 这个是全局变量
def fun1():
    global num # 需要使用 global 才能修改全局变量的指针
    print(num) # 1
    num = 123
    print(num) # 123
fun1()
print(num) # 123

def fun2():
    num = 10 # 这个是 fun3() 函数的外层非全局变量
    def fun3():
        nonlocal num  # 需要使用 nonlocal 才能修改外层非全局变量的指针
        print(num) # 10
        num = 100
        print(num) # 100
    fun3()
    print(num) # 100
fun2()