# 从 class1.py 文件中导入 Class1 类
from class1 import Class1
# 从 class3.py 文件中导入 Class3 类
from class3 import Class3
# 从 class4.py 文件中导入 Class4 类
from class4 import Class4

# 类的使用
a = Class1("webabcd", 30)
a.country = "china"
a.age = 40
print(a.toString()) # id:0001, name:webabcd, age:40, country:china
# 演示如何使用 [] 方式的操作（相关逻辑请看 Class1 类的代码）
a["a"] = "abc"
print(a["a"]) # myvalue_abc
# 演示如何实现类似静态属性的效果
Class1.country = "PRC"
print(Class1.country)

# 类的使用
b = Class3("webabcd", 40, 100)
b.country = "china"
print(b.toString()) # name:webabcd, age:40, level:100
# 调用基类的函数
print(super(Class3, b).toString()) # id:0001, name:webabcd, age:40, country:china

# 演示 with 的用法
# 实例化时返回的对象是由类的 __enter__ 返回的
# 退出 with 时会调用对象的 __exit__
with Class4() as c:   
    c.hello("webabcd")
'''
enter
hello:webabcd
exit
'''