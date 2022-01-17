# 通过 import time, datetime 实现日期和时间

import time, datetime

# datetime 是对 time 的封装，用起来比较简单

# 获取当前本地时间
print(datetime.datetime.now()) # 2022-01-17 16:22:09.279780

# 获取当前 utc-0 的时间
print(datetime.datetime.utcnow()) # 2022-01-17 08:22:09.279780

# 通过指定年月日时分秒构造 datetime 对象
a = datetime.datetime(2012, 12, 21, 10, 11, 12, 123456)
print(a) # 2012-12-21 10:11:12.123456

# 格式化 datetime 对象
b = a.strftime('%Y-%m-%d %H:%M:%S.%f')
print(b) # 2012-12-21 10:11:12.123456

# 字符串转 datetime 对象
c = datetime.datetime.strptime("2012-12-21 10:11:12.123456", '%Y-%m-%d %H:%M:%S.%f')
print(c) # 2012-12-21 10:11:12.123456


# 距 1970.1.1 的秒数，是一个浮点型
print(time.time()) # 1642406929.1009686

# 获取当前本地时间，是一个 struct_time 对象
print(time.localtime()) # time.struct_time(tm_year=2022, tm_mon=1, tm_mday=17, tm_hour=16, tm_min=8, tm_sec=49, tm_wday=0, tm_yday=17, tm_isdst=0)

# 获取当前 GMT 时间，是一个 struct_time 对象
print(time.gmtime()) # time.struct_time(tm_year=2022, tm_mon=1, tm_mday=17, tm_hour=8, tm_min=8, tm_sec=49, tm_wday=0, tm_yday=17, tm_isdst=0)

# 将指定的“距 1970.1.1 的秒数”转为本地时间，是一个 struct_time 对象
print(time.localtime(1600000000)) # time.struct_time(tm_year=2020, tm_mon=9, tm_mday=13, tm_hour=20, tm_min=26, tm_sec=40, tm_wday=6, tm_yday=257, tm_isdst=0)

# 获取 struct_time 对象中的数据
print(time.localtime().tm_year) # 2022

# 格式化 struct_time 对象
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) # 2022-01-17 16:25:42

# 在当前线程阻塞指定的秒数
time.sleep(0.1)

# 获取设备开机到现在经过的秒数
print(time.perf_counter())

