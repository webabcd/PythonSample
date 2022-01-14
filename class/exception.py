# 定义自定义异常类（需要继承 Exception）
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    # 抛出自定义异常
    raise MyError("异常信息")
except MyError as ex:
    print(ex)