#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
请求头信息工具类

获取cookie、token等信息, 然后存入cookie.json文件中
"""
import os

from app.utils import JsonUtil


class HeaderUtil(object):

	def __init__(self, response):
		self.response = response

	def get_php_session_id(self):
		"""返回PHPSESSID"""
		return self.response.cookies.get('PHPSESSID')

	def get_token(self):
		"""获取登录成功后的token"""
		return self.response.json()['data']['token']

	def write_cookie(self):
		"""写入cookie文件"""
		php_session_id = self.get_php_session_id()
		token = self.get_token()
		data = {
			'PHPSESSID': php_session_id,
			'token': token
		}

		file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data/cookie.json')
		# 写入cookie.json中
		JsonUtil.write(data=data, file=file)

