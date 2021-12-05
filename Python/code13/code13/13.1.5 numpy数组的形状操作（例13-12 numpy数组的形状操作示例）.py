#13.1.5 numpy数组的形状操作（例13-12 numpy数组的形状操作示例）
import numpy as np
yarr0=np.int32(50*np.random.rand(3,4))
print(yarr0)
yarr1=yarr0.ravel()  #降低数组的维度
print(yarr1)
yarr0.shape=(6,2)  #与yarr0.reshape(6,2)等价
print(yarr0)
yarr2=yarr0.transpose()
print(yarr2)
print(id(yarr2))
print(yarr2.transpose())
print(id(yarr2))

