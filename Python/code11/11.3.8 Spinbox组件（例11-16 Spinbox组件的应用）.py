# 11.3.8 Spinbox组件（例11-16 Spinbox组件的应用）.py
from tkinter import *
win=Tk()
win.geometry("300x200")     #geometry()方法
label1=Label(text='请选择评语和成绩')
label1.pack(expand=1,fill=X)
label1.config(font=('隶书',15))
label2=Label()
label2.config(font=('宋体',18))
label2.pack()
subject=StringVar()  #控制变量1——科目
score=IntVar()       #控制变量2——分数
spin1=Spinbox(textvariable=subject,value=('语文','数学','外语'),wrap=True)  #创建滚动选择组件1
spin1.pack()
spin2=Spinbox(textvariable=score,from_=60,to=100,increment=5,wrap=True)   #创建滚动选择组件2
spin2.pack()
def change():    #获得科目和分数值，显示在标签上
    label2.config(text=subject.get()+str(score.get()))
button1=Button(text="确定",command=change)   #单击按钮时，执行函数

button1.pack()
win.mainloop()
