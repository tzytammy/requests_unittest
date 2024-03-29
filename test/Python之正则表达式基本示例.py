# -*- coding: utf-8 -*-
#Regular Expression 正则表达式
import re

print('Test: 010-12345')
#match() 函数只在字符串的开始位置尝试匹配正则表达式，也就是只报告从位置 0 开始的匹配情况
# 而 search() 函数是扫描整个字符串来查找匹配。如果想要搜索整个字符串来寻找匹配，应当用 search()。
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(1), m.group(2))

t = '19:05:30'
print('Test:', t)

m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)

print(m.groups())
