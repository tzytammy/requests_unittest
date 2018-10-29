#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: LogUtil.py
"""
日志操作

使用Python内置的logging模块，记录用例的执行情况，便于定位错误位置
logging模块的两种使用方式:
  模块级别的函数、使用四大组件
日志的五个严重级别(level):
  DEBUG INFO WARNING ERROR CRITICAL(日志等级依次升高，记录日志的信息量依次减少)
日志的三种配置方式:
  Python代码、配置文件、dict字典
logging模块的四大组件:
  Logger Handler Filter Formatter
日志的作用:
  诊断日志(调试、定位错误)、审计日志(进行用户行为分析，指导业务，提升商业效益)
"""
import os
import json
import logging
from logging.config import fileConfig
from logging.config import dictConfig


class LogUtil(object):
	"""
	日志工具类
	"""

	def __init__(self, logger_name, log_conf_file=None, config_dict=None):
		"""
		初始化
		:param logger_name: 日志器名字
		:param log_conf_file: 日志配置文件,可为ini或json格式
		:param config_dict: 字典形式的日志配置
		"""
		self.log_config_file = log_conf_file
		if log_conf_file is not None:
			try:
				self.load_log_configuration(log_conf_file)
			except FileNotFoundError as e:
				print(str(e))
		elif config_dict is not None:
			dictConfig(config_dict)
		else:
			# 加载默认配置，日志会输出到控制台上
			logging.basicConfig()
		self.logger = logging.getLogger(logger_name)

	def load_log_configuration(self, log_config_file):
		"""
		加载日志配置文件
		:param log_config_file: 日志配置文件路径
		:return:
		"""
		extension_name = self.get_file_extension(log_config_file)
		if extension_name == 'json':
			with open(log_config_file, 'r') as fp:
				log_configuration = json.load(fp)
			dictConfig(log_configuration)
		elif extension_name == 'ini':
			fileConfig(log_config_file)
		return

	@staticmethod
	def get_file_extension(file):
		"""
		获得文件扩展名(不带点号)
		:param file: 文件名
		:return: str
		"""
		return os.path.splitext(file)[-1][1:]

	def get_current_logger(self):
		"""返回当前日志器"""
		return self.logger

	def debug(self, message, *args, **kwargs):
		self.logger.debug(message, *args, **kwargs)

	def info(self, message, *args, **kwargs):
		self.logger.info(message, *args, **kwargs)

	def warning(self, message, *args, **kwargs):
		self.logger.warning(message, *args, **kwargs)

	def error(self, message, *args, **kwargs):
		self.logger.error(message, *args, **kwargs)

	def critical(self, message, *args, **kwargs):
		self.logger.critical(message, *args, **kwargs)

	def log(self, level, message, *args, **kwargs):
		self.logger.log(level, message, *args, **kwargs)


if __name__ == '__main__':
	log_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'config/log.json')

	# log_config_dict = dict(
	# 	version=1,
	# 	disable_existing_loggers=False,
	# 	formatters={
	# 		"simple": {
	# 			"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
	# 		}
	# 	},
	# 	handlers={
	# 		"file_handler": {
	# 			"class": "logging.FileHandler",
	# 			"level": "ERROR",
	# 			"formatter": "simple",
	# 			"filename": "../../log/error.log",
	# 			"encoding": "utf8"
	# 		},
	# 		"console_handler": {
	# 			"class": "logging.StreamHandler",
	# 			"level": "DEBUG",
	# 			"formatter": "simple",
	# 			"stream": "ext://sys.stdout"
	# 		}
	# 	},
	# 	loggers={
	# 		"file_logger": {
	# 			"level": "DEBUG",
	# 			"handlers": ["console_handler"],
	# 			"propagate": "no"
	# 		},
	# 		"root": {
	# 			"level": "DEBUG",
	# 			"handlers": ["file_handler"]
	# 		}
	# 	}
	# )

	log_util = LogUtil('root', log_conf_file=log_file)

	print(log_util.logger.handlers[0].filename)

	log_util.debug('This is a debug log.')
	log_util.info('This is a info log.')
	log_util.log(logging.WARNING, 'this is a warning log.')
	log_util.error('this is a error log.')
	log_util.critical('this is a critical log.')
