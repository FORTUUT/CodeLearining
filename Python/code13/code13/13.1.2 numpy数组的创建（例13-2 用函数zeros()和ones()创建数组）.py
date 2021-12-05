#13.2 numpy数组的创建（例13-2 用函数zeros()和ones()创建数组）
import numpy as np
lst2=[[1,2,3],[4,5,6]]
arr3=np.array(lst2)
print(arr3)
arr4=np.zeros((3,4))
print(arr4)
arr5=np.ones((3,4))
print(arr5)
print(arr5.dtype)
print(arr5.dtype.itemsize)

