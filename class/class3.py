# 从 class1.py 文件中导入 Class1 类
from class1 import Class1
# 从 class2.py 文件中导入 Class2 类
from class2 import Class2

# 类的继承，支持多继承
class Class3(Class1, Class2):

    def __init__(self, name, age, level):
        # 调用基类的构造函数
        Class1.__init__(self, name, age)
        Class2.__init__(self, level)

    # 重写基类的函数
    def toString(self):
        # super() - 用于调用基类的函数
        return super().toString() + " - " + f"name:{self.name}, age:{self.age}, level:{self.level}"


'''
注：
如果多个基类有相同的函数的话，那么你调用的时候调用的是哪个呢？
调用的是前面的那个类的函数
比如 class MyClass(a, b, c):
a, b, c 中有相同的函数，那么你调用会是 a 中的函数
'''