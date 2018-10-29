#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: douban_login.py
# Date: 2018/6/5 16:18
#
# 豆瓣登录页面对象
__author__ = 'genghui'


from selenium.webdriver.common.by import By
from ui.base.base_page import BasePage
from ui.page.main_page import MainPage
from pageobject_support import callable_find_by as find_by
from ..element.douban_login import DoubanLoginElement


class DoubanLogin(BasePage):
    """
    登录页对象
    相当于业务操作类
    """

    # 定义页面标题
    title = '豆瓣'
    # 定义页面url
    url = "https://www.douban.com"

    def __init__(self, driver):
        """
        初始化Page Object
        :param driver: 驱动器对象
        """
        # 元素层对象
        self.__element_obj = DoubanLoginElement(driver)
        super().__init__(driver=driver)

        # 声明page object时，即打开页面
        # self.open(login_locators.get("login.url"))
        self.open(self.url)

    def get_title(self):
        """
        获取页面的title
        :return: 页面的title
        """
        return self._driver.title

    def is_loaded(self):
        """
        判断页面是否加载正常
        :return: True/False
        """
        return self.title == self.get_title()

    def is_target_page(self):
        pass

    def login(self, username, password):
        """
        登录操作(具体业务操作)
        :param username: 用户名
        :param password: 密码
        :return:
        """
        self.input(webElement=self.__element_obj.get_username_frame(), values=username)
        self.input(webElement=self.__element_obj.get_password_frame(), values=password)
        self.click(self.__element_obj.get_submit_btn())

        # 跳转到主页面，比较标题，判断登录是否成功
        return MainPage.title == self.get_title()
