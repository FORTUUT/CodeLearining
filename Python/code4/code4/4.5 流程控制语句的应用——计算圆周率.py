#4.5 流程控制语句的应用——计算圆周率
#例4-15 使用蒙特卡罗方法（随机数+概率）计算圆周率
import random
NUMBER = 100000  #随机产生10000个点
n = 0
for i in range(NUMBER):#循环10000次调用随机函数
    x = random.random() * 2 - 1  #横坐标
    y = random.random() * 2 - 1  #纵坐标
    if ((x * x + y * y) <= 1): #判断是否在圆内
        n+=1                #统计落在圆内的点数
pi = 4.0 * n / NUMBER       #计算pi值
print("使用蒙特卡罗方法计算圆周率的值是：",pi)
