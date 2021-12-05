#8.1.2 导入模块（例8-2 使用from语句导入模块）
from random import random
print(random())  #返回0~1之间的随机小数
from random import *  #导入random模块中的所有对象
print(randint(10,20))  #返回两个整数之间的随机整数
print(uniform(5,10))   #返回两个整数之间的浮点数
from random import uniform as u
print(u(5,10))         #返回两个整数之间的浮点数

