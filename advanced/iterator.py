# iterator 迭代器（迭代器只能往下迭代，不能返回去）

a = [1, 2, 3]
# 可遍历的对象都可以通过如下方式转换为迭代器
b = iter(a) # 通过 iter() 将指定的对象转换为迭代器
while True:
    try:
        print(next(b)) # 通过 next() 迭代
    except StopIteration:
        print("迭代完成")
        break
# 上面语句的运行结果如下
# 1
# 2
# 3
# 迭代完成


# 定义一个支持被转换为迭代器的类（要实现 __iter__() 函数和 __next__() 函数）
class Class1:
    def __iter__(self):
        self.a = 0
        return self
    def __next__(self):
        if self.a < 3:
            temp = self.a
            self.a += 1
            return temp
        else:
            raise StopIteration
c = Class1()
# 如果对象支持被转换为迭代器，就可以通过 iter() 将其转换为迭代器
d = iter(c)
while True:
    try:
        print(next(d))
    except StopIteration:
        print("迭代完成")
        break
# 上面语句的运行结果如下
# 0
# 1
# 2
# 迭代完成