#13.1.5 numpy数组的形状操作（例13-13 使用resize()函数改变数组形状）
import numpy as np
yarr0=np.array([[12,31],[32,49],[34,41],[26,34],[43,3],[10,5]])
print(id(yarr0))
yarr0.resize((4,3))
print(yarr0)
print(id(yarr0))
