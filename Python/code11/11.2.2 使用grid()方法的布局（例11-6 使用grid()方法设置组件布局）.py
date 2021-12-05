#11.2.2 使用grid()方法的布局（例11-6 使用grid()方法设置组件布局）.py
from tkinter import *
win=Tk()
label1 = Label(win,text="请选择下列操作",fg="green")
label1.grid(row=0,column=0,columnspan=4)    #标签位于第0行第0列，跨4列
btn1= Button(text="copy")
btn2= Button(text="cut")
btn3= Button(text="paste")
btn4= Button(text="delete")
btn1.grid(row=2,column=0,padx=2)   #按钮1位于第2行第0列，外部预留2像素宽
btn2.grid(row=2,column=1,padx=2)   #按钮1位于第2行第1列，外部预留2像素宽
btn3.grid(row=2,column=2,padx=2)   #按钮1位于第2行第2列，外部预留2像素宽
btn4.grid(row=2,column=3,padx=2)   #按钮1位于第2行第3列，外部预留2像素宽
win.title("grid()布局")    #title()方法
win.geometry ("200x150")   #geometry()方法
win.mainloop()


