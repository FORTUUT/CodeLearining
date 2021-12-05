#13.1.4 numpy数组的算术运算（例13-11 通过指定axis参数计算numpy数组的特征值）
import numpy as np
myarr1=np.arange(12).reshape(3,4)
print(myarr1)
print(myarr1.sum(axis=0))  #计算每列和
print(myarr1.sum(axis=1))  #计算每行和
print(myarr1.max(axis=0))  #列最大值
print(myarr1.max(axis=1))  #行最大值
print(myarr1.cumsum(axis=1))  #计算每行累积和



