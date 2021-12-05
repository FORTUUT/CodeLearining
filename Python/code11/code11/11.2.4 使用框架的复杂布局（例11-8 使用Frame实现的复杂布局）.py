#11.2.4 使用框架的复杂布局（例11-8 使用Frame实现的复杂布局）.py
from tkinter import *
win=Tk()
frma = Frame()      #框架frma
frmb = Frame()      #框架frmb
frma.pack()   #打包框架对象，使其显示在其父容器中
frmb.pack()   #打包框架对象，使其显示在其父容器中
lblUname = Label(frma,text="UserName",width=10,fg="black")  #创建用户名标签
etyUname = Entry(frma,width=20)   #创建用户名输入框
lblUname.grid(row=1,column=1)     #用户名标签布局
etyUname.grid(row=1,column=2)     #用户名输入框布局
lblPwd = Label (frma,text="PassWord",width=10,fg="black")  #创建密码标签
etyPwd = Entry(frma,width=20)     #创建密码输入框
lblPwd.grid(row=2,column=1)       #密码标签布局
etyPwd.grid(row=2,column=2)       #密码输入框布局
#向容器中用grid()方法添加两个按钮
btnReset= Button (frmb,text="ReSet",width=10)    #创建重置按钮对象
btnSubmit= Button (frmb,text="Submit",width=10)  #创建提交按钮对象
btnReset.grid(row=1,column=1)     #布局重置按钮对象
btnSubmit.grid(row=1,column=2)    #布局提交按钮对象
win.title("Example11-8")          #窗口标题
win.geometry ("300x200")          #窗口大小
win.mainloop()

