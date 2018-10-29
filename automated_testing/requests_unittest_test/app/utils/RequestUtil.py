#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: RequestUtil.py
"""
HTTP网络请求工具类

使用requests库发送get、post请求
"""
import threading
import requests
# from requests.sessions import Session


class RequestUtil(object):
	_instance_lock = threading.Lock()

	def __new__(cls, *args, **kwargs):
		"""实现单例模式"""
		if not hasattr(cls, '_instance'):
			with cls._instance_lock:
				if not hasattr(cls, '_instance'):
					cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, base_url):
		"""
		初始化
		:param base_url: 接口基础url
		"""
		self.base_url = base_url
		# self.session = Session()

	@staticmethod
	def send_get(url, params=None, headers=None, cookies=None):
		"""
		GET请求
		:param url:
		:param params:
		:param headers:
		:param cookies:
		:return:
		"""
		if headers is not None:
			response = requests.get(url, params=params, headers=headers, cookies=cookies, verify=False)
		else:
			response = requests.get(url, params=params, cookies=cookies, verify=False)
		# return response.json()
		return response

	@staticmethod
	def send_post(url, data, headers=None, cookies=None):
		"""
		POST请求
		:param url:
		:param data:
		:param headers:
		:param cookies:
		:return:
		"""
		if headers is not None:
			response = requests.post(url=url, data=data, headers=headers, cookies=cookies)
		else:
			response = requests.post(url=url, data=data, cookies=cookies)
		# return response.json()
		return response

	@staticmethod
	def send_put(url, data=None, headers=None, cookies=None):
		"""
		发送PUT请求
		:param url:
		:param data:
		:param headers:
		:param cookies:
		:return:
		"""
		if headers is not None:
			response = requests.put(url=url, data=data, headers=headers, cookies=cookies, verify=False)
		else:
			response = requests.put(url=url, data=data, cookies=cookies, verify=False)
		return response

	@staticmethod
	def send_delete(url, data=None, headers=None, cookies=None):
		"""
		发送PUT请求
		:param url:
		:param data:
		:param headers:
		:param cookies:
		:return:
		"""
		if headers is not None:
			response = requests.delete(url=url, data=data, headers=headers, cookies=cookies, verify=False)
		else:
			response = requests.delete(url=url, data=data, cookies=cookies, verify=False)
		return response

	def run(self, url, method, data=None, headers=None, cookies=None):
		"""
		主方法
		:param url: 请求url
		:param method: 请求类型
		:param data: 请求数据
		:param headers: 请求头
		:param cookies:
		:return:
		"""
		response = None
		if method == "POST":
			response = self.send_post(url, data, headers, cookies)
		elif method == "PUT":
			response = self.send_put(url, data, headers, cookies)
		elif method == "DELETE":
			response = self.send_delete(url, data, headers, cookies)
		elif method == "GET":
			response = self.send_get(url, data, headers, cookies)
		return response
