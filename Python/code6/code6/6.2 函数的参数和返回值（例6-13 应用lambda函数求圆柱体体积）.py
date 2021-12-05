#6.2 函数的参数和返回值（例6-13 应用lambda函数求圆柱体体积）
import math
area=lambda r:math.pi*r*r   #给匿名函数绑定一个名字area以便调用
volume=lambda r,h:math.pi*r*r*h  #给匿名函数绑定一个名字volume以便调用
print("{:6.2f}".format(area(2)))
print(volume(2,5))

