#11.3.2 Button组件（例11-10 单击Button计算1-100的累加值）.py
from tkinter import *
win=Tk()
win.title("Button Test")
win.geometry("300x200")
label1=Label(win,text='此处显示计算结果 ')
label1.config(font=('宋体',12))
label1.pack()
def computing():
    sum = 0
    for i in range(100+1):
        sum+=i
    result="累加结果是："+ str(sum)
    label1.config(text=result)  
str1='计算1-100累加值'
mybutton=Button(win,text=str1)	
mybutton.config(justify=CENTER)		#设置按钮文本居中
mybutton.config(width=20,height=3)		#设置按钮的宽和高
mybutton.config(bd=3,relief=RAISED)	#设置边框宽度和样式
mybutton.config(anchor=CENTER)			#设置内容在按钮内部居中
mybutton.config(font=('隶书',12,'underline'))		#设置按钮的字体字号下划线
mybutton.config(command=computing)    #指定单击按钮时的响应函数
mybutton.config(activebackground='yellow')
mybutton.config(activeforeground='red')
mybutton.pack()
win.mainloop()
