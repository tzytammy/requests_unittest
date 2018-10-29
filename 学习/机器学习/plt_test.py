import matplotlib.pyplot as plt

#绘制简单的曲线
# plt.plot([1,3,5],[4,8,10])
# plt.show()

import numpy as np
#x轴的定义域为-3.14~3.14，中间间隔100个元素
# x=np.linspace(-np.pi,np.pi,100)
# plt.plot(x,np.sin(x))
# plt.show()

# y=np.linspace(-np.pi*2,np.pi*2,100)
# plt.figure(1,dpi=50) #创建图标1
# #dpi=50 dpi表示精度，绘画图形的详细程度，精度越高，所产生图片体积越大
# for i in range(1,5): #画四条线
#     plt.plot(y,np.sin(y/i))
# plt.show()

#创建图标1，dpi代表图片精细度，dpi越大文件越大，杂志要300以上
# plt.figure(1,dpi=50)
# data=[1,1,1,2,2,2,3,3,4,5,5,6,4]
# #只要传入数据，直方图就会统计数据出现的次数
# plt.hist(data)
# plt.show()

x=np.arange(1,10)
y=x
fig=plt.figure()
#c='r'表示散点的颜色为红色，marker 表示指定散点的形状为圆形
plt.scatter(x,y,c='r',marker='o')
plt.show()
