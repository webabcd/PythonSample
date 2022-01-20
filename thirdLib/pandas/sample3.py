# pandas
#   DataFrame 连接：append(), concat(), merge(), join()
#   DataFrame 去重
#   DataFrame 空值处理

import pandas as pd

data1 = {
    "name": ["zhao", "qian"],
    "age": [40, 25], 
    "city": ["beijing ", "beijing"],
    "gender": ["M", "F"]
} 
a = pd.DataFrame(data=data1) 
data2 = { 
    "name": ["qian", "sun"],
    "age": [25, 22], 
    "city": ["beijing", "shanghai"],
    "salary": [100, 150]
} 
b = pd.DataFrame(data=data2) 
print(a)
'''
   name  age      city gender
0  zhao   40  beijing       M
1  qian   25   beijing      F
'''
print(b)
'''
   name  age      city  salary
0  qian   25   beijing     100
1   sun   22  shanghai     150
'''

# append() 在 DataFrame 数据的末尾追加指定的 DataFrame 数据
print(a.append(b))
'''
   name  age      city gender  salary
0  zhao   40  beijing       M     NaN
1  qian   25   beijing      F     NaN
0  qian   25   beijing    NaN   100.0
1   sun   22  shanghai    NaN   150.0
'''


# drop_duplicates() 去重
#   subset - 根据指定的字段去重
#   keep - first保留第一条重复数据，last保留最后一条重复数据，False删除全部重复数据
#   inplace - 是否直接修改原对象
#     False 默认值，原对象不变，返回数据修改后的副本
#     True 直接修改原对象，返回值为 None
print(a.append(b).drop_duplicates(subset=['age','city'], keep='first', inplace=False))
'''
   name  age      city gender  salary
0  zhao   40  beijing       M     NaN
1  qian   25   beijing      F     NaN
1   sun   22  shanghai    NaN   150.0
'''


# concat() 拼接多个 DataFrame 数据
print(pd.concat([a, b]))
'''
   name  age      city gender  salary
0  zhao   40  beijing       M     NaN
1  qian   25   beijing      F     NaN
0  qian   25   beijing    NaN   100.0
1   sun   22  shanghai    NaN   150.0
'''

# concat() 拼接多个 DataFrame 数据
#   ignore_index=True 重建索引
print(pd.concat([a, b], ignore_index=True))
'''
   name  age      city gender  salary
0  zhao   40  beijing       M     NaN
1  qian   25   beijing      F     NaN
2  qian   25   beijing    NaN   100.0
3   sun   22  shanghai    NaN   150.0
'''

# concat() 拼接多个 DataFrame 数据
#   join='outer' 默认值，各方列名不相同的也集成到一起
#   join='inner' 各方列名不相同的就舍弃，只保留列名相同的数据
print(pd.concat([a, b], ignore_index=True, join='inner'))
'''
   name  age      city
0  zhao   40  beijing
1  qian   25   beijing
2  qian   25   beijing
3   sun   22  shanghai
'''

# concat() 拼接多个 DataFrame 数据
#   axis=1 横向拼接
print(pd.concat([a, b], axis=1))
'''
   name  age      city gender  name  age      city  salary
0  zhao   40  beijing       M  qian   25   beijing     100
1  qian   25   beijing      F   sun   22  shanghai     150
'''


# merge() 整合 2 个 DataFrame 数据
#   on='name' 以 name 列为关联关键字整 2 个 DataFrame 数据
#   如果 2 个 DataFrame 数据的关联关键字不相同，则类似这么设置 left_on="name1", right_on="name2"
print(pd.merge(a, b, on='name'))
'''
   name  age_x   city_x gender  age_y   city_y  salary
0  qian     25  beijing      F     25  beijing     100
'''

# merge() 整合 2 个 DataFrame 数据
#   how='inner' 默认值，只整合两边都存在的数据
#   how='outer' 整合两边的全部数据
#   how='left' 只整合左边存在的数据
#   how='right' 只整合右边存在的数据
print(pd.merge(a, b, on='name', how='outer'))
'''
   name  age_x    city_x gender  age_y    city_y  salary
0  zhao   40.0  beijing       M    NaN       NaN     NaN
1  qian   25.0   beijing      F   25.0   beijing   100.0
2   sun    NaN       NaN    NaN   22.0  shanghai   150.0
'''

# merge() 整合 2 个 DataFrame 数据
#   suffixes - 相同列名整合时，为列名加上指定的后缀，以便区分列是来自哪个 DataFrame 的
print(pd.merge(a, b, on='name', how='outer', suffixes=("_left", "_right")))
'''
   name  age_left city_left gender  age_right city_right  salary
0  zhao      40.0  beijing       M        NaN        NaN     NaN
1  qian      25.0   beijing      F       25.0    beijing   100.0
2   sun       NaN       NaN    NaN       22.0   shanghai   150.0
'''


# join() 整合 2 个 DataFrame 数据
#   相当于 how='left' 的 merge()
print(a.join(b.set_index("name"), on="name", lsuffix="_left", rsuffix='_right'))
'''
   name  age_left city_left gender  age_right city_right  salary
0  zhao        40  beijing       M        NaN        NaN     NaN
1  qian        25   beijing      F       25.0    beijing   100.0
'''



# 以下用于说明空值如何处理
index3 = ['zhao', 'qian', 'sun', 'li', 'zhou']
data3 = {
    "age": [None, None, 22, 28, 28],
    "city": ['beijing', 'beijing', None, 'beijing', 'shanghai']
}
c = pd.DataFrame(data=data3, index=index3)
print(c)
'''
NaN 数字类型的空值（来自 numpy 的 nan），None 其他类型的空值
       age      city
zhao   NaN   beijing
qian   NaN   beijing
sun   22.0      None
li    28.0   beijing
zhou  28.0  shanghai
'''

# isnull() 判断数据是否有空值
# notnull() 判断数据是否没有空值
print(c.isnull())
'''
        age   city
zhao   True  False
qian   True  False
sun   False   True
li    False  False
zhou  False  False
'''

# 获取指定列没有空值的数据
print(c[c.age.notnull()])
'''
       age      city
sun   22.0      None
li    28.0   beijing
zhou  28.0  shanghai
'''

# dropna() 删除空值数据
#   how="any" 有一个字段空值，则整行删除
#   how="all" 所有字段都空值，才整行删除
#   subset=["column1", "column2"] 只从指定的列中查询
print(c.dropna(how="any"))
'''
       age      city
li    28.0   beijing
zhou  28.0  shanghai
'''
print(c.dropna(how="any", subset=["age"]))
'''
       age      city
sun   22.0      None
li    28.0   beijing
zhou  28.0  shanghai
'''

# 为指定的字段中的空值填充一个指定的值
#   inplace=False 默认值，原对象不变，返回数据修改后的副本
#   inplace=True 直接修改原对象，返回值为 None
print(c.fillna({'age':0,'city':'unknown'}, inplace=True)) # None
print(c)
'''
       age      city
zhao   0.0   beijing
qian   0.0   beijing
sun   22.0   unknown
li    28.0   beijing
zhou  28.0  shanghai
'''