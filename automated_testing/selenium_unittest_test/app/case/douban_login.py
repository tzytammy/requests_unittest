#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: douban_login.py
#
# 豆瓣首页登录用例

__author__ = 'genghui'

import time
import sys
import requests
import unittest
from ui.base.browser_engine import BrowserEngine
from ui.page.douban_login import DoubanLogin
# sys.path.append('')

class DoubanTest(unittest.TestCase):
    """
    首页登录测试用例类
    """

    def setUp(self):
        """
        用于初始化
        :return:
        """
        self.driver = BrowserEngine(browser='chrome').init_driver()     # 初始化驱动器
        self.login_obj = DoubanLogin(driver=self.driver)                # 初始化页面对象
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_one(self):
        """
        豆瓣首页登录
        :return:
        """
        # 替换为测试用的用户名、密码
        username = 'gh123icdi@qq.com'
        password = '123'
        self.assertEqual(True, self.login_obj.login(username=username, password=password))      # 调用登录方法

    def test_login_two(self):
        """
        豆瓣首页登录
        :return:
        """
        username = 'gH123icdi@qq.com'
        password = '456'
        self.assertEqual(False, self.login_obj.login(username=username, password=password))      # 调用登录方法

    def test_login_three(self):
        """
        豆瓣首页登录
        :return:
        """
        username = 'gh123icdi@qq.com'
        password = ' abc'
        self.assertEqual(True, self.login_obj.login(username=username, password=password))      # 调用登录方法

    def test_login_four(self):
        """
        豆瓣首页登录
        :return:
        """
        username = 'gh123icdi@qq.com'
        password = 'acF234 '
        self.assertEqual(True, self.login_obj.login(username=username, password=password))      # 调用登录方法

    def test_login_five(self):
        """
        豆瓣首页登录
        :return:
        """
        username = 'gh123icdi@qq.com'
        password = 'abc  234'
        self.assertEqual(True, self.login_obj.login(username=username, password=password))      # 调用登录方法

    def test_page_loading(self):
        """
        页面是否加载正常
        :return:
        """
        self.assertEqual(True, self.login_obj.isLoaded())

    def test_title(self):
        """
        页面标题是否相同
        :return:
        """
        self.assertEqual(DoubanLogin.title, self.login_obj.getTitle())

    def tearDown(self):
        """
        析构方法
        :return:
        """
        # 关闭浏览器
        #self.driver.close()
        self.driver.quit()
        #self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    unittest.main()