from pandas import Series,DataFrame

import pandas as pd

obj2=Series([4,7,-5,3],index=['d','b','c','a'])

print(obj2)

obj2['c']=6
print(obj2)

print('f' in obj2)

#字典变数组
sdata={'beijing':3500,'shanghai':60000}
obj3=Series(sdata)
print(obj3)


obj3.index=['bj','sh']
print(obj3)
