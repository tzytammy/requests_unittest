# -*- coding: utf-8 -*-

def f(x):
    return x * x
'''
map(function, iterable, ...)
会根据提供的函数对指定序列做映射
function -- 函数，有两个参数
iterable -- 一个或多个序列
'''
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))