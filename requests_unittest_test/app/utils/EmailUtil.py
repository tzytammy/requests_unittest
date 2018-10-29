#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: EmailUtil.py

"""
邮件工具类
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class EmailUtil(object):

	def __init__(self, server_host, password, from_user, to_user_list):
		"""
		初始化发送邮件设置

		:param server_host: 发送邮件的邮件服务器
		:param password: 发送用户的密码
		:param from_user: 发送邮件的用户邮箱
		:param to_user_list: 接收邮件的用户邮箱列表
		"""
		self.server_host = server_host
		self.password = password
		self.from_user = from_user
		self.to_user_list = to_user_list
		self.server = self._init_server()

	def _init_server(self):
		"""
		邮件服务器初始化
		:return: 邮件服务器对象
		"""
		# # 1、第一种方法: 创建server时先不初始化，再调用connect()方法
		# # 创建SMTP对象
		# server = smtplib.SMTP()
		# # 创建与邮件服务器的连接
		# server.connect(self.server_host)

		# 2、第二种方法: 调用SMTP()方法时，传入初始化参数host和端口(25)
		server = smtplib.SMTP(self.server_host, 25)

		# 登录邮箱服务
		server.login(self.from_user, self.password)

		return server

	def send(self, subject, content):
		"""
		发送邮件
		:param subject: 邮件主题
		:param content: 邮件内容，用户可自定义
		:return:
		"""
		# 邮件正文中显示的发件人格式
		from_user_format = Header(str(self.from_user) + '<' + self.from_user + '>', 'utf-8')

		# 组装邮件主体
		message = MIMEText(content, _subtype='html', _charset='utf-8')
		message['Subject'] = Header(subject, 'utf-8')
		message['From'] = from_user_format
		message['To'] = ','.join(self.to_user_list)

		# 发送邮件
		try:
			self.server.sendmail(self.from_user, self.to_user_list, message.as_string())
		except smtplib.SMTPException as e:
			print(str(e))
		else:
			print("\n邮件报告发送成功")
		finally:
			self.server.quit()
