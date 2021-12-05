# 13.2.2 matplotlib.pyplot库中的函数
# 例 在绘图对象中绘制多个子图
import numpy as np
import matplotlib.pyplot as plt
for idx,color in enumerate('rgbyck'):
    temp=1+idx
    plt.subplot(3,2,temp,facecolor=color)
plt.show()



