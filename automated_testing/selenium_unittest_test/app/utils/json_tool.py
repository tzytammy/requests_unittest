#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename: json.py
# date: 2018/6/21
# Author: genghui

"""
json.py

json格式数据的操作类

"""

import json
import os

# Python字典转换为 JSON对象
# data = {
#     'no': 1,
#     'name': 'Runoob',
#     'url': 'http://www.runoob.com'
# }
# json_str = json.dumps(data)   # 编码
# # print("原始Python数据为：", repr(data))
# print("JSON对象：", json_str)
#
# # JSON对象转换回Python数据类型
# data1 = json.loads(json_str)  # 解码
# print("原始Python字典为：", data1)


# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
# 读取数据
with open('test.json', 'r') as f:
    data2 = json.load(f)
    print(data2)





# # 写入JSON数据
# data3 = {
#     "python": "I am the best",
#     "java": "zhazha",
#     "php": "zhazha"
# }
# with open('test.json', 'w') as fp:
#     json.dump(data3, fp)


class Json(object):
    """JSON工具类库

    对json字符串进行解码、对Python数据类型进行编码操作
    对json文件进行载入操作、将json数据写入json文件

    """

    

    def __init__(self):
        pass

    def encode(self, data=None):
        """
        编码为JSON字符串
        :param data: 待编码数据
        :return:
        """
        pass

    def decode(self, json_str=None):
        """
        解码JSON字符串
        :param json_str: str 待解码的JSON字符串
        :return:
        """
        # TODO(genghui) Change this to use relations.
        # TODO(gh123icdi@126.com): Use a '*' here for string repeation.
        # TODO(genghui): 有待完善业务逻辑 2018年7月解决
        pass

    def read(self, file=None):
        """
        从json文件读取数据
        :param file:
        :return:
        """
        pass

    def write(self, file=None, json_data=None):
        """
        向json文件写入json数据
        :param file: file 要写入的json文件
        :param json_data: json 要写入的json数据
        :return:
        """
        str1 = "We all know that 'A' and 'B' are two capital letters."
        str2 = 'The teacher said: "Practice makes perfect" is a very famous proverb.'
        pass
