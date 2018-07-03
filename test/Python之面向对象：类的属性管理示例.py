# -*- coding: utf-8 -*-
'''
类实例的变量名以__开头，就变成了一个私有变量(private)，只有内部可以访问，外部不能访问

如果变量名以双下划线开头，并且以双下划线结尾(__xxx__)，它是特殊变量，特殊变量是可以直接访问的，表示private变量

如果变量名以一个下划线开头(_xxx)，这样的实例变量外部是可以访问的，但是按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是请把我看成私有变量，不要随意访问”
'''
# 类定义
class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

# 类初始化
obj = MyObject()

# 判断类属性是否存在
#hasattr() 函数用于判断对象是否包含对应的属性
print('hasattr(obj, \'x\') =', hasattr(obj, 'x')) # 有属性'x'吗？
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print('hasattr(obj, \'y\') =', hasattr(obj, 'y')) # 有属性'y'吗？
print('getattr(obj, \'y\') =', getattr(obj, 'y')) # 获取属性'y'
print('obj.y =', obj.y) # 获取属性'y'

# 获取属性
print('getattr(obj, \'z\') =',getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

# 获取属性
f = getattr(obj, 'power') # 获取属性'power'
print(f)
print(f())
