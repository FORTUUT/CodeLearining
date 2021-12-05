#8.5 turtle库的应用（例8-11 绘制图案为紫色正方形螺旋）
'''绘制图案为紫色正方形螺旋'''
import turtle
turtle.setup(400,360)
turtle.pensize(1)               #设置画笔宽度为2像素
turtle.pencolor("purple")       #设置画笔颜色为紫色
turtle.shape("turtle")          #设置画笔形状为“海龟”
turtle.speed(10)                #设置绘图速度为10
turtle.circle(2)
a=0                             #起始移动长度a为5单位
for i in range(40):             #循环40次
    a=a+6                       #移动长度a每次增加6单位
    turtle.left(90)             #画笔每次移动旋转90度
    turtle.fd(a)                #画笔向前移动a单位
turtle.hideturtle()             #隐藏画笔
turtle.done()                   #结束绘制