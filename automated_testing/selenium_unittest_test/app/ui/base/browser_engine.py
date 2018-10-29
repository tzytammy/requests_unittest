#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: browser_engine.py
# Date: 2018/6/5 16:18
#
# 浏览器引擎基类
__author__ = 'genghui'

import os

from selenium import webdriver
from selenium_unittest_test.app.config import settings


class BrowserEngine(object):

    def __init__(self, browser=None):
        """
        初始化浏览器类型
        :param browser:
        """
        if browser is None:
            self._browser_type = settings.DEFAULT_BROWSER
        else:
            self._browser_type = browser
        self._driver = None

    def init_driver(self):
        """
        初始化驱动器
        :return: 返回驱动器
        """
        if self._browser_type.lower() == 'chrome':
            self._driver = webdriver.Chrome()
        elif self._browser_type.lower() == 'firefox':
            self._driver = webdriver.Firefox()
        elif self._browser_type.lower() == 'ie':
            self._driver = webdriver.Ie()
        else:
            ValueError('传入的浏览器类型错误,目前仅支持Chrome/Firefox/IE.')

        self._driver.implicitly_wait(time_to_wait=settings.UI_WAIT_TIME)   # 设置隐式等待时间
        return self._driver