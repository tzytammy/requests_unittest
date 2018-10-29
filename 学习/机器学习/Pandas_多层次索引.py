from pandas import Series,DataFrame
import numpy as np
import pandas as pd
from numpy import nan as NA

#是从标准正态分布中返回一个或多个样本值
data3=Series(np.random.randn(10),
             index=[['a','a','a','b','b','b','c','c','d','d'],
                    [1,2,3,1,2,3,1,2,2,3]])

print(data3)
#
# print(data3['b'])
# print(data3['b':'c'])

print(data3.unstack())
print(data3.unstack().stack())
