#11.1.2 设置窗口和组件的属性（例11-2 设置了标题和大小的窗口）.py
from tkinter import *
win=Tk()    #创建窗口对象
label = Label(win,text="Hello,Python")  #创建标签对象
btn1= Button(win,text="click")          #创建按钮对象
label.pack()              #打包对象，使其显示在其父容器中
btn1.pack()               #打包对象，使其显示在其父容器中
win.title("Example11-2")  #title()方法设置窗口标题
win.geometry("300x200")   #geometry()方法设置窗口的大小
win.mainloop()



