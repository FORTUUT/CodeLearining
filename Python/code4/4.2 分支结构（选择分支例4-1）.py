#4.2 分支结构（选择分支例4-1）.py
#分段函数计算，根据x的值，输出y的值
import math
x = -37
if x<0:
    y=math.fabs(x)
else:
    y=math.sqrt(x)
print("计算的结果是：",y)
