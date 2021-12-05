#13.1.4 numpy数组的算术运算（例13-9 numpy数组中操作符及其应用）
import numpy as np
arr1=np.ones((2,3))
arr2=np.random.rand(2,3)
print(arr1)
arr1*=3   #arr1数组内容发生改变
print(arr1)
print(arr2)
print(id(arr2))
arr2+=arr1   #arr2数组发生内容改变
print(arr2)
print(id(arr2))


