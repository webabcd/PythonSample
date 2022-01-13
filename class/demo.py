# 从 class1.py 文件中导入 Class1 类
from class1 import Class1
# 从 myClass.py 文件中导入 MyClass 类
from myClass import MyClass

# 类的使用
a = Class1("webabcd", 30)
a.country = "china"
a.age = 40
print(a.toString()) # id:0001, name:webabcd, age:40, country:china
# 演示如何使用 [] 方式的操作（相关逻辑请看 Class1 类的代码）
a["a"] = "abc"
print(a["a"]) # myvalue_abc

# 类的使用
b = MyClass("webabcd", 40, 100)
b.country = "china"
print(b.toString()) # name:webabcd, age:40, level:100
# 调用父类的函数
print(super(MyClass, b).toString()) # id:0001, name:webabcd, age:40, country:china
