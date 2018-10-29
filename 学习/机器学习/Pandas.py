from pandas import Series,DataFrame

import pandas as pd

#定义一维数组
obj=Series([4,5,6,-7])
print(obj)


'''自动添加索引
0    4
1    5
2    6
3   -7
'''
#Pandas中索引是可以重复的

print(obj.index)
print(obj.values)
