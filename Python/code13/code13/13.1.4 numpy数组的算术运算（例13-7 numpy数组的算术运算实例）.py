#13.1.4 numpy数组的算术运算（例13-7 numpy数组的算术运算实例）
import numpy as np
arr1=np.array([10,20,30,40])
arr2=np.arange(1,5)
print(arr1,arr2)
result1=arr1+arr2
result2=arr1-arr2
result3=arr1*arr2
result4=arr1/arr2
result5=arr2**2
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
result5=arr1<30
print(result5)