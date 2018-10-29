#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: douban_login.py
# Date: 2018/6/5 16:18
#
# 登录成功后的页面对象
__author__ = 'genghui'


from selenium_unittest_test.app.ui.base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    title = '豆瓣首页'

    def __init__(self):
        pass
