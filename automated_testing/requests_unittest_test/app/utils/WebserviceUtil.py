#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: WebserviceUtil.py
"""
Webservice接口测试
"""

from suds.client import Client


class WebserviceUtil(object):

	def __init__(self, ws_url):
		self.client = Client(ws_url)

	def get_methods_name(self):
		method_list = []
		for method in self.client.wsdl.services[0].ports[0].methods:
			method_list.append(method)
		return method_list

	def get_method_param(self, method_name):
		method = self.client.wsdl.services[0].ports[0].methods[method_name]
		input_param = method.binding.input
		params = input_param.param_defs(method)[0]
		return params[1].name

	def run(self):
		for method in self.get_methods_name():
			func = getattr(self.client.service, method)
			print(func('***'))


if __name__ == '__main__':
	url = '*****'
	webservice = WebserviceUtil(url)
	webservice.run()
