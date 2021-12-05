#13.1.3 访问numpy数组的元素（例13-5 numpy数组的切片）
import numpy as np
arr0=np.arange(1,10)
print(arr0)
print(arr0[4])
print(arr0[2:4])
print(arr0[:5])
print(arr0[:-1])
arr0[2:4]=10,20   #修改数组元素的值
print(arr0)
print(arr0[::-1])     #数组翻转


