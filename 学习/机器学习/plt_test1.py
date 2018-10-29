import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

iris = pd.read_csv("./iris_training.csv")
#设置样式
sns.set(style="white", color_codes=True)
# 设置绘制格式为散点图
sns.jointplot(x="120", y="4", data=iris, size=5)
# distplot绘制曲线
sns.distplot(iris['120'])

# 没啥用，只是让pandas 的plot() 方法在pyCharm上显示
plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
#
# import warnings
# warnings.filterwarnings("ignore")
#
# iris = pd.read_csv("./iris_training.csv")
#
# sns.set(style="white", color_codes=True)


# FacetGrid 一般绘图函数
# hue 彩色显示分类0/1/2
# plt.scatter 绘制散点图
# add_legend() 显示分类的描述信息
# sns.FacetGrid(iris, hue="virginica", size=5).map(plt.scatter, "120", "4").add_legend()

# sns.FacetGrid(iris, hue="virginica", size=5).map(plt.scatter, "setosa", "versicolor").add_legend()
# # 没啥用，只是让pandas 的plot() 方法在pyCharm上显示
# plt.show()