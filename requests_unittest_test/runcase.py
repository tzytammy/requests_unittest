#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: runcase.py
#
# CRM Requests + Unittest接口自动化测试
__author__ = 'genghui'


import unittest
import time
from app.case import TestOrderList
from HTMLTestRunner import HTMLTestRunner

# 构造测试集
suite = unittest.TestSuite()

# 加载测试用例
suite.addTest(TestOrderList.TestOrderIndex("test_get_list"))


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(suite)

    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 定义报告存放路径
    filename = './test_report/' + now + '_test_result.html'

    # 定义测试报告
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                            title="订单列表接口测试报告",
                            description="测试用例执行情况")
        # 运行测试
        runner.run(testunit)
