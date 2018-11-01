#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
测试基类

"""
import unittest

from app.utils import RequestUtil
from app.utils import Config


class Base(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.config_util = Config.ConfigUtil()
		cls.base_url = cls.config_util.get_option_value_by_section('crm', 'base_url')
		cls.login_url = cls.config_util.get_option_value_by_section('crm', 'login_url')
		cls.request = RequestUtil.RequestUtil(cls.base_url)
		cls.headers = {
			'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
			" Chrome/57.0.2987.133 Safari/537.36"
		}

	@classmethod
	def tearDownClass(cls):
		cls.request = None
