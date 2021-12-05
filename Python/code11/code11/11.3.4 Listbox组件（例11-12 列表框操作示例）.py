#11.3.4 Listbox组件（例11-12 列表框操作示例）.py
from tkinter import *
win=Tk()
listbox=Listbox(win)   #创建列表框
#初始化列表框
items=["HTML5","CSS3","JavaScript","Jquery"]
for item in items:
    listbox.insert(END,item)  #将列表中数据项尾部插入到列表框
listbox.pack(side=LEFT,expand=1,fill=Y)   #打包列表框
def additem():						     #在列表框中填加选项
    str=entry1.get()  #获得输入框字符串
    if not str=='':   #字符串非空
        index=listbox.curselection()  #获得当前选中项的索引index元组
        if len(index)>0:
            listbox.insert(index[0],str)		#有选中项时，在选中项前面添加一项
        else:
            listbox.insert(END,str)			#无选中项时，添加到最后
def removeitem():					           #在列表框中删除选项
    index=listbox.curselection()      #获得当前选中项的索引元组
    if len(index)>0:                  #有选中项时，
        if len(index)>1:              #选中多项时，
            listbox.delete(index[0],index[-1])	#删除选中的多项
        else:                
            listbox.delete(index[0])			#删除选中的一项
entry1=Entry(width=20)   #创建输入框
entry1.pack(anchor=NW)   #打包输入框
bt1=Button(text='添加',command=additem)  #创建按钮1
bt1.pack(anchor=NW)      #打包按钮1
bt2=Button(text='删除',command=removeitem)  #创建按钮2
bt2.pack(anchor=NW)      #打包按钮2
mainloop()
