#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: TestLogin.py
"""
登录接口测试用例

登录成功，将PHPSESSID写入cookie.json文件
"""

import os

# 参数化模块
from parameterized import parameterized
# 数据驱动模块ddt
from ddt import ddt
from ddt import file_data
from ddt import data
from ddt import unpack

from app.libs.Base import Base
from app.utils.HeaderInfo import HeaderUtil


@ddt
class TestLoginDemo(Base):

	@classmethod
	def setUpClass(cls):
		super(TestLoginDemo, cls).setUpClass()

	def setUp(self):
		""" environment init before test """
		print("login test start")
		pass

	def tearDown(self):
		""" environment clear after test """
		print("login test end")
		pass

	@data(
		['陈琳', 'jiubugaosuni30']
	)
	@unpack
	def test_login_api(self, account, password):
		"""
		登录接口测试用例
		:return:
		"""
		# 组装登录数据
		login_data = {
			'account': account,
			'password': password
		}

		res = self.request.run(self.login_url, 'POST', login_data, self.headers)
		# 将PHPSESSID写入cookie.json
		header_obj = HeaderUtil(res)
		header_obj.write_cookie()

		self.assertEqual(True, res.json()['success'])
