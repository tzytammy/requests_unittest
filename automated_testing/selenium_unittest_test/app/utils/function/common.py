#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: common.py
# Date: 2018/6/8 13:57
#
# 公共函数库
__author__ = 'genghui'


from selenium import webdriver
import os


def insert_img(driver, file_name):
    """
    截屏函数
    :param driver: 驱动器
    :param file_name: 文件名
    :return:
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/mail')[0]
    file_path = base + '/mail/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)