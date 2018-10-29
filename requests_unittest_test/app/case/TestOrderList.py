#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: TestOrderList.py
"""
CRM 销售中心-订单-列表接口

数据驱动(Data Driven Testing)：
1、可以通过json库读取JSON文件
2、可以通过ddt库的@ddt、@file_data装饰器读取JSON文件. @file_data的参数接收json或yaml类型文件
3、可以通过ddt库的@ddt、@data结合@unpack装饰器直接把 用例数据 和 测试用例 放在一起
4、可以通过@parameterized.expand参数化来传入用例参数
5、paramunittest模块实现参数化
6、CSV、Excel
"""
import os
# 参数化模块
from parameterized import parameterized
import paramunittest
import unittest

# 数据驱动模块ddt
from ddt import ddt
from ddt import file_data
from ddt import data
from ddt import unpack

from app.libs.Base import Base
from app.utils.ExcelUtil import ExcelUtil
from app.utils import LogUtil
from app.utils import JsonUtil
from app.utils import DependencyUtil


# 订单详情接口参数依赖于订单列表接口返回的数据
dependency_instance = DependencyUtil.DependencyUtil()
order_list_url = 'http://crm.wshang.com/index.php?s=/Crm/Order/index'
order_list_params = {
	"customer_id": 132395,
	"operate_pid": 10
}
order_list_res = dependency_instance.get_dependency_api_data(url=order_list_url, method='GET', params=order_list_params)
order_list = order_list_res.get('data')
order_detail_param = [{'order_id': int(order_item['order_id']), 'second_product_id': int(order_item['second_product_id'])} for order_item in order_list]


@ddt
class TestOrderModule(Base):
	""" 接口名称：订单列表 """

	@classmethod
	def setUpClass(cls):
		super(TestOrderModule, cls).setUpClass()
		# 从cookie.json中读取PHPSESSID
		cookie_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data/cookie.json')
		php_session_id = JsonUtil.get_data(cookie_file, 'PHPSESSID')
		cls.cookies = {
			"PHPSESSID": php_session_id
		}

	def setUp(self):
		""" environment init before test """
		# excel文件1.xlsx的路径
		# 加载excel中的测试数据
		excel_path = os.path.join(os.path.dirname(__file__), '1.xlsx')
		excel_obj = ExcelUtil(excel_path, 'Sheet1')
		print("start test")
		pass

	def tearDown(self):
		""" environment clear after test """
		print("end test")
		pass

	# 参数化扩展
	# @parameterized.expand([
	# 	("case01", "http://crm.wshang.com/index.php?s=/Crm/Order/index", "http://crm.wshang.com/index.php?s=/Pub/Public/login", "晏雪彬", 'jiubugaosuni12'),
	# 	("case02", "http://crm.wshang.com/index.php?s=/Crm/Order/index", "http://crm.wshang.com/index.php?s=/Pub/Public/login", "谢磊", 'jiubugaosuni12'),
	# ])
	# def test_get_list(self, name, url, login_url, account, passwd):
	# 	"""
	# 	用例1
	# 	"""
	# 	r = self.req.run(url, 'GET', None, headers, cookies)
	# 	self.assertIn("true", r.text)

	# @file_data("./test_ddt_file.json")   # @file_data装饰器读取JSON数据文件
	@data('http://crm.wshang.com/index.php?s=/Crm/Order/index')
	def test_get_list(self, url):
		"""
		获得订单列表接口用例
		"""
		params = {
			"customer_id": 132395,
			"operate_pid": 10
		}
		res = self.request.run(url, 'GET', data=params, headers=self.headers, cookies=self.cookies)

		# # 测试打印日志
		# log_conf_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'config/log.ini')
		# log_util1 = LogUtil.LogUtil('root', log_conf_file=log_conf_file)
		# log_util1.info('order info')
		# log_util1.error('order hhha')
		# log_util1.critical('order critical')

		self.assertEqual(True, res.json()['success'])

	@data(*order_detail_param)
	def test_order_detail(self, order_data):
		"""
		订单详情接口测试用例
		依赖于订单列表接口返回的数据
		:param order_data:
		:return:
		"""
		detail_url = 'http://crm.wshang.com/index.php?s=/Crm/Order/detail'
		params = {
			"order_id": order_data['order_id'],
			"second_product_id": order_data['second_product_id']
		}
		res = self.request.run(detail_url, 'GET', data=params, headers=self.headers, cookies=self.cookies)
		self.assertEqual(True, res.json()['success'])
