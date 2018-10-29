#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: Dependency.py
"""
接口依赖工具类

接口测试时的参数会出现依赖另一个接口返回结果中某个字段的情况
此时，就产生了接口依赖的需求
"""
import os
import json

from app.utils import RequestUtil
from app.utils import JsonUtil
from app.utils import Config


class DependencyUtil(object):

	def __init__(self):
		self.config_util = Config.ConfigUtil()
		self.base_url = self.config_util.get_option_value_by_section('crm', 'base_url')
		self.request = RequestUtil.RequestUtil(self.base_url)

		# 从cookie.json中读取PHPSESSID
		cookie_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data/cookie.json')
		php_session_id = JsonUtil.get_data(cookie_file, 'PHPSESSID')
		self.cookies = {
			"PHPSESSID": php_session_id
		}
		self.headers = {
			'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
		}

	def get_dependency_api_data(self, url, method='GET', params=None):
		response = self.request.run(url=url, method=method, data=params, headers=self.headers, cookies=self.cookies)
		return json.loads(response.text)


if __name__ == '__main__':
	# customer_id: 132395
	dependency_obj = DependencyUtil()
	order_list_url = 'http://crm.wshang.com/index.php?s=/Crm/Order/index'
	data = {
		"status": -1,
		"operate_pid": 10
	}

	# 订单详情接口参数
	# data = {
	# 	'order_id': 6747,
	# 	'second_product_id': 10217
	# }

	order_list = dependency_obj.get_dependency_api_data(order_list_url, method='GET', params=data).get('data')
	order_detail_param = [{'order_id': int(order_item['order_id']), 'second_product_id': int(order_item['second_product_id'])} for order_item in order_list]

	print(order_list)
	print(order_detail_param)
