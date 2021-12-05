#11.2.1 使用pack()方法的布局
# 例11-5 使用pack()方法的anchor参数设置组件的布局.py
from tkinter import *
win=Tk()
label1 = Label(win,text="标签标题",fg="white",bg="blue")
label1.grid( )
label1.pack(anchor=NW,padx=5)
#组件在窗口中位置,锚点为西北NW，组件外部预留空白宽为5
label2 = Label(win)
label2.config(text="标签内容",fg="white",bg="grey") #配置文本属性
label2.pack(expand=YES,fill=BOTH,padx=5)
#组件可拉伸，X和Y方向填充，组件外部预留空白宽为5
btn= Button()
btn['text']="click" #配置文本属性的另一种方法
btn.pack()
win.title("Example11-5")    #title()方法
win.geometry("300x200")    #geometry()方法
win.mainloop()


