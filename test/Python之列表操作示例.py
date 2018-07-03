# -*- coding: utf-8 -*-

# 定义并初始化列表对象
classmates = ['Michael', 'Bob', 'Tracy']

# 打印列表内容
print('classmates =', classmates)

# 计算列表长度
print('len(classmates) =', len(classmates))

# 通过索引获取指定列表元素
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

#pop 删除指定索引值的元素,返回值为当前删除的元素的值。不指定索引值，默认删除最后一个元素
classmates.pop()
print('classmates =', classmates)
classmates.pop(1)

#append  列表添加元素，添加至列表末尾
classmates .append('5')
print ('classmates=',classmates)

#count 统计指定元素在列表中的个数
print(classmates.count('5'))

#  extend  迭代字符元素或列表元素
love=['L','O','V','E']

classmates.extend(love)
print ('classmates=',classmates)

#index  定位列表中指定元素
print(classmates.index('O'))

# insert  在指定索引位置的元素前面插入新的元素
classmates.insert(2,'tammy')
print ('classmates=',classmates)


#remove 删除列表中指定的元素
classmates.remove('5')
print ('classmates=',classmates)


#reverse 用于反向列表中的元素
classmates.reverse()
print ('classmates=',classmates)

#sort 对列表中的元素进行排序
classmates.sort()
print ('classmates=',classmates)