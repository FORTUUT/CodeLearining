# 11.3.6 Checkbutton组件（例11-14 Checkbutton组件操作示例）.py
from tkinter import *
win =Tk()
label1=Label(win,text='Checkbutton按钮测试')
label1.config(font=('宋体',18),justify=CENTER)
label1.grid(row=1,column=1,columnspan=2)
choice1=IntVar()   #控制变量1
choice1.set(0)
choice2=IntVar()   #控制变量2
choice2.set(0)
frame1=Frame(bd=0,relief=RIDGE)  #创建框架，框架中放置复选框1和2
frame1.grid(row=2,column=1)
check1=Checkbutton(frame1,text='粗体',variable=choice1,width=8,pady=10)  #创建复选框1
check1.grid(row=1,column=1)
check2=Checkbutton(frame1,text='斜体',variable=choice2,width=8)          #创建复选框2
check2.grid(row=1,column=2)
def changeFont():
    #temp=choice1.get()
    if choice1.get()==1 and choice2.get()==1:
        label1.config(font=('宋体',18,"bold italic"))
    elif choice1.get()==1 and choice2.get()==0:
        label1.config(font=('宋体',18,"bold"))
    elif choice1.get()==0 and choice2.get()==1:
        label1.config(font=('宋体',18,"italic"))
    else:
        label1.config(font=('宋体',18))      
check1.config(command=changeFont)   #单击复选框1时，执行函数
check2.config(command=changeFont)   #单击复选框2时，执行函数
win.geometry("240x150")
mainloop()
