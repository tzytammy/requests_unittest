#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: excel.py
# Date: 2018/6/6 23:49
#
# Excel操作类

__author__ = 'genghui'

import xlwt
import xlrd
from datetime import datetime
from xlutils.copy import copy


class Excel(object):
    """
    Excel工具类
    """

    def __init__(self, file_name=None, sheet_id=0):
        """
        初始化
        :param file_name: 文件名
        :param sheet_id: sheet标识
        """
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = "../data/test.xls"
            self.sheet_id = 0
        self.data = self.read()

    @staticmethod
    def get_workbook(file_name):
        """
        返回workbook对象
        :param file_name: 文件名
        :return:
        """
        return xlrd.open_workbook(file_name)

    def read(self):
        """
        获得sheet对象
        :return:
        """
        try:
            workbook = xlrd.open_workbook(self.file_name)
            if isinstance(self.sheet_id, int):
                sheet = workbook.sheet_by_index(self.sheet_id)
            elif isinstance(self.sheet_id, str):
                sheet = workbook.sheet_by_name(self.sheet_id)
            else:
                # 默认取第一个sheet
                sheet = workbook.sheets()[0]
            return sheet
        except ValueError as e:
            print(str(e))

    def get_rows(self):
        """
        获得excel行数、列数
        :return:
        """
        return self.data.nrows, self.data.ncols

    def get_value(self, row, col):
        """
        获取某个单元格数据
        :param row: 行数
        :param col: 列数
        :return:
        """
        return self.data.cell_value(row, col)

    def get_data(self, head_row_index=0):
        """
        根据索引获得表格数据
        :param head_row_index:  表头列名 所在行的索引
        :return: 返回字典格式的表数据
        """
        table = self.read()
        rows = table.nrows
        cols = table.ncols
        table_head_data = table.row_values(head_row_index)  # 表头行数据
        list_data = []
        for row in range(head_row_index + 1, rows):
            row_data_obj = table.row(row)
            if row_data_obj:
                dict_data = {}
                for col in range(cols):
                    # 如果是日期类型, 则单独处理
                    if row_data_obj[col].ctype == 3:
                        cell_date_value = xlrd.xldate_as_tuple(row_data_obj[col].value, Excel.get_workbook(self.file_name).datemode)
                        dict_data[table_head_data[col]] = datetime(*cell_date_value[:]).strftime('%Y/%m/%d %X')
                    # 如果内容为空
                    # elif row_data_obj[col].ctype == 6:
                    else:
                        dict_data[table_head_data[col]] = row_data_obj[col].value
                list_data.append(dict_data)
        return list_data

    @staticmethod
    def set_style(font_name=None, bold=False, height=220, color_index=4):
        """
        设置单元格样式
        :param font_name: 字体
        :param bold: 是否加粗
        :param height: 单元格高度
        :param color_index: 颜色值
        :return:
        """
        style = xlwt.XFStyle()      # 初始化样式
        style1 = xlwt.XFStyle()
        style2 = xlwt.XFStyle()

        font = xlwt.Font()          # 为样式创建字体
        font1 = xlwt.Font()
        font.name = font_name
        font.bold = bold
        font.shadow = True
        font.underline = xlwt.Font.UNDERLINE_NONE
        font.escapement = xlwt.Font.ESCAPEMENT_NONE
        font.family = xlwt.Font.FAMILY_ROMAN
        font.italic = True
        font.struck_out = False
        font.colour_index = color_index  # 0-black  4-blue
        font.height = height

        font1.colour_index = 0
        font1.bold = True
        font1.height = height * 2
        font1.name = font_name
        # 设置日期的格式 Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss,
        # M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
        style1.num_format_str = "YY-MMM-D"
        style.font = font
        style2.font = font1
        ret = (style, style1, style2)
        return ret

    @staticmethod
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
            workbook_file = xlwt.Workbook(encoding='utf-8')  # 设置字符编码，支持中文

            # 新建一个sheet,返回一个Worksheet类
            new_table_sheet = workbook_file.add_sheet(sheet_name, cell_overwrite_ok)

            # 写入初始化数据write(row, col, value)
            if initial_data:
                row, col, content = initial_data
                style_tuple = Excel.set_style('Times New Roman', False, 220, 0)

                # 可遍历的数据对象
                for row_index, row_data1 in enumerate(content):
                    for col_index, value in enumerate(row_data1):
                        if row_index == 0:
                            new_table_sheet.write(0, col_index, value, style_tuple[2])
                        else:
                            new_table_sheet.write(row_index, col_index, value, style_tuple[0])

            # 设置单元格宽度
            new_table_sheet.col(0).width = 256 * 30
            new_table_sheet.col(1).width = 256 * 30
            new_table_sheet.col(2).width = 256 * 30
            new_table_sheet.col(3).width = 256 * 30
            new_table_sheet.col(4).width = 256 * 30

            # 保存文件
            workbook_file.save(file_name)
        except Exception as e:
            print(str(e))

    @staticmethod
    def write(file_name=None, data=None):
        """
        向已存在的Excel中写入数据
        :param file_name: 打开的文件名
        :param data: 写入的数据
        :return:
        """
        try:
            workbook = Excel.get_workbook(file_name)              # 只读workbook
            writable_workbook = copy(workbook)                    # copy一份可写的workbook
            new_ws = writable_workbook.get_sheet(0)

            if data:
                row, col, content = data
                style_tuple = Excel.set_style('Times New Roman', False, 220, 0)

                # 可遍历的数据对象
                for row_index, row_data1 in enumerate(content):
                    for col_index, value in enumerate(row_data1):
                        if row_index == 0:
                            new_ws.write(0, col_index, value, style_tuple[2])
                        else:
                            new_ws.write(row_index, col_index, value, style_tuple[0])
            # 设置单元格宽度
            new_ws.col(0).width = 256 * 30
            new_ws.col(1).width = 256 * 30
            new_ws.col(2).width = 256 * 30
            new_ws.col(3).width = 256 * 30
            new_ws.col(4).width = 256 * 30

            # 保存文件
            writable_workbook.save(file_name)
        except Exception as e:
            print(str(e))