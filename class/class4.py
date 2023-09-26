# 用于演示 with 的用法
class Class4:
    # 通过 with 实例化时，获取到的对象是 __enter__ 返回的对象
    def __enter__(self):
        print('enter')
        return self
    # 退出 with 时会调用 __exit__
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
    def hello(self, name):
        print('hello:' + name)