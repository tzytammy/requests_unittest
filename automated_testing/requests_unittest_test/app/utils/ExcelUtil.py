#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
excel操作工具类

get_data()方法：返回一个可迭代的列表，包含了excel中整个sheet的测试数据
xlrd库: 读取excel数据
xlwt库: 写入excel数据
xlutils库: 依赖于xlrd、xlwt库，提供复制excel文件内容和修改文件的功能,引入了以上两个库，做一些
如合并、过滤、修改文件的操作
openpyxl库:
"""

import xlrd


def hello():
	"""测试hello Python"""
	return "hello Python"


class ExcelUtil(object):
	"""excel工具类"""

	def __init__(self, file, sheet_name):
		"""
		初始化读取excel数据
		:param file: excel文件路径
		:param sheet_name: sheet名
		"""
		# 根据sheet名获得表格数据
		self.table_data = self.get_sheet_origin_data(file, sheet_name)

		# 标题行
		self.title_row = self.table_data.row_values(0)

		# 行数量
		self.row_num = self.table_data.nrows

		# 列数量
		self.col_num = self.table_data.ncols

		# 当前行号
		self.cur_row_no = 1

	@staticmethod
	def get_sheet_origin_data(file, sheet_name):
		"""
		获得sheet的数据
		:param file: excel文件
		:param sheet_name: sheet名
		:return:
		"""
		all_data = xlrd.open_workbook(file)
		return all_data.sheet_by_name(sheet_name)

	def get_data(self):
		"""以字典形式获得每一行数据，存入列表中"""

		result = []  # 存放整个表的数据

		while self.has_next():
			cur_row_result = {}   # 存放单行数据
			cur_row = self.table_data.row_values(self.cur_row_no)

			for i in range(self.col_num):
				cur_row_result[self.title_row[i]] = cur_row[i]

			result.append(cur_row_result)
			self.cur_row_no += 1
		return result

	def has_next(self):
		"""下一行是否还有数据"""

		if self.row_num == 0 or self.row_num <= self.cur_row_no:
			return False
		else:
			return True

	def get_row_count(self):
		"""返回excel表格的总行数"""
		return self.row_num

	def get_cell_value(self, row_id, col_id):
		"""
		获得单元格的内容
		:param row_id: 行号
		:param col_id: 列号
		:return:
		"""
		return self.table_data.cell_value(row_id, col_id)

	def get_row_by_case_id(self, case_id):
		"""
		根据case_id查找对应行的内容
		:param case_id: 用例ID
		:return:
		"""
		row_num = self.get_row_num(case_id)
		row_data = self.get_row_data(row_num)
		return row_data

	def get_row_num(self, case_id):
		"""
		根据case_id获得行号
		:param case_id: 用例ID
		:return:
		"""
		num = 0
		first_col_data = self.get_col_data()
		for col_data in first_col_data:
			if case_id in col_data:
				return num
			num += 1

	def get_row_data(self, row_num):
		"""
		根据行号，查找该行内容
		:param row_num:
		:return:
		"""
		row_data = self.table_data.row_values(row_num)
		return row_data

	def get_col_data(self, col_num=None):
		"""
		根据col_num获取某一列的内容, col_id为None，则返回case ID列的内容
		:param col_num: 列号
		:return:
		"""
		if col_num is not None:
			col_data = self.table_data.col_values(col_num)
		else:
			# 获取Excel中第一列的内容(也就是case ID列)
			col_data = self.table_data.col_values(0)

		return col_data
