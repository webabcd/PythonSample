def a():
    print("module2_a")

def b():
    print("module2_b")

if __name__ == '__main__': # 程序是在该模块自身运行的
   print('module2_没人引用我，我是主模块')
else: # 程序是在其它地方运行的，那个地方引用了这个模块
   print('module2_我被引用了，我不是主模块')