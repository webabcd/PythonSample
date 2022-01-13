# python 语句

import random

# if/elif/else 语句
a = random.randint(0,2)
if a == 0:
    print("a==0")
elif a == 1:
    print("a==1")
else:
    print("a==2")

# value1 if condtion else value2
print("奇数" if 1 % 2 else "偶数") # 奇数
print("奇数" if 2 % 2 else "偶数") # 偶数

# 其他语言一般通过 {} 或 ; 实现空语句
# python 是通过 pass 实现空语句的
if True:
    pass # 这里如果不想写任何代码的话，只空着是不行的，需要加上一个空语句，即 pass

# while 语句（支持 break, continue）
# 退出循环后会走到 else（不需要的话可以不写 else）
b = 0
while b < 10:
    print("while b", b)
    b +=2
else:
    print("else b", b)

# for 语句（支持 break, continue）
# 退出循环后会走到 else（不需要的话可以不写 else）
for c in range(5):
    print("while c", c)
else:
    print("else c", c)