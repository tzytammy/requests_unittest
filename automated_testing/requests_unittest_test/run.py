#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: run.py
"""
测试入口文件

"""
import sys
import os
import time
import unittest
import argparse

from app.libs.HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport
from app.utils import GlobalFunction
from app.utils.EmailUtil import EmailUtil
from app.utils import Config

# 将测试框架根目录添加到Python的系统搜索路径中
sys.path.append("E:\Python\auto_testing\auto_test_framework\requests_unittest_test")


def send_email(is_send_email, content):
	"""
	发送邮件
	:param is_send_email: 是否发送邮件, True-发送, False-不发送给
	:param content: 邮件主体内容
	:return:
	"""
	# email为True,则发送邮件
	if is_send_email:
		# 邮件服务器地址
		config = Config.ConfigUtil(os.path.join(os.path.dirname(__file__), 'config/mail.ini'))
		mail_server_host = config.get_option_value_by_section('email', 'mail_server_host')
		# 发件人地址
		from_mail_address = config.get_option_value_by_section('email', 'from_mail_address')
		# 收件人地址
		to_mail_address = config.get_option_value_by_section('email', 'to_mail_address').split(',')

		# 邮件主题
		subject = '接口自动化测试报告'

		# 126 163 开启客户端授权密码登录模式
		# 发件人客户端第三方登录邮件服务器密码
		from_mail_pass = config.get_option_value_by_section('email', 'from_mail_pass')

		# 发送邮件
		email_obj = EmailUtil(mail_server_host, from_mail_pass, from_mail_address, to_mail_address)
		email_obj.send(subject, content)
	return


def get_parser():
	"""
	获得命令行参数解析器对象
	:return:
	"""
	parser = argparse.ArgumentParser(
		prog='tw_auto_tf',
		description='test command line argument',
		epilog='最后再瞅我一眼吧^^'
	)

	parser.add_argument('report_type', metavar='N', type=int, nargs='?', default=1, choices=(1, 2), help='请输入生成报告的类型')
	parser.add_argument('-e', '--email', help='whether to send email or not', action='store_true')
	parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0')

	return parser


def command_line_runner():
	if sys.version < '3':
		raise SystemExit('请使用Python 3.0.0以上的版本^^')

	# 获得命令行参数解析器
	parser = get_parser()

	# 解析命令行参数
	args = parser.parse_args()
	report_type = args.report_type

	# 当前文件所在目录
	current_file_dir = os.path.dirname(__file__)

	# 定义测试用例的目录
	test_dir = os.path.join(current_file_dir, 'app/case')

	# 定义测试套件
	suite = unittest.defaultTestLoader.discover(test_dir, pattern='Test*.py')
	# suite1 = unittest.TestLoader().loadTestsFromModule(TestLogin)
	# suite2 = unittest.defaultTestLoader.discover(test_dir, pattern='Test*.py')
	# suite = unittest.TestSuite([suite1, suite2])

	# 按照一定的格式获取当前的时间
	now = time.strftime("%Y-%m-%d %H_%M_%S")

	# 定义报告存放路径、报告文件名
	test_report_path = os.path.join(current_file_dir, 'report/')
	filename = now + "_test_result.html"

	if report_type == 1:
		# 使用HTMLTestRunner生成测试报告
		with open(test_report_path + filename, 'wb') as fp:
			runner = HTMLTestRunner(stream=fp, title="测试统计报告", description="测试用例执行统计报告")
			runner.run(suite)

		# 最新测试报告
		new_report_file = GlobalFunction.new_report(test_report_path)

		# 邮件内容, 这里读取最新的一个测试报告
		with open(new_report_file, 'rb') as fp:
			mail_content = fp.read()
	elif report_type == 2:
		# 使用BeautifulReport生成测试报告
		result = BeautifulReport(suite)
		result.report(filename=filename, description="测试用例执行统计报告", log_path=test_report_path)
		# 可以从result中获取用例个数
		mail_content = "用例总数为{total}, 成功用例个数为{success}, 失败用例个数为{failure}, 错误用例个数为{error}".format(
			total=result.testsRun,
			success=result.success_count,
			failure=result.failure_count,
			error=result.error_count
		)

	# 发送邮件
	send_email(args.email, mail_content)


if __name__ == '__main__':
	command_line_runner()
