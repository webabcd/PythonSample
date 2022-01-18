# openpyxl - excel 样式处理

from openpyxl import *
from openpyxl.styles import *
import sys

path = sys.path[0] + "\demo2.xlsx"

wb = Workbook()
sheet1 = wb.active
sheet1.title = "sheet1"

for i in range(1, 100):
    for j in range(1, 10):
        sheet1.cell(i, j).value = f'{i}_{j}'


# 指定行的行高
sheet1.row_dimensions[1].height = 40
# 指定列的列宽
sheet1.column_dimensions['A'].width = 40


# 单元格的对齐方式
# horizontal 可选值 'fill', 'distributed', 'centerContinuous', 'right', 'justify', 'center', 'left', 'general'
# vertical 可选值 'distributed', 'justify', 'center', 'bottom', 'top'
sheet1.cell(1, 1).alignment = Alignment(horizontal='center', vertical='center')


# 单元格的字体
# name - 字体名称
# size - 字体大小
# color - 字体颜色
# b - 是否粗体
# i - 是否斜体
sheet1.cell(1, 1).font = Font(name='微软雅黑', size=24, color=Color(rgb='ff0000'), b=True, i=True)


# 单元格的边框
# style - 边框样式，可选值 'dashDot','dashDotDot', 'dashed','dotted', 'double','hair', 'medium', 'mediumDashDot', 'mediumDashDotDot', 'mediumDashed', 'slantDashDot', 'thick', 'thin'
# color - 边框颜色
sheet1.cell(1, 1).border = Border(left=Side(), top=Side(), right=Side(), bottom=Side(style='thick', color='ff0000'))


# 单元格的填充
# fgColor - 填充的颜色
sheet1.cell(1, 1).fill = PatternFill(fgColor='00ff00')


# 定义样式
myStyle = NamedStyle(
            name='my_style',
            font=Font(color='ff0000'),
            fill=PatternFill(fgColor='00ff00'),
            border=Border(left=Side(style='medium',color='0000ff')),
            alignment=Alignment(horizontal='center', vertical='center')
          )
# 单元格的样式
sheet1.cell(2, 1).style = myStyle # 通过样式对象设置样式
sheet1.cell(3, 1).style = "my_style" # 通过样式名称设置样式
# cell.has_style - 单元格是否存在样式
# cell.style - 获取单元格的样式名称
print(sheet1.cell(3, 1).has_style, sheet1.cell(2, 1).style) # True my_style


# 数字格式
sheet1.cell(1, 2).value = 1234.1234
print(sheet1.cell(1, 2).number_format) # General
sheet1.cell(1, 2).number_format = '#,##0.00' # 在 excel 中单元格显示 1,234.12

# 日期也属于数字格式
import datetime
sheet1.cell(2, 2).value = datetime.datetime(2012, 12, 21, 10, 0, 0, 0)
sheet1.cell(2, 2).number_format = 'yyyy-MM-dd HH:mm:ss' # 在 excel 中单元格显示 2012-12-21 10:00:00


# 保存 excel
wb.save(path)