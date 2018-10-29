from pandas import Series,DataFrame

import pandas as pd
#
# data={'city':['shanghai','shanghai','shanghai','beijing','beijing'],
#       'year':[2016,2017,2018,2017,2018],
#        'pop':[1.5,1.7,3.6,2.4,2.9 ]}
# frame=DataFrame(data)
# frame2=DataFrame(data,columns=['year','city','pop'])
# # print(frame)
# # print(frame2)
# # print(frame2['city'])
# # print(frame2.year)
#
# frame2['new']=100
# print(frame2)
# frame2['cap']=frame2.city=='beijing'
# print (frame2)
#
# pop={'beijing':{2008:1.5,2009:2.0},
#      'shanghai':{2008:2.0,2009:3.6}
#      }
#
# frame3=DataFrame(pop)
# print(frame3)
# #行列互换
# print(frame3.T)
#
# obj4=Series([4.5,7.2,-5.3,3.6],index=['b','d','c','a'])
# #按照索引重新排序,fill_value填充
# obj5=obj4.reindex(['a','b','c','d','e'],fill_value=0)
#
# print(obj5)
#
# obj6=Series(['blue','purple','yellow'],index=[0,2,4])
# #利用上面的内容进行填充
# print(obj6.reindex(range(6),method='ffill'))
# #利用下面的内容进行填充
# print(obj6.reindex(range(6),method='bfill'))
#
#
from numpy import nan as NA
#
# data=Series([1,NA,2])
# print(data)
# print(data.dropna())


data2=DataFrame([[1.,6.5,3],[1.,NA,NA],[NA,NA,NA]])
# print(data2)
# #只要出现NA就会被删除
# print(data2.dropna())
# #删除行全是NA的
# print(data2.dropna(how='all'))
# #删除整列都是NA的
data2[4]=NA
# print(data2)
# print(data2.dropna(axis=1,how='all'))

#缺失值填充为0
data2.fillna(0)
print(data2.fillna(0))
print(data2)
print(data2.fillna(0,inplace=True))
#print(data2)




