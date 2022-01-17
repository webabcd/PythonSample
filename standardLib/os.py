# 通过 import os 实现目录和文件管理

import os

# 删除指定目录下的目录和文件（不包括指定目录本身）
def deleteDir(path):
    # topdown=False 的意思是从下往上遍历（默认是从上往下遍历）
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            # 删除文件
            os.remove(os.path.join(root, name))
        for name in dirs:
            # 删除空目录（如果目录非空，则会抛出一个 OSError 异常）
            os.rmdir(os.path.join(root, name))
            

path = r'd:\temp'

# 判断路径是否存在
if not os.path.exists(path):
    # 创建目录
    os.mkdir(path)

    # 创建目录（如果当前目录的父辈目录们不存在，则自动创建它们）
    os.makedirs(os.path.join(path, "dir1", "dir1_1"))
    os.mkdir(os.path.join(path, "dir1", "dir1_2"))
    os.mkdir(os.path.join(path, "dir1", "dir1_3"))
    with open(os.path.join(path, "dir1", "dir1_1", "dir1_1_f1.txt"), 'w'): pass
    with open(os.path.join(path, "dir1", "dir1_1", "dir1_1_f2.txt"), 'w'): pass
    with open(os.path.join(path, "dir1", "dir1_1", "dir1_1_f3.txt"), 'w'): pass

    os.makedirs(os.path.join(path, "dir2", "dir2_1"))
    with open(os.path.join(path, "dir2", "dir2_1", "dir2_1_f1.txt"), 'w'): pass

# 删除指定目录下的目录和文件（不包括指定目录本身）
deleteDir(os.path.join(path, "dir2"))

# 判断路径是目录还是文件
print(path + " isdir:", os.path.isdir(path)) # d:\temp isdir: True
print(path + " isfile:", os.path.isfile(path)) # d:\temp isfile: False

# 遍历指定目录下的目录和文件
for home, dirs, files in os.walk(path):
    print(home)
    for dirName in dirs:
        print("--" + dirName)
    for fileName in files:
        print("--" + fileName)
'''
上面语句的运行结果为
d:\temp
--dir1
--dir2
d:\temp\dir1
--dir1_1
--dir1_2
--dir1_3
d:\temp\dir1\dir1_1
--dir1_1_f1.txt
--dir1_1_f2.txt
--dir1_1_f3.txt
d:\temp\dir1\dir1_2
d:\temp\dir1\dir1_3
d:\temp\dir2
'''