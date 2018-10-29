#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: request_demo.py
import os
import json
import datetime
import argparse
import logging
import logging.handlers
from logging.config import fileConfig

from app.utils import ExcelUtil
from app.utils import RequestUtil


class RunTest(object):
	"""
	requests库测试类
	"""

	def __init__(self):
		file_path = os.path.join(os.path.dirname(__file__), 'app/case/1.xlsx')
		self.excel_instance = ExcelUtil.ExcelUtil(file_path, 'Sheet1')
		self.run_tool = RequestUtil.RequestUtil('http://crm.wshang.com/index.php?s=')

	def start_run(self):
		data = self.excel_instance.get_data()

		# 先登录
		user_account = {
			'account': data[1]['account'],
			'password': data[1]['password']
		}
		login_res = self.run_tool.run(data[1]['login_url'], 'POST', user_account)

		# 获得订单列表
		# cookies = {
		# 	'PHPSESSID': login_res.cookies.get('PHPSESSID')
		# }
		headers = {
			'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'
		}
		params = {
			'status': -1,
			'operate_pid': 10
		}
		resp = self.run_tool.run(data[1]['url'], 'GET', params, headers)

		print(resp.json())
		print('登录响应数据为: ', login_res.json())
		print('登录响应Token为: ', login_res.json()['data']['token'])
		print('登录响应cookieJar为: ', login_res.cookies)
		print('登录响应cookie数据为: ', login_res.cookies.get('PHPSESSID'))

		# 输出日志信息
		# 1、模块级别的函数
		# 1.1 模块级别的函数，所使用的日志记录器设置的日志级别是WARNING
		# 1.2 CRITICAL:root:this is a critical log.
		#  上面日志记录各个字段的含义分别是： 日志级别：日志器名称：日志内容
		#  之所以有上面的输出，是因为模块级别的函数，所使用的日志记录器设置的日志格式默认是BASIC_FORMAT,
		#  其值为"%(levelname)s:%(name)s:%(message)s"
		# 1.3 模块级别的函数，所使用的日志记录器设置的处理器，所指定的日志输出位置默认为：sys.stderr

		log_common_file = os.path.join(os.path.dirname(__file__), 'log/common.log')
		log_error_file = os.path.join(os.path.dirname(__file__), 'log/error.log')
		log_format = '%(asctime)s : %(levelname)s : %(name)s : %(pathname)s : %(lineno)d : %(funcName)s : %(message)s'
		date_format = '%m/%d/%Y %H:%M:%S %p'
		# logging.basicConfig(
		# 	filename=log_file,
		# 	filemode='a',
		# 	level=logging.DEBUG,
		# 	format=log_format,
		# 	datefmt=date_format
		# )

		# a、通过Python代码实现日志配置
		# # 创建一个logger实例
		# logger = logging.getLogger('mylogger')
		# logger.setLevel(logging.DEBUG)
		#
		# # 定义两个formatter
		# rf_formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt=date_format)
		# f_formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
		#
		# # 创建两个处理器handler
		# rf_handler = logging.handlers.TimedRotatingFileHandler(
		# 	log_common_file,
		# 	when='midnight',
		# 	interval=1,
		# 	backupCount=7,
		# 	atTime=datetime.time(0, 0, 0, 0)
		# )
		# rf_handler.setFormatter(rf_formatter)
		#
		# f_handler = logging.FileHandler(log_error_file)
		# f_handler.setLevel(logging.ERROR)
		# f_handler.setFormatter(f_formatter)
		#
		# # 将handler加入到logger中
		# logger.addHandler(rf_handler)
		# logger.addHandler(f_handler)

		# b、通过配置文件和fileConfig()函数实现日志配置
		log_conf_file = os.path.join(os.path.dirname(__file__), 'config/log.ini')
		fileConfig(log_conf_file)

		logger = logging.getLogger('root')

		# c、通过字典信息和dictConfig()实现日志配置
		# ...

		# 打印日志
		logger.debug('This is a debug log.')
		logger.info('This is a info log.')
		logger.log(logging.WARNING, 'this is a warning log.')
		logger.error('this is a error log.')
		logger.critical('this is a critical log.')

		# 2、logging.basicConfig()函数
		# 该函数用于为logging日志系统做一些基本配置
		# logging.basicConfig()函数是一个一次性的简单配置工具，也就是说只有在第一次调用该函数时会起作用,
		#    后续再次调用该函数时完全不会产生任何操作的
		# 日志器（Logger）是有层级关系的,上面调用的logging模块级别的函数所使用的日志器是RootLogger类的实例,
		#    其名称为root,它是处于日志器层级关系最顶层的日志器，且该实例是以单例模式存在的
		# 如果要记录的日志中包含变量数据，可使用一个格式字符串作为这个事件的描述消息(logging.debug、logging.info等函数的第一个参数),
		#    然后将变量数据作为第二个参数*args的值进行传递
		# logging.debug()、logging.info()等方法的定义中，除了msg和args参数外，还有一个**kwargs参数。
		#    它们支持3个关键字参数: exc_info, stack_info, extra

		# 3、logging模块的四大组件
		# 日志器 Logger 提供了应用程序可一直使用的接口
		# 处理器 Handler 将logger创建的日志记录发送到合适的目的输出
		# 过滤器 Filter 提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
		# 格式器 Formatter 决定日志记录的最终输出格式
		# 简单点说就是：日志器(logger)是入口，真正干活儿的是处理器(handler)，处理器(handler)还可以通过过滤器(filter)和
		#    格式器(formatter)对要输出的日志内容做过滤和格式化等处理操作。
		# 与Logging四大组件相关的类：Logger Handler Filter Formatter
		#    logger = logging.getLogger()   # 获得一个Logger实例

		# 4、配置logging的几种方式
		# 4.1 使用Python代码显式的创建loggers, handlers和formatters并分别调用它们的配置函数
		# 4.2 创建一个日志配置文件，然后使用fileConfig()函数来读取该文件的内容
		# 4.3 创建一个包含配置信息的dict，然后把它传递个dictConfig()函数

		# 5、向日志输出中添加上下文信息
		# 5.1 通过向日志记录函数传递一个extra参数引入上下文信息
		# 5.2 使用LoggerAdapters引入上下文信息
		# 5.3 使用Filters引入上下文信息


def get_parser():
	# 默认情况下，ArgumentParser对象使用dest的值作为每个对象的“名字”。默认情况下，对于位置参数直接使用dest的值,
	# 对于可选参数则将dest的值变为大写
	parser = argparse.ArgumentParser(usage='我是一个测试命令', description='test command line argument', epilog='我是epilog')
	# nargs的不同值可能导致metavar使用多次
	parser.add_argument('num', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
	parser.add_argument(
		'--sum',
		dest='accumulate',
		action='store_const',
		const=sum,
		default=max,
		help='sum the integers(default: find the max)'
	)
	# 对于可选参数的动作，dest的动作通常从选项字符串推导出来
	parser.add_argument('-ver', '--verbosity', help='increase output verbosity')
	parser.add_argument('-e', help='whether to send email or not', action='store_true')
	parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0')
	# dest允许提供自定义的属性名
	parser.add_argument('--foo')
	return parser


def command_line_runner():
	parser = get_parser()
	args = parser.parse_args()

	print(args.accumulate(args.num))
	print(args.verbosity)
	print(args.e)
	print(args.foo)


if __name__ == '__main__':
	# Const.AUTHOR = 'yufeng1'   # 不能修改该常量

	# # 单例模式
	# instance_a = RequestUtil.RequestUtil('https://www.baidu.com')
	# instance_b = RequestUtil.RequestUtil('https://www.sina.com.cn')
	# print("实例a: ", instance_a)
	# print("实例b: ", instance_b)
	command_line_runner()

	# run = RunTest()
	# run.start_run()
