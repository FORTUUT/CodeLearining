#13.2.3 绘制直方图条形图饼状图
# 例13-17 简单的条形图绘制.py
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(6,4))
y=[10,20,8.45,22,3,2,12]
x=np.arange(7)
plt.bar(x,y,color="blue",width=0.5)
plt.show()

