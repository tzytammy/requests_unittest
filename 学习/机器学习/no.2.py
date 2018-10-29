import numpy as np
#产生从0到9的整数
print(np.arange(10))


arr4=np.arange(10)
#从0开始的
print(arr4[5])
print(arr4[5:8])
arr4[5:8]=10
print(arr4)



#重新复制不改变原有数组
arr_slice=arr4[5:8].copy()
#arr_slice 从第一个元素到最后一个元素全部赋值15
arr_slice[:]=15
print(arr_slice)
print(arr4)