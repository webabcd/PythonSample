# pandas
#   DataFrame 筛选和分组

import pandas as pd

data = {
    "age": [40, 25, 22, 28, 28],
    "gender": ['M', 'F', 'M', 'M', 'F'],
    "city": ['beijing', 'beijing', 'shanghai', 'beijing', 'shanghai']
}
index = pd.Index(['zhao', 'qian', 'sun', 'li', 'zhou'])
a = pd.DataFrame(data=data, index=index)
print(a)
'''
      age gender      city
zhao   40      M   beijing
qian   25      F   beijing
sun    22      M  shanghai
li     28      M   beijing
zhou   28      F  shanghai
'''


# 按照索引正序排序
print(a.sort_index())
# 按照索引倒序排序
print(a.sort_index(ascending=False))
# 按照指定字段和指定顺序排序
print(a.sort_values(by="age", ascending=False))
# 先按 city 排序，再按 age 排序
print(a.sort_values(by=["city", "age"]))


# 取前 n 条数据
print(a.head(2))
# 取后 n 条数据
print(a.tail(2))
# 获取 age 字段最大的前 2 条数据
print(a.nlargest(2, 'age'))
# 获取 age 字段最小的前 2 条数据
print(a.nsmallest(2, 'age'))


# 取索引 zhao 和 sun 的数据
print(a.loc[['zhao', 'sun']]) 
# 取索引 zhao 到 sun 之间的数据
print(a.loc['zhao':'sun']) 
# 取 age 列和 city 列的全部数据
print(a.loc[:, ["age", "city"]])
# 取索引 zhao 和 sun 的 age 列到 city 列之间的数据
print(a.loc[['zhao', 'sun'], "age":"city"])
# 取位置 0 和 3 的数据
print(a.iloc[[0,3]])
# 取位置 0 到 2 的数据
print(a.iloc[0:3]) 
# 取第 1 行到第 3 行，第 1 列到第 2 列的数据
print(a.iloc[0:3, 0:2])
'''
      age gender
zhao   40      M
qian   25      F
sun    22      M
'''


# 取 age 大于 30 且 gender 是 M 的数据
#   & 和
#   | 或
#   ~ 非
print(a[(a.age>30) & (a.gender=='M')])
# 取 age 大于 30 的只包含 age 列的数据
print(a.loc[a.age>30, ["age"]])
# 取 city 为 beijing 或 shanghai 的数据
print(a[a.city.isin(["beijing", "shanghai"])])
# 取索引为 zhao 的数据
print(a[a.index.isin(["zhao"])])



# 以下用于演示如何对数组做分组
# 依据 gender 分组
b = a.groupby("gender")
# 依据 gender 和 city 的联合值分组
c = a.groupby(["gender", "city"])

# 获取全部分组数据
print(b.groups) # {'F': ['qian', 'zhou'], 'M': ['zhao', 'sun', 'li']}
print(c.groups) # {('F', 'beijing'): ['qian'], ('F', 'shanghai'): ['zhou'], ('M', 'beijing'): ['zhao', 'li'], ('M', 'shanghai'): ['sun']}

# 遍历分组
for name, group in b: 
    print(name)
    print(group) 
'''
F
      age gender      city
qian   25      F   beijing
zhou   28      F  shanghai
M
      age gender      city
zhao   40      M   beijing
sun    22      M  shanghai
li     28      M   beijing
'''

# 分组统计（更多功能需要借助 numpy 库，比如统计平均值可以用 numpy.mean）
# 统计不同 gender 分组的相同年龄的数量
print(b["age"].agg(len))
'''
gender
F    2
M    3
'''
# 统计不同 gender 分组的最大年龄
print(b["age"].agg(max))
'''
gender
F    28
M    40
'''

# 统计不同 gender 分组的年龄的累加值和最大值（可以指定统计后的列名）
print(b["age"].agg([sum, max]).rename(columns={"sum":"mySum", "max":"myMax"}))
'''
        mySum  myMax
gender
F          53     28
M          90     40
'''

# 支持同时对分组数据的不同字段做统计（可以指定统计后的列名）
print(b.agg({"age":sum}).rename(columns={"age": "myAge"}))
'''
        myAge
gender
F          53
M          90
'''