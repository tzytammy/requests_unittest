#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: GlobalFunction.py
"""
公共函数库
"""

import os
import unittest


def new_report(test_report):
	"""
	查找最新的测试报告

	:param test_report:
	:return:
	"""
	lists = os.listdir(test_report)
	# Mac平台
	lists.sort(key=lambda fn: os.path.getmtime(test_report + '/' + fn))

	# windows平台
	lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))

	file_new = os.path.join(test_report, lists[-1])

	return file_new


def create_suite(case_path):
	"""
	创建测试套件
	:param case_path:
	:return:
	"""
	test_unit = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py', top_level_dir=None)
	for test_suite in discover:
		for test_case in test_suite:
			test_unit.addTest(test_case)

	return test_unit
