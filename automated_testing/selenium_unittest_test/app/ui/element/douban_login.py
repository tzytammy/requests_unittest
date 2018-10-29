#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: douban_login.py
# Date: 2018/6/11 11:49
#
# 豆瓣登录页面对象
__author__ = 'genghui'


from selenium.webdriver.common.by import By
from selenium_unittest_test.app.ui.base.base_page import BasePage
from selenium_unittest_test.app.ui.page.main_page import MainPage
from pageobject_support import callable_find_by as find_by


class DoubanLoginElement(BasePage):
    """
    豆瓣登录页元素类
    """

    def __init__(self, driver):
        super().__init__(driver=driver)

    def get_username_frame(self):
        return self.find((By.ID, 'form_email'))
        #return find_by(id_='form_email')()

    def get_password_frame(self):
        return self.find((By.ID, 'form_password'))

    def get_submit_btn(self):
        return self.find((By.XPATH, "//input[@class='bn-submit']"))

    def is_target_page(self):
        pass

