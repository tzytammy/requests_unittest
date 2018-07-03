#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: common.py
#
# 公共函数库
__author__ = 'genghui'

import os
import smtplib, unittest
import csv, json, xlrd
from email.mime.text import MIMEText
from email.header import Header

# 定义发送邮件
def send_mail(file_new, mail_server, from_mail_addr, to_mail_addr, from_pass):
    """ 发送邮件 """
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('订单列表接口自动化测试报告', 'utf-8')
    msg['From'] = Header(from_mail_addr + '<' + from_mail_addr + '>', 'utf-8')
    msg['To'] = '<' + to_mail_addr + '>'

    try:
        # 创建SMTP对象
        # server = smtplib.SMTP()
        # 创建与服务器主机的连接
        # server.connect(mail_server)
        server = smtplib.SMTP(mail_server, 25)

        # 登录邮箱服务
        server.login(from_mail_addr, from_pass)
        # 发送邮件
        server.sendmail(from_mail_addr, to_mail_addr, msg.as_string())
        server.quit()
        print('邮件已发出!请注意查收。')
    except smtplib.SMTPException as e:
        print(str(e))



# 查找测试目录，找到最新生成的测试报告
def new_report(test_report):
    """ 找到最新的测试报告 """
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report + '\\' + fn))

    file_new = os.path.join(test_report, lists[-1])

    print(file_new)
    return file_new


# 读取Excel
# 封装xlrd模块,实现参数化



# 写入Excel



# 读取CSV
def read_csv(file):
    """ file: csv文件名 """
    result = []
    try:
        with open(file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = {}
                data['id'] = row['id']
                data['url'] = row['url']
                data['token'] = row['token']
                data['mobile'] = row['mobile']
                data['email'] = row['email']

                if isinstance(row['expect'], dict):
                    data['expect'] = json.dumps(row['expect'])
                else:
                    data['expect'] = row['expect']
                result.append(data)
        return result
    except FileNotFoundError as e:
        print('文件不存在')
        return result

# 写入CSV
#def write_csv(file, content):




# 将用例添加到测试套件
def creatsuite(case_path):
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir = None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            print(testunit)
    return testunit