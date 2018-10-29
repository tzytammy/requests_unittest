#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: base_case.py
#
# 测试用例基础库

__author__ = 'genghui'



from time import sleep
import unittest

class BaseCase(unittest.TestCase):


    def setUp(self):
        """
        初始化
        :return:
        """
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self):
        """
        析构函数
        :return:
        """
        self.driver.quit()