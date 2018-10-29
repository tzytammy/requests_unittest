#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: Config.py
"""
配置工具类

对ini格式配置文件进行操作
实现对配置文件的CRUD操作
配置文件用于存放一些环境相关的变量、数据库信息、用户信息等
"""

import os
import configparser


class ConfigUtil(object):

	def __init__(self, config_file=None):
		"""
		初始化设置
		:param config_file: 待操作的配置文件
		"""
		self.config_parser = configparser.ConfigParser()  # 配置解析类对象
		if config_file is not None:
			self.file = config_file
		else:
			# 默认加载公共配置文件
			self.file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'config/common.ini')
		self.config_parser.read(self.file, encoding='utf-8')

	def get_all_sections(self):
		"""获取所有的section块"""
		return self.config_parser.sections()

	def get_options_by_section(self, section_name):
		"""
		获取section_name块下的所有配置项
		:param section_name: 配置块名字
		:return:
		"""
		return self.config_parser.options(section_name)

	def get_option_value_by_section(self, section_name, option_name):
		"""
		获取指定section下指定option的值
		:param section_name: 指定section块名字
		:param option_name: 指定option配置项名字
		:return:
		"""
		# return self.config_parser.getint(section_name, option_name)  # 将获取到的值转换成int型
		return self.config_parser.get(section_name, option_name)

	def get_all_option_value_by_section(self, section_name):
		"""
		获取指定section下所有配置项的值
		:param section_name: 指定section块名字
		:return:
		"""
		return self.config_parser.items(section_name)

	def has_section(self, section_name):
		"""
		检查某个section块是否存在
		:param section_name: 指定section块
		:return: boolean
		"""
		return self.config_parser.has_section(section_name)

	def has_option(self, section_name, option_name):
		"""
		检查section下某个option是否存在
		:param section_name:
		:param option_name:
		:return: boolean
		"""
		return self.config_parser.has_option(section_name, option_name)

	def set_option(self, section_name, option_name, option_value):
		"""
		修改某个option的值，如果不存在该option则会创建
		:param section_name: section名字
		:param option_name: option名字
		:param option_value: option值
		:return:
		"""
		self.config_parser.set(section_name, option_name, option_value)
		with open(self.file, 'r+') as fp:
			self.config_parser.write(fp)
		return

	def delete_section(self, section_name):
		"""
		删除某个配置块
		:param section_name: 指定配置块
		:return:
		"""
		self.config_parser.remove_section(section_name)
		with open(self.file, 'w+') as fp:
			self.config_parser.write(fp)
		return

	def delete_option(self, section_name, option_name):
		"""
		删除某个配置项
		:param section_name: 指定配置块
		:param option_name: 指定配置项
		:return:
		"""
		self.config_parser.remove_option(section_name, option_name)
		with open(self.file, 'w+') as fp:
			self.config_parser.write(fp)
		return


if __name__ == '__main__':
	file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/database.ini')
	config = ConfigUtil(file)

	print("配置块: ", config.get_all_sections())
	print("db块配置项为: ", config.get_options_by_section('db'))
	print("db块host的值为: ", config.get_option_value_by_section('db', 'host'))
	# print("db块所有配置项的信息为: ", config.get_all_option_value_by_section('db'))
	# config.set_option('db', 'name', 'admin')
	# config.delete_section('test')
	# config.delete_option('db', 'name')
