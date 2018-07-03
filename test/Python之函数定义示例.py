# -*- coding: utf-8 -*-

import math

'''
isinstance() 与 type() 区别：

type() 不会认为子类是一种父类类型，不考虑继承关系。

isinstance() 会认为子类是一种父类类型，考虑继承关系。
'''
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x, y, step, angle=0):
    #cos() 返回x的弧度的余弦值
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

n = my_abs(-20)
print(n)
#math.pi / 6
x, y = move(100, 100, 60, angle=0)
print(x, y)

# TypeError: bad operand type:
#my_abs(123)
my_abs('123')