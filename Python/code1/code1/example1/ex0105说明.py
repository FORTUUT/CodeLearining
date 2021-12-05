# program0105.py
'''
输入三角形三条边，有海伦公式计算三角形面积s。
在对三边进行了异常处理基础上，判断3边符合三角形条件。
'''
import math
try:
    a=eval(input("请输入a边长：")) #——用户键盘输入
    b=eval(input("请输入b边长：")) #——用户键盘输入
    c=eval(input("请输入c边长：")) #——用户键盘输入
except NameError:   #异常处理——处理
    print("请输入正数数值") #异常提示——输出
if a<0 or b<0 or c<0:  #分析判断——处理
    print("输入数据不可以为负数") #提示信息——输出
elif a+b<=c or a+c<=b or b+c<=a: #分析判断——处理
     print("不符合两边之和大于第三边原则")  #提示信息——输出
else:   
    p = (a + b + c) / 2         #三边和的一半计算——处理
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))  #海伦公式计算面积——处理
    print("三角形的面积是{:.2f}".format(s))   #输出面积——输出

