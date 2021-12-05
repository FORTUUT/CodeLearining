#13.1.3 访问numpy数组的元素（例13-6 二维数组的切片操作）
import numpy as np
arr0=np.random.rand(3,4)
print(arr0)
e1=arr0[0,2]  #第0行第2个元素
print("第0行第2个元素{}".format(e1))
e2=arr0[:2]   #第0行和第1行元素
print("第0行和第1行元素{}".format(e2))
e3=arr0[:,1]  #所有行第1列元素
print("所有行第1列元素{}".format(e3))
e4=arr0[1,:]  #第1行所有元素，与e4=arr0[1]同
print("第1行所有元素{}".format(e4))
e5=arr0[2,2:]  #第2行第2个元素后的所有元素
print("第2行第2个元素后的所有元素{}".format(e5))
e6=arr0[0:3,2] #每行的第2个元素
print("每行的第2个元素{}".format(e6))
e7=arr0[:,2]   #每行的第2个元素
print("每行的第2个元素{}".format(e7))

