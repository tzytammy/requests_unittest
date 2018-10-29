#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename: excel_demo.py
# date: 2018/6/13
# excel操作demo

__author__ = 'genghui'

import os
import xlrd
import xlwt
from datetime import datetime
from xlutils.copy import copy

path = os.getcwd()


def open_excel(file=None):
    """
    打开excel文件
    :param file: 待打开的excel文件
    :return: 返回一个workbook对象
    """
    try:
        # 要获取合并的单元格, 保留原有的格式, 需将formatting_info设置为True
        # formatting_info还没有对新版本的xlsx的格式完成兼容，所以在读取xlsx格式的Excel时，传入formatting_info会直接抛出异常,需打开xls文件
        data = xlrd.open_workbook(file, formatting_info=True)
    except FileNotFoundError as e:
        print(str(e))
    else:
        return data


def get_sheet(workbook=None, sheet_flag=None):
    """
    根据索引或名字获得sheet表格对象
    :param workbook: excel文件对象
    :param sheet_flag: sheet标识,可为索引、名字
    :return: 返回sheet表格
    """
    try:
        if isinstance(sheet_flag, int):
            table = workbook.sheet_by_index(sheet_flag)
        elif isinstance(sheet_flag, str):
            table = workbook.sheet_by_name(sheet_flag)
        else:
            # 默认取第一个sheet
            table = workbook.sheets()[0]
        return table
    except ValueError as e:
        print(str(e))


def is_sheet_loaded(file=None, sheet_name='Sheet1'):
    """
    检查sheet表是否加载
    :param file: 待打开的excel文件
    :param sheet_name: sheet名字
    :return: 加载则返回True,否则返回False
    """
    try:
        excel_obj = open_excel(file)
    except FileNotFoundError as e:
        print(str(e))
    else:
        ret = excel_obj.sheet_loaded(sheet_name)
        return ret


def get_data_by_index(book=None, head_row_index=0):
    """
    根据索引获得表格数据
    :param book: Workbook对象
    :param head_row_index:  表头列名 所在行的索引
    :return: 返回字典格式的表数据
    """
    table = get_sheet(book)
    rows = table.nrows
    cols = table.ncols
    table_head_data = table.row_values(head_row_index)    # 表头行数据
    list_data = []
    for row in range(head_row_index + 1, rows):
        row_data_obj = table.row(row)
        if row_data_obj:
            dict_data = {}
            for col in range(cols):
                # 如果是日期类型, 则单独处理
                if row_data_obj[col].ctype == 3:
                    # 得到一个tuple
                    cell_date_value = xlrd.xldate_as_tuple(row_data_obj[col].value, book.datemode)
                    # datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]), 返回datetime类型
                    dict_data[table_head_data[col]] = datetime(*cell_date_value[:]).strftime('%Y/%m/%d %X')
                # 如果内容为空
                # elif row_data_obj[col].ctype == 6:
                else:
                    dict_data[table_head_data[col]] = row_data_obj[col].value
            list_data.append(dict_data)
    return list_data


def set_style(font_name=None, bold=False, height=12, color_index=4):
    """
    创建样式
    :param font_name: 字体名字
    :param bold: 是否加粗
    :param height: 字体高度
    :param color_index: 颜色值
    :return: 返回创建的样式元组
    """
    style = xlwt.XFStyle()       # 初始化样式
    style1 = xlwt.XFStyle()
    style2 = xlwt.XFStyle()

    font = xlwt.Font()           # 为样式创建字体
    font1 = xlwt.Font()
    font.name = font_name
    # font.outline
    font.bold = bold
    font.shadow = True
    font.underline = xlwt.Font.UNDERLINE_NONE
    font.escapement = xlwt.Font.ESCAPEMENT_NONE
    font.family = xlwt.Font.FAMILY_ROMAN
    font.italic = True
    font.struck_out = False
    # font.charset = xlwt.Font.CHARSET_ANSI_LATIN
    font.colour_index = color_index   # 0-black  4-blue
    # font.get_biff_record()
    font.height = height
    font1.colour_index = 4
    font1.bold = True
<<<<<<< HEAD
    font1.height = height + 30
    font1.name = font_name

    style.font = font
    style1.num_format_str = "YY-MMM-D"   # 设置日期的格式
    style2.font = font1
    return (style, style1, style2)
=======
    font1.height = height + 60
    font1.name = font_name

    style.font = font

    # 设置日期的格式 Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss,
    # M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
    style1.num_format_str = "YY-MMM-D"

    style2.font = font1
    ret = (style, style1, style2)
    return ret
>>>>>>> b4060b1cbf29b13cf0bcb4364e4c30c741be7ee7


def write(file_name=None, data=None):
    """
    向已存在的Excel中写入数据
    :param file_name: 打开的文件名
    :param data: 写入的数据
    :return:
    """
    try:
        workbook = open_excel(file_name)           # 只读workbook
        writable_workbook = copy(workbook)         # copy一份可写的workbook
        new_ws = writable_workbook.get_sheet(0)
<<<<<<< HEAD
=======

        if data:
            row, col, content = data
            style_tuple = set_style('Times New Roman', False, 220, 0)

            # 可遍历的数据对象
            for row_index, row_data1 in enumerate(content):
                for col_index, value in enumerate(row_data1):
                    if row_index == 0:
                        new_ws.write(0, col_index, value, style_tuple[2])
                    else:
                        new_ws.write(row_index, col_index, value, style_tuple[0])

        # 保存文件
        writable_workbook.save(file_name)
    except Exception as e:
        print(str(e))
>>>>>>> b4060b1cbf29b13cf0bcb4364e4c30c741be7ee7

        if data:
            row, col, content = data
            style_tuple = set_style('Times New Roman', False, 220, 0)

            # 可遍历的数据对象
            for row_index, row_data1 in enumerate(content):
                for col_index, value in enumerate(row_data1):
                    if row_index == 0:
                        new_ws.write(0, col_index, value, style_tuple[2])
                    else:
                        new_ws.write(row_index, col_index, value, style_tuple[0])

        # 保存文件
        writable_workbook.save(file_name)
    except Exception as e:
        print(str(e))

<<<<<<< HEAD

=======
>>>>>>> b4060b1cbf29b13cf0bcb4364e4c30c741be7ee7
def new_file(sheet_name='Sheet1', file_name=None, cell_overwrite_ok=True, initial_data=None):
    """
    新建一个excel文件
    :param sheet_name: sheet名字
    :param file_name: 文件名
    :param cell_overwrite_ok: 是否可以覆盖单元格
    :param initial_data: 初始化数据,元组形式
    :return:
    """
    try:
        # 新建一个Workbook对象
        workbook_file = xlwt.Workbook(encoding='utf-8')   # 设置字符编码，支持中文

        # 新建一个sheet,返回一个Worksheet类
        new_table_sheet = workbook_file.add_sheet(sheet_name, cell_overwrite_ok)

        # 写入初始化数据write(row, col, value)
        if initial_data:
            row, col, content = initial_data
            style_tuple = set_style('Times New Roman', False, 220, 0)

            # new_table_sheet.write(row, col, 8, style_tuple[0])                                           # B2
            # new_table_sheet.write(row + 1, col + 1, 5)                                                   # C3
<<<<<<< HEAD
            # new_table_sheet.write(row + 2, col + 2, xlwt.Formula("B2+C3"))                               # 两个单元格数值相加  D4
=======
            # new_table_sheet.write(row + 2, col + 2, xlwt.Formula("B2+C3"))                               # 添加公式：两个单元格数值相加  D4
>>>>>>> b4060b1cbf29b13cf0bcb4364e4c30c741be7ee7
            # new_table_sheet.write(row + 3, col + 2, xlwt.Formula("B{0}*C{1}".format(row + 1, col + 2)))  # 两个单元格数值相乘  D5
            # new_table_sheet.write(row + 3, col + 3, datetime(2018, 6, 15), style_tuple[1])               # 写日期
            # new_table_sheet.write(row + 4, col + 2, xlwt.Formula("SUM(D4:D{0})".format(row + 4)))        # 求和
            # new_table_sheet.write(row + 5, col + 4, xlwt.Formula("'A'!$A$1&'A'!$A$2"))
<<<<<<< HEAD
            # new_table_sheet.write_merge()   # 合并单元格
=======
            # new_table_sheet.write(row + 6, col + 5, xlwt.Formula('HYPERLINK("https://www.baidu.com";"baidu")'))  # 添加链接
            # new_table_sheet.write_merge()   # 合并单元格  worksheet.write_merge(1, 2, 0, 3, 'Second Merge', style)

            # alignment = xlwt.Alignment()
            # borders = xlwt.Borders()
            # pattern = xlwt.Pattern()

            # 可遍历的数据对象
            for row_index, row_data1 in enumerate(content):
                for col_index, value in enumerate(row_data1):
                    if row_index == 0:
                        new_table_sheet.write(0, col_index, value, style_tuple[2])
                    else:
                        new_table_sheet.write(row_index, col_index, value, style_tuple[0])

        # 设置单元格宽度
        new_table_sheet.col(0).width = 4444
        new_table_sheet.col(1).width = 6500
        new_table_sheet.col(2).width = 4999
        new_table_sheet.col(4).width = 256 * 30
        # new_table_sheet.row(0).set_style(style_tuple[2])    # 设置行高
>>>>>>> b4060b1cbf29b13cf0bcb4364e4c30c741be7ee7

            # 可遍历的数据对象
            for row_index, row_data1 in enumerate(content):
                for col_index, value in enumerate(row_data1):
                    if row_index == 0:
                        new_table_sheet.write(0, col_index, value, style_tuple[2])
                    else:
                        new_table_sheet.write(row_index, col_index, value, style_tuple[0])

        # 保存文件
        workbook_file.save(file_name)
    except Exception as e:
        print(str(e))


""" 1、打开表格 """
xl_data = open_excel('./test.xls')                     # workbook对象

""" 2、获取sheet """
# sheets_names = xl_data.sheet_names()                  # 获得所有sheets的名字
# sheets_obj = xl_data.sheets()  # 获得所有sheet对象
# sheets_count = xl_data.nsheets  # 获取sheets总数

# 根据索引获得单个sheet对象
# single_sheet_obj = xl_data.sheets()[3]
first_table = get_sheet(xl_data)                       # 获取索引为0处的工作表对象

# print(first_table.merged_cells)                      # 返回sheet中合并的单元格,返回一个元组列表 [(), ()], (row,row_range,col,col_range)

# is_loaded = xl_data.sheet_loaded('Sheet1')             # 如果加载了sheets为'Sheet1'的单元,则返回True;否则返回False,
# 如果execl中不存在名为Sheet1的单元则抛出XLRDError
# xl_data.unload_sheet(index/name)                     # 索引为index或者表名为name的工作表不能再使用
# 根据名字获取sheet对象
# single_sheet_obj2 = xl_data.sheet_by_name('hello')

# print(first_table)


""" 3、获取sheet内的汇总数据 """
# print(first_table.name)                        # 表格的名字
# print(first_table.ncols, first_table.nrows)    # 表格的列数、行数

""" 4、单元格批量读取 """
# 行(row)
# print(first_table.row(2))                # 获取第一行的数据及对应的数据类型(获取单元对象)

# print(first_table.row_slice(0, 1, 3))    # 获取第0行中,start_colx -> end_colx内的单元(不包含end_colx列)
# print(first_table.row_values(0, 1, 3))   # 获取第1行的第二列、第三列的内容,若是合并单元格,首行显示值,其它为空
# print(first_table.row_types(0, 0, 2))    # 获取rowx行中,strat_colx -> end_colx内的单元格类型,返回一个数组,类似于array('B', [1, 1, 1, 1])
# print(first_table.row_types(1))
# print(first_table.get_rows())            # 所有行的生成器
# for row in first_table.get_rows():
#    print(row)

# print(first_table.merged_cells)            # 合并的单元格

# 列(col)
# print(first_table.col(0))                # 获取第一列的数据及对应的数据类型(获取单元对象)
# print(first_table.col_slice(0, 0, 2))    # 获取第0列中,start_rowx -> end_rowx内的单元(不包含end_rowx列)
# print(first_table.col_values(0))         # 获取第一列的内容
# print(first_table.col_types(0, 0, 4))    # 类似于row_types,返回一个list

""" 5、单元格(cell) """
# print("单元格：")
# print(first_table.cell(0, 0))            # 返回一个xlrd.sheet.Cell对象,获取rowx行,colx列的单元对象
# 取值
# print(first_table.cell(0, 0).value)
# print(first_table.cell_value(0, 0))      # 获取rowx行,colx列的值
# print(first_table.row(0)[1].value)
# print(first_table.col(1)[2].value)

# 取类型
# print(first_table.cell(0, 0).ctype)      # 以数字表示：0 empty string,1 string,2 number, 3 date, 4 boolean, 5 error 6 blank
# print(first_table.cell_type(1, 1))       # 获取(rowx,colx)处的类型, 返回一个数字
# print(first_table.row(3)[2].ctype)

# first_table.put_cell(0, 0, 2, 3, xf_index=0)      # 修改(row,col)处的值,ctype为单元类型,(只是修改程序中此处的值,不会影响原文件),返回None


""" 6、常用技巧（0,0）转换成A1 """
# print(xlrd.cellname(0, 1))
# print(xlrd.cellnameabs(0, 1))
# print(xlrd.colname(0))

tb_data = get_data_by_index(xl_data, 0)
for row_data in tb_data:
    print(row_data)

# print(is_sheet_loaded('./test.xlsx'))

""" 7、循环行列表数据 """
# for row in range(first_table.nrows):
#    print(first_table.row_values(row))

# for row in range(first_table.nrows):
#    for col in range(first_table.ncols):
#        if col + 1 < first_table.ncols:
#            print(first_table.cell(row, col).value, end='  ')   # 不换行
#        else:
#            print(first_table.cell(row, col).value)             # 默认会换行,end="\n"

# 新建excel文件
filled_data = [
                (u"网站名", u"域名", u"IP地址", u"端口号", u"网站负责人"),
                ("菁英汇", 'http://jyh.wshang.com', '127.0.0.1', '99', 'Jack'),
                ("宙斯CRM", 'http://crm.wshang.com', '127.0.0.1', '88', 'Mark'),
                ("数字化营销", 'http://youxiong.wshang.com', '127.0.0.1', '67', 'WangXianSen'),
            ]

file_path = os.path.join(path, '1.xls')
new_file_path = os.path.join(path, 'hello.xls')
new_file('工时统计表', new_file_path, True, (1, 1, filled_data))
# write(file_path, (1, 1, filled_data))
