#用海伦公式计算三角形面积
import math
a,b,c=3,4,5
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("三角形的面积是{:.2f}".format(s))