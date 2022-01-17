# 文件写入和读取

# 文件路径
path = r'd:\temp.txt'

# 写文件
fw = open(path, 'w')
fw.write('hello webabcd')
fw.close()

# 读文件
fr = open(path, 'r')
print(fr.read())
fr.close()

# with 语句，会在代码块执行完后自动调用 close()
# 写文件
with open(path, 'w') as fw2:
    fw2.write('hello webabcd2')
    # 执行完后会自动调用 fw2.close()

# with 语句，会在代码块执行完后自动调用 close()
# 读文件
with open(path, 'r') as fr2:
    print(fr2.read())
    # 执行完后会自动调用 fr2.close()