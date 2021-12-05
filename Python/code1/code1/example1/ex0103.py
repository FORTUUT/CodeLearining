# program0103.py
# 输入三角形三条边，有海伦公式计算三角形面积s。
import math #导入math模块，可使用平方根方法
a=eval(input("请输入a边长："))
b=eval(input("请输入b边长："))
c=eval(input("请输入c边长："))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("三角形的面积是{:.2f}".format(s))
