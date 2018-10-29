#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
JSON工具模块

纯函数式模块
编码、解码JSON字符串
编码、解码JSON文件
"""

import json


def read(file):
	"""
	从json文件中读取数据
	:param file: json文件路径
	:return: 返回一个字典
	"""
	with open(file, 'r') as fp:
		data = json.load(fp)

	return data


def get_data(file, index):
	"""
	根据index获得数据
	:param file: json文件路径
	:param index: json key
	:return:
	"""
	data = read(file)   # 返回整个json文件的数据
	if index in data:
		return data[index]
	else:
		return ''


def write(data, file):
	"""
	向json文件中写入编码后的数据
	:param data: 要写入的数据
	:param file: 要写入数据的文件路径
	:return:
	"""
	try:
		with open(file, 'w') as fp:
			json.dump(data, fp)
	except Exception as e:
		print(str(e))
	finally:
		print("写入数据成功")


def encode(data):
	"""
	将Python对象编码为JSON字符串
	:param data: 待编码的数据
	:return: 返回json字符串
	"""
	json_str = json.dumps(data)
	return json_str


def decode(data):
	"""
	解析JSON字符串
	:param data: json字符串
	:return: 返回Python类型数据
	"""
	origin_data = json.loads(data)
	return origin_data


if __name__ == "__main__":
	# Python 字典类型转换为 JSON 对象
	data1 = {
		'no': 1,
		'name': 'hello world',
	}

	# write(data1, '1.json')
	output_data = read('1.json')
	# output_data = get_data('1.json', 'name')
	print(output_data)
