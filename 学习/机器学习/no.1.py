import numpy as np

# arr1=np.array([2,3,4])
# print(arr1)
# print(arr1.dtype)
#
# arr2=np.array([1.2,2.3,3.4])
# print(arr2)
# print(arr2.dtype)
#
# print(arr1+arr2)
#
# print(arr2*10)
#
# data=[[1,2,3],[4,5,6]]
# arr3=np.array(data)
# print(arr3)
# print(arr3.dtype)
#一维，全部为空
print (np.zeros(10))
#3行5列，全部为空
print (np.zeros((3,5)))
#全部为1
print(np.ones((4,6)))
#全部为空，不安全，随机添加
print(np.empty((2,3,2)))