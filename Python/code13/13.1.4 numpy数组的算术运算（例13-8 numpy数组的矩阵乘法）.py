#13.1.4 numpy数组的算术运算（例13-8 numpy数组的矩阵乘法）
import numpy as np
lst1=[[1,2],[3,4]]
lst2=[[5,6],[7,8]]
arr1=np.array(lst1)
arr2=np.array(lst2)
print(arr1)
print(arr2)
result1=arr1*arr2
print(result1)
result2=np.dot(arr1,arr2)
print(result2)

