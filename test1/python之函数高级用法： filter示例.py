# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

L = range(100)
'''
filter(function, iterable)
函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
function -- 判断函数。
iterable -- 可迭代对象。
'''
print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()
'''
strip() 
用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
'''
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))