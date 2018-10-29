#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: base_page.py
#
# Page Object基类
# 封装常用的元素操作方法

# page_objects封装了Selenium的一些方法，我们不需要通过driver.find_element_by_xpath()等来查找元素，转而用
# pageelement（locator）这样的方式来定位
# 每个子类，都应该实现抽象类里的抽象方法
__author__ = 'genghui'

import time
import page_objects
import logging
from abc import abstractmethod
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_unittest_test.app.config import settings
from pageobject.locator import Locator


class BasePage(object):
    """
    元素的基础操作类, 扮演了操作层的角色
    """
    base_url = None

    def __init__(self, driver):
        """
        初始化驱动器、url
        :param driver:
        :param url:
        """
        self._driver = driver
        self.log_obj = None      # 日志对象

    @abstractmethod
    def is_target_page(self):
        pass


    def open(self, url):
        """
        打开指定URL
        :param url: 待打开的url
        :return:
        """
        self._driver.maximize_window()
        self._driver.get(url)
        time.sleep(2)
        assert self._driver.current_url == url, "Dit not land on %s" % url

    def find(self, *locator, timeout=None):
        """
        定位元素
        :param locator: 元素定位器
        :param timeout: 超时时间
        :return: 元素对象
        """
        try:
            return self._init_wait(timeout).until(
                EC.visibility_of_element_located(locator=locator)
            )
        except NoSuchElementException:
            self._driver.close()
            raise NoSuchElementException(msg='元素定位失败,定位方式为:{}'.format(locator))
        except TimeoutException:
            self._driver.close()
            raise TimeoutException(msg='元素定位失败,定位方式为:{}'.format(locator))

    def click_by_locator(self, *locator, timeout=None, is_button=True):
        """
        单击元素
        :param locator: 定位器
        :param timeout:  超时时间
        :param is_button: 是否是按钮
        :return:
        """
        if is_button:
            self.find(locator, timeout).click()
        else:
            ActionChains(self._driver).click(self.find(locator, timeout)).perform()

    def click(self, webElement):
        """
        元素直接点击操作
        :param webElement:
        :return:
        """
        webElement.click()


    def input(self, webElement, values):
        """
        向文本输入框输入文本内容
        :param webElement: 元素对象
        :param values: 文本值
        :return:
        """
        webElement.clear()
        webElement.send_keys(values)

    def iframe(self, iframe_id):
        """
        获得iframe元素
        :param iframe_id: frame标识
        :return:
        """
        return self._driver.switch_to.frame(iframe_id)

    def iframe_out(self):
        """
        回到主页面对象
        :return:
        """
        return self._driver.switch_to.default_content()

    def _init_wait(self, timeout=5):
        """
        设置(显式)等待时间
        :param timeout: 超时时间
        :return: 返回wait对象
        """
        if timeout is None:
            return WebDriverWait(driver=self._driver, timeout=settings.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver, timeout=timeout)

    def write(self, msg, level='error'):
        """
        写入日志
        :param msg:
        :param level:
        :return:
        """
        self.log_obj.write(msg, level)

    @property
    def xpath(self):
        """
        获得Xpath
        :return:
        """
        return


class InvalidPageException(Exception):
    pass
