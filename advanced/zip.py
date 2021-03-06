# zip - 将多个可迭代对象压缩为一个可迭代对象，将一个可迭代对象解压缩为多个可迭代对象

a = [1, 2, 3]
b = [4, 5, 6]


# 将多个可迭代对象压缩为一个可迭代对象（把多个可迭代对象的相同索引位置的数据取出来，并组成新的可迭代对象的元素）
c = zip(a, b) 
d = list(c)
print(c) # 一个 zip 对象
print(d) # [(1, 4), (2, 5), (3, 6)]


# 将一个可迭代对象解压缩为多个可迭代对象（把一个可迭代对象的每个元素的相同索引位置的数据取出来，并分别组成多个可迭代对象）
e, f = zip(*[[1, 4], [2, 5], [3, 6]])      
print(e) # (1, 2, 3)
print(f) # (4, 5, 6)

g, h = zip(*([1, 4], [2, 5], [3, 6]))      
print(g) # (1, 2, 3)
print(h) # (4, 5, 6)

i, j = zip(*[(1, 4), (2, 5), (3, 6)])      
print(i) # (1, 2, 3)
print(j) # (4, 5, 6)