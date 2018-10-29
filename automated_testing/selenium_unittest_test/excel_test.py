#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename: excel_test.py
# date: 2018/6/19
# excel操作demo

__author__ = 'genghui'

from utils.excel import Excel
import os

path = os.getcwd()
file = os.path.join(path, 'test.xls')

# 实例化
excel_obj = Excel(file, 0)

# 读取数据
print(excel_obj.get_rows())
test_data = excel_obj.get_data(0)
for data in test_data:
    print(data)


# 新建excel文件
filled_data = [
                (u"网站名", u"域名", u"IP地址", u"端口号", u"网站负责人"),
                ("菁英汇", 'http://jyh.wshang.com', '127.0.0.1', '199', 'Allen'),
                ("宙斯CRM", 'http://crm.wshang.com', '127.0.0.1', '88', 'Mark'),
                ("数字化营销", 'http://youxiong.wshang.com', '127.0.0.1', '67', 'WangXianSen'),
            ]
new_file_path = os.path.join(path, 'python.xls')
old_file = os.path.join(path, '1.xls')
# Excel.new_file('工时统计表', new_file_path, True, (1, 1, filled_data))
Excel.write(old_file, (1, 1, filled_data))
