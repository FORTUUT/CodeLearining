#11.3.3 Entry组件（例11-11 输入数据并计算累加和）.py
from tkinter import *
def computing():
    sum = 0
    n= int(number.get())
    for i in range(n+1):
        sum+=i
    result="累加结果是："+ str(sum)
    label3.config(text=result)
win=Tk()
win.title("Entry Test")
win.geometry("300x200")
label1=Label(win,text='请输入计算数据： ')  #标签组件1
label1.config(width=16,height=3)
label1.config(font=('宋体',12))
label1.grid(row=0,column=0)
number = StringVar()           #字符串类型的控制变量number
entry1 = Entry(win,textvariable = number,width=16)  #输入框组件，
# textvariable为获取组件内容的变量，Entry组件中的文本和控制变量的值会关联变化
entry1.grid(row=0,column=1)
label2=Label(win,text='请单击确认：')      #标签组件2
label2.config(width=14,height=3)
label2.config(font=('宋体',12))
label2.grid(row=1,column=0)
button1=Button(win,text="计算")           #按钮组件
button1.config(justify=CENTER)			#设置按钮文本居中
button1.config(width=14,height=2)		#设置按钮的宽和高
button1.config(bd=3,relief=RAISED)		#设置边框宽度和样式
button1.config(anchor=CENTER)			#设置内容在按钮内部居中
button1.config(font=('隶书',12))		
button1.config(command=computing)       #指定单击时响应函数
button1.grid(row=1,column=1)
label3=Label(win,text='显示结果 ')       #标签组件3
label3.config(width=16,height=3)
label3.config(font=('宋体',12))
label3.place(x=50,y=130)
win.mainloop()
