#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: base_element.py
#
# 页面元素控件基类


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class BaseTextElement(object):
    """ 文本框元素 """

    def __set__(self, obj, value):
        """ Sets the text to the value supplied """
        dr = obj.driver
        WebDriverWait(dr, 100).until(
            lambda driver: driver.find_element(self.locator)
        )
        dr.find_element(self.locator).clear()
        dr.find_element(self.locator).send_keys(value)

    def __delete__(self, obj):
        pass

    def __get__(self, obj, owner):
        """ Gets the text of the specified object """
        pass
