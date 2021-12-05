#13.2.3 绘制直方图条形图饼状图
# 例13-16 正态分布随机数的范围分布直方图示例.py
import matplotlib.pyplot as plt
import numpy as np
mu=100       #设置起始值
sigma=20     #每个点的放大倍数
x=mu+sigma*np.random.randn(20)   #为简单直观，样本量取20
plt.hist(x,bins=10,color='green',density=True)
print(x)
plt.show()
#plt.hist(x,bins=30,color='green',density=True)

