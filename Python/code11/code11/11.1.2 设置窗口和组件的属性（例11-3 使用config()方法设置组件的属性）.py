#11.1.2 设置窗口和组件的属性（例11-3 使用config()方法设置组件的属性）.py
from tkinter import *
win=Tk()    #创建窗口对象
label = Label()             #创建标签对象
label.config(text="Hello Python")    #配置组件文本属性
label.config(fg="white",bg="blue")   #配置组件前景和背景属性
label.pack()                #打包标签对象，使其显示在其父容器中
btn1= Button()              #创建按钮对象
btn1['text']="click"             #配置文本属性的另一种方法
btn1.pack()                 #打包按钮对象，使其显示在其父容器中
win.title("配置组件属性")    #title()方法设置窗口标题
win.geometry("300x200")    #geometry()方法设置窗口大小
win.mainloop()
