# openpyxl - excel 数据处理

from openpyxl import *
import sys

# sys.path[0] 用于获取当前运行的目录
path = sys.path[0] + "\demo1.xlsx"

# 实例化一个空的工作簿对象（可以把它理解为 excel 文件）
wb = Workbook()
# load_workbook() - 通过指定的 excel 文件实例化工作簿对象
# wb = load_workbook(path)

# 当前 excel 文件中选中的 sheet 对象
sheet1 = wb.active
# 修改 sheet 的名称
sheet1.title = "sheet1"
# 创建新的 sheet 并指定其名称
sheet3 = wb.create_sheet("sheet3")
sheet4 = wb.create_sheet("sheet4")
sheet5 = wb.create_sheet("sheet5")
sheet6 = wb.create_sheet("sheet6")
# 在指定位置创建新的 sheet 并指定其名称（index 如果是 -1 的话就代表在倒数第 2 个位置新建 sheet）
sheet2 = wb.create_sheet("sheet2", index=1)
# 删除指定的 sheet
# wb.remove(sheet6)
# 删除指定的 sheet
del wb["sheet6"]
# 获取 excel 的所有 sheet 的名称列表
print(wb.sheetnames) # ['sheet1', 'sheet2', 'sheet3', 'sheet4', 'sheet5']


# 为单元格赋值的几种方式
sheet1["A1"].value = "1_1" # 第一行第一列
sheet1.cell(1, 2).value = "1_2" # 第一行第二列
sheet1.append(["a", "b", "c"])

# 获取指定位置的单元格对象
cell = sheet1.cell(3, 5)
# cell.row - 单元格的所在行的位置（数字表示）
# cell.column - 单元格的所在列的位置（数字表示）
# cell.column_letter - 单元格的所在列的位置（字母表示）
# cell.coordinate - 单元格的坐标（字母和数字表示）
# cell.encoding - 单元格的编码方式（默认是 utf-8）
# cell.data_type - 单元格的数据格式
#                  n 数值（默认值）
#                  s 字符串
#                  d 日期时间
print(cell.row, cell.column, cell.column_letter, cell.coordinate, cell.encoding, cell.data_type) # 3 5 E E3 utf-8 n


# 获取第一列的全部单元格对象
print(sheet1["A"]) # (<Cell 'sheet1'.A1>, <Cell 'sheet1'.A2>, <Cell 'sheet1'.A3>)
# 获取第一行的全部单元格对象
print(sheet1[1]) # (<Cell 'sheet1'.A1>, <Cell 'sheet1'.B1>, <Cell 'sheet1'.C1>, <Cell 'sheet1'.D1>, <Cell 'sheet1'.E1>)
# 获取第一列到第二列的全部单元格对象
print(sheet1["A:B"]) # ((<Cell 'sheet1'.A1>, <Cell 'sheet1'.A2>, <Cell 'sheet1'.A3>), (<Cell 'sheet1'.B1>, <Cell 'sheet1'.B2>, <Cell 'sheet1'.B3>))
# 获取第一行到第二行的全部单元格对象
print(sheet1[1:2]) # ((<Cell 'sheet1'.A1>, <Cell 'sheet1'.B1>, <Cell 'sheet1'.C1>, <Cell 'sheet1'.D1>, <Cell 'sheet1'.E1>), (<Cell 'sheet1'.A2>, <Cell 'sheet1'.B2>, <Cell 'sheet1'.C2>, <Cell 'sheet1'.D2>, <Cell 'sheet1'.E2>))
# 获取第一行第一列到第二行第二列的全部单元格对象
print(sheet1["A1:B2"]) # ((<Cell 'sheet1'.A1>, <Cell 'sheet1'.B1>), (<Cell 'sheet1'.A2>, <Cell 'sheet1'.B2>))


for i in range(1, 4):
    for j in range(1, 6):
        sheet2.cell(i, j).value = f'{i}_{j}'
# 删除第一行
sheet2.delete_rows(1)
# 删除第一列
sheet2.delete_cols(1)
# 获取 sheet 的行数和列数
print(sheet2.max_row, sheet2.max_column) # 2 4

# 遍历出的数据是：每行的单元格值的元组
for row in sheet2.values:
    print(row)

# 遍历出的数据是：每行的单元格对象的元组
for row in sheet2.rows:
    print(row)

# 遍历出的数据是：指定范围的每行的单元格对象的元组
for row in sheet2.iter_rows(min_col=1,max_col=2,min_row=1,max_row=2):
    print(row)

# 遍历出的数据是：每列的单元格对象的元组
for column in sheet2.columns:
    print(column)

# 遍历出的数据是：指定范围的每列的单元格对象的元组
for column in sheet2.iter_cols(min_col=1,max_col=2,min_row=1,max_row=2):
    print(column)


for i in range(1, 4):
    for j in range(1, 6):
        sheet3.cell(i, j).value = f'{i}_{j}'
# 合并指定范围的单元格，并保留左上单元格的数据
sheet3.merge_cells("A1:B1")
sheet3.merge_cells(start_column=3,end_column=4,start_row=1,end_row=3)


for i in range(1, 10):
    for j in range(1, 10):
        sheet4.cell(i, j).value = i * j
# 为指定的单元格设置公式
sheet4.cell(1, 10).value = '=SUM(H1:I1)'


from openpyxl.utils import get_column_letter, column_index_from_string
# 根据列的数字位置返回字母位置
print(get_column_letter(4))  # D
# 根据列的字母位置返回数字位置
print(column_index_from_string('D'))  # 4


# 保存 excel
wb.save(path)