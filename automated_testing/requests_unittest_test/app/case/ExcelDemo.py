#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
对Excel中的数据进行加载测试
"""

import os
import logging
from logging.config import fileConfig
from app.utils import ExcelUtil

# 加载日志配置文件，设置日志记录器
# fileConfig(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logging_config.ini'))
# logger = logging.getLogger()
# logger.debug('often makes a very good meal of %s', 'visiting tourists')


def main():
	# 加载excel中的测试数据
	excel_obj = ExcelUtil.ExcelUtil('./2.xlsx', 'Sheet1')

	for item in excel_obj.get_data():
		print(item['username'])
		print(item['password'])

	# 打印模块字典
	print(ExcelUtil.__dict__)
	print(ExcelUtil.hello())

	# 返回当前局部命名空间存在的属性的一个字典
	print(locals())

	# 返回通过该对象可以获取到的属性的一个列表
	print(dir(ExcelUtil))


def logging_demo():
	pass


if __name__ == '__main__':
	# 返回全局命名空间中当前存在的属性的一个字典
	print(globals())
	main()
