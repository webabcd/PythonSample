# pandas - DataFrame 基础
#   Series - 带索引的一维表
#   DataFrame - 带索引的二维表
#
# 注 pandas 是基于 numpy 的

import pandas as pd

index1 = ['zhao', 'qian', 'sun', 'li', 'zhou']
data1 = {
    "age": [40, 25, 22, 28, 28],
    "city": ['beijing', 'beijing', 'shanghai', 'beijing', 'shanghai']
}
# 实例化 DataFrame（指定索引列，包括列名的数据列），不指定索引的话默认就是从 0 开始的序列
a = pd.DataFrame(data=data1, index=index1)
print(a)
'''
第一列是索引列，右面的都是数据列
      age      city
zhao   40   beijing
qian   25   beijing
sun    22  shanghai
li     28   beijing
zhou   28  shanghai
'''

index2 = pd.Index(['zhao', 'qian', 'sun', 'li', 'zhou'], dtype=object)
data2 = [[40,"beijing"], [25,"beijing"], [22,"shanghai"], [28,"beijing"], [28,"shanghai"]]
# 实例化 DataFrame（指定索引列和索引列的数据类型，不包括列名的数据列，数据列的列名列表），不指定索引的话默认就是从 0 开始的序列
b = pd.DataFrame(data=data2, index=index2, columns=["age", "city"])
print(b)
'''
第一列是索引列，右面的都是数据列
      age      city
zhao   40   beijing
qian   25   beijing
sun    22  shanghai
li     28   beijing
zhou   28  shanghai
'''

# 获取数据的行数和列数
print(b.shape) # (5, 2)

# 获取数据列的数据
print(b.values)
'''
[[40 'beijing']
 [25 'beijing']
 [22 'shanghai']
 [28 'beijing']
 [28 'shanghai']]
'''

# 获取索引列的数据
print(list(b.index)) # ['zhao', 'qian', 'sun', 'li', 'zhou']

# 行列转换
print(b.T)
'''
         zhao     qian       sun       li      zhou
age        40       25        22       28        28
city  beijing  beijing  shanghai  beijing  shanghai
'''

# 获取指定列的数据
print(b.get('age'))
print(b.age)
'''
zhao    40
qian    25
sun     22
li      28
zhou    28
'''
# 获取指定列的指定索引的数据
print(b.get('age').get('zhao')) # 40
print(b.age.zhao) # 40
# 取指定列最大值的索引列的值
print(b.age.idxmax()) # zhao
# 取指定列最小值的索引列的值
print(b.age.idxmin()) # sun
# 取指定列的最大值
print(b.age.max()) # 40
# 取指定列的最小值
print(b.age.min()) # 22
# 取指定列的平均值
print(b.age.mean()) # 28.6
# 取指定列的累加值
print(b.age.sum()) # 143
# 取指定列的中位数
print(b.age.quantile()) # 28.0
# 取指定列的标准差
print(b.age.std()) # 6.841052550594829
# 对指定的列做累加求和（返回一个 Series 类型的数据）
print(b.age.cumsum())
'''
zhao     40
qian     65
sun      87
li      115
zhou    143
'''

# 获取指定索引的数据
print(b.loc['zhao']) # 返回的是 Series 对象
'''
age          40
city    beijing
'''
# 获取指定位置的数据
print(b.iloc[0]) # 返回的是 Series 对象
'''
age          40
city    beijing
'''
# 获取指定索引的指定列的数据
print(b.loc['zhao'].city) # beijing
print(b.loc['zhao'].get('city')) # beijing
print(a.loc['zhao'][['age', 'city']])
'''
age          40
city    beijing
'''
# 获取指定索引的行的最大值（前提是这行都是数字类型的）。类似的还有 min(), idxmax(), idxmin(), mean(), sum(), quantile(), std(), cumsum() 之类的，上面都写了
# print(b.loc['zhao'].max())

# 为 DataFrame 添加列，并为其指定相同的值
b["gender"] = "M"
'''
      age      city gender
zhao   40   beijing      M
qian   25   beijing      M
sun    22  shanghai      M
li     28   beijing      M
zhou   28  shanghai      M
'''
print(b)

# 为 DataFrame 添加列，并为其指定不同的值
b["salary"] = [100, 200, 150, 150, 150]
print(b)
'''
      age      city gender  salary
zhao   40   beijing      M     100
qian   25   beijing      M     200
sun    22  shanghai      M     150
li     28   beijing      M     150
zhou   28  shanghai      M     150
'''

# 为 DataFrame 添加列，并为其指定与原有信息相关的值
b = b.assign(salary_expected=b["salary"] * 2)
print(b)
'''
      age      city gender  salary  salary_expected
zhao   40   beijing      M     100              200
qian   25   beijing      M     200              400
sun    22  shanghai      M     150              300
li     28   beijing      M     150              300
zhou   28  shanghai      M     150              300
'''

# 为 DataFrame 添加列，并为其指定与原有信息相关的值（通过调用函数的方式）
def getLevel(age, salary): 
    # 注意：这里的 age 和 salary 是 Series 类型的数据
    print(type(age), type(salary)) # <class 'pandas.core.series.Series'> <class 'pandas.core.series.Series'>
    return (age * 0.5 + salary * 2) / 50
b = b.assign(level=getLevel(b["age"], b["salary"]))
print(b)
'''
      age      city gender  salary  salary_expected  level
zhao   40   beijing      M     100              200   4.40
qian   25   beijing      M     200              400   8.25
sun    22  shanghai      M     150              300   6.22
li     28   beijing      M     150              300   6.28
zhou   28  shanghai      M     150              300   6.28
'''

# 删除指定的列
b = b.drop(["salary_expected"], axis=1)
print(b)
'''
      age      city gender  salary  level
zhao   40   beijing      M     100   4.40
qian   25   beijing      M     200   8.25
sun    22  shanghai      M     150   6.22
li     28   beijing      M     150   6.28
zhou   28  shanghai      M     150   6.28
'''

# 修改列名
b = b.rename(columns={"level": "employee_level"}) 
print(b)
'''
      age      city gender  salary  employee_level
zhao   40   beijing      M     100            4.40
qian   25   beijing      M     200            8.25
sun    22  shanghai      M     150            6.22
li     28   beijing      M     150            6.28
zhou   28  shanghai      M     150            6.28
'''

# 删除指定的行
b = b.drop(["zhou"], axis=0)
print(b)
'''
      age      city gender  salary  employee_level
zhao   40   beijing      M     100            4.40
qian   25   beijing      M     200            8.25
sun    22  shanghai      M     150            6.22
li     28   beijing      M     150            6.28
'''

# 替换指定字段的指定的值为另一个指定的值
b = b.replace({"city": 'beijing'}, 'bj')
print(b)
'''
      age      city gender  salary  employee_level
zhao   40        bj      M     100            4.40
qian   25        bj      M     200            8.25
sun    22  shanghai      M     150            6.22
li     28        bj      M     150            6.28
'''

# 所有数据都变为大写
print(a.applymap(lambda x: str(x).upper()))
'''
     age      city
zhao  40   BEIJING
qian  25   BEIJING
sun   22  SHANGHAI
li    28   BEIJING
zhou  28  SHANGHAI
'''

# 所有数据都乘以 2
def temp(x):
    return x * 2
print(a.applymap(lambda x: temp(x)))
'''
      age              city
zhao   80    beijingbeijing
qian   50    beijingbeijing
sun    44  shanghaishanghai
li     56    beijingbeijing
zhou   56  shanghaishanghai
'''

# 修改索引名
b = b.rename(index={"zhao": "wang"}) 
print(b)
'''
      age      city gender  salary  employee_level
wang   40        bj      M     100            4.40
qian   25        bj      M     200            8.25
sun    22  shanghai      M     150            6.22
li     28        bj      M     150            6.28
'''