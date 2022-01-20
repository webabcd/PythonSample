# pandas - Series 基础
#   Series - 带索引的一维表
#   DataFrame - 带索引的二维表
#
# 注 pandas 是基于 numpy 的

import pandas as pd

# 列表转 Series
a = ['a','b','c','d','e']
b = pd.Series(a)
print(b)
'''
第一列是索引列（不指定索引的话，默认就是从 0 开始的序列），第二列是数据列
0    a
1    b
2    c
3    d
4    e
'''

# 实例化 Series（指定索引列，数据列）
c = pd.Series(index=['zhao', 'qian', 'sun', 'li', 'zhou'], data=[40, 25, 22, 28, 28])
print(c)
'''
第一列是索引列，第二列是数据列
zhao    40  
qian    25  
sun     22  
li      28  
zhou    28    
'''

# 实例化 Series（指定索引列和索引列的数据类型，数据列和数据列的数据类型）
c = pd.Series(index=pd.Index(['zhao', 'qian', 'sun', 'li', 'zhou'], dtype=object), data=[40, 25, 22, 28, 28], dtype=int)
print(c)
'''
第一列是索引列，第二列是数据列
zhao    40  
qian    25  
sun     22  
li      28  
zhou    28    
'''

# 获取 Series 的索引列的数据和数据列的数据
print(c.values) # [40 25 22 28 28]
print(list(c.values)) # [40, 25, 22, 28, 28]
print(c.index) # Index(['zhao', 'qian', 'sun', 'li', 'zhou'], dtype='object')
print(list(c.index)) # ['zhao', 'qian', 'sun', 'li', 'zhou']

# 获取指定索引的数据
print(c.get('zhao')) # 40
print(c['zhao']) # 40
print(c[0]) # 40
print(c[0:3])
'''
zhao    40
qian    25
sun     22
'''
print(c[[0,3]])
'''
zhao    40
li      28
'''
print(c[c<28])
'''
qian    25
sun     22
'''

# 去重
print(c.unique()) # [40 25 22 28]

# 统计不同数据出现的次数
print(c.value_counts())
'''
28    2
40    1
25    1
22    1
'''

# 判断数据是否包含指定的值
print(c.isin([28,40]))
'''
zhao     True
qian    False
sun     False
li       True
zhou     True
'''
# 取出包含指定值的数据
print(c[c.isin([28,40])])
'''
zhao    40
li      28
zhou    28
'''

# 判断数据是否不包含指定的值
print(~c.isin([28,40]))
'''
zhao    False
qian     True
sun      True
li      False
zhou    False
'''
# 取出不包含指定值的数据
print(c[~c.isin([28,40])])
'''
qian    25
sun     22
'''

# 判断数据是否包含指定范围的值
print(c.isin(c[c<26]))
'''
zhao    False
qian     True
sun      True
li      False
zhou    False
'''
# 取出包含指定范围值的数据
print(c[c.isin(c[c<26])])
'''
qian    25
sun     22
'''

# 对所有数据做 +10 的操作
c += 10
print(c)
'''
zhao    50
qian    35
sun     32
li      38
zhou    38
'''