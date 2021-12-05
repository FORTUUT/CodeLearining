#11.3.5 Radiobutton组件（例11-13 单选按钮组操作示例）.py
from tkinter import *

win =Tk()
label1=Label(win,text='请为您最喜欢的体育项目投票')
label1.grid(row=1,column=1,columnspan=2)

s_items=IntVar()  #控制变量s_items与单选框选项有关
s_items.set(2)

frame1=Frame(bd=2,relief=RIDGE)
frame1.grid(row=2,column=1)

frame2=Frame(bd=0,relief=RIDGE)
frame2.grid(row=2,column=2)

radio1=Radiobutton(frame1,text='足球',variable=s_items,value=1,width=8)  #创建单选框1
radio1.grid(row=1,column=1)
radio2=Radiobutton(frame1,text='排球',variable=s_items,value=2)          #创建单选框2
radio2.grid(row=2,column=1)
radio3=Radiobutton(frame1,text='篮球',variable=s_items,value=3)          #创建单选框3
radio3.grid(row=3,column=1)

num1=IntVar()   #控制变量num1与输入框1有关
entry1 = Entry(frame2,textvariable=num1,width=10,state = 'readonly')     #输入框1（只读）
entry1.grid(row=1,column=1,pady=4)
num2=IntVar()   #控制变量num2与输入框2有关
entry2 = Entry(frame2,textvariable=num2,width=10,state = 'readonly')     #输入框2（只读）
entry2.grid(row=2,column=1,pady=4)
num3=IntVar()   #控制变量num3与输入框3有关
entry3 = Entry(frame2,textvariable=num3,width=10,state = 'readonly')     #输入框3（只读）
entry3.grid(row=3,column=1,pady=4)

def voting():
    global num1,num2,num3
    temp=s_items.get()        #s_items与单选框选项有关，获得单选选项值1/2/3
    if temp==2:
        num2.set(num2.get()+1)   #num2与输入框2的输出显示有关
    elif temp==1:
        num1.set(num1.get()+1)   #num1与输入框1的输出显示有关
    else:
        num3.set(num3.get()+1)   #num3与输入框3的输出显示有关

btn1=Button(win,text="请投票",command=voting)   #单击请投票按钮时，执行投票函数
btn1.grid(row=3,column=1,columnspan=2,pady=5)

win.geometry("300x200")
mainloop()
