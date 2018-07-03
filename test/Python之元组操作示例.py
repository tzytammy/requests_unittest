# -*- coding: utf-8 -*-

# 定义并初始化元组
classmates = ('Michael', 'Bob', 'Tracy')

# 打印元组内容
print('classmates =', classmates)

# 计算元素长度
print('len(classmates) =', len(classmates))

# 通过索引获取指定位置元组
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# 尝试修改元组，这个会抛异常，因为元组是不可修改的，只能读
#classmates[0] = 'Adam'