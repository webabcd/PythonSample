def a():
    print("module1_a")

def b():
    print("module1_b")

if __name__ == '__main__': # 程序是在该模块自身运行的
   print('module1_没人引用我，我是主模块')
else: # 程序是在其它地方运行的，那个地方引用了这个模块
   print('module1_我被引用了，我不是主模块')