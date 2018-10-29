#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: runcase2.py
#
# CRM Requests + Unittest接口自动化测试
# 通过discover函数加载测试用例
__author__ = 'genghui'

import requests, unittest, json
import time
from HTMLTestRunner import HTMLTestRunner


# 定义测试用例的目录
test_dir = './app/case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test*.py')


if __name__ == '__main__':
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
        runner.run(discover)



