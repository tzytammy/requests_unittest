#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Python中实现单例的方式:

1、装饰器
2、类
3、__new__(推荐)
"""

import threading

# 1、装饰器
# def singleton(cls):
# 	_instance = {}
#
# 	def _singleton(*args, **kwargs):
# 		if cls not in _instance:
# 			_instance[cls] = cls(*args, **kwargs)
# 		else:
# 			return _instance[cls]
# 	return _singleton


class Demo(object):
	_instance_lock = threading.Lock()

	# 3、__new__
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			with cls._instance_lock:
				if not hasattr(cls, '_instance'):
					cls._instance = object.__new__(cls)
		return cls._instance

	def __init__(self, x):
		self.x = x

	def hello(self):
		return self.x + 1
