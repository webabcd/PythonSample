# openpyxl 结合 pandas
# 本例演示了 sheet 和 DataFrame 之间如何互相转换

from openpyxl import *
from openpyxl.utils.dataframe import dataframe_to_rows
from itertools import islice
import pandas as pd
import sys

path = sys.path[0] + "\demo3.xlsx"
wb = Workbook()
sheet1 = wb.active
sheet1.title = "sheet1"


data1 = {
    "name": ['zhao', 'qian', 'sun', 'li', 'zhou'],
    "age": [40, 25, 22, 28, 28],
    "gender": ['M', 'F', 'M', 'M', 'F'],
    "city": ['beijing', 'beijing', 'shanghai', 'beijing', 'shanghai']
}
df1 = pd.DataFrame(data=data1)
# DataFrame 数据写入 sheet
#    index 用于指定是否需要写入索引列的数据
#    header 用于指定是否需要写入标题数据
for row in dataframe_to_rows(df1, index=False, header=True):
    sheet1.append(row)
'''
保存到 sheet 后的数据是这样的
name	age	gender	city
zhao	40	M	beijing
qian	25	F	beijing
sun	22	M	shanghai
li	28	M	beijing
zhou	28	F	shanghai

'''


# sheet 转 DataFrame
#   firstColumnIsIndexColumn 用于指定第一列是否是索引列
#     True 把第一列作为 DataFrame 的索引列
#     False 自动生成 DataFrame 的索引列
# 注：本函数会将 sheet 的第一行转换为 DataFrame 的列名
def sheetToDataFrame(sheet, firstColumnIsIndexColumn):
    data = sheet.values
    if (firstColumnIsIndexColumn):
        cols = next(data)[1:] 
        data = list(data)
        idx = [r[0] for r in data]
        data = (islice(r, 1, None) for r in data)
    else:
        cols = next(data)[:] 
        data = list(data)
        idx = None
        data = (islice(r, 0, None) for r in data)
    return pd.DataFrame(data, index=idx, columns=cols)

df2 = sheetToDataFrame(sheet1, True)
df3 = sheetToDataFrame(sheet1, False)

print(df2)
'''      age gender      city
zhao   40      M   beijing
qian   25      F   beijing
sun    22      M  shanghai
li     28      M   beijing
zhou   28      F  shanghai'''
print(df3)
'''
   name  age gender      city
0  zhao   40      M   beijing
1  qian   25      F   beijing
2   sun   22      M  shanghai
3    li   28      M   beijing
4  zhou   28      F  shanghai
'''


# 保存 excel
wb.save(path)