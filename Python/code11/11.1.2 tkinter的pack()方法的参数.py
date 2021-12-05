import tkinter
from tkinter import *

if __name__ == '__main__':
    w = tkinter.Tk()
    w.geometry('{}x{}+{}+{}'.format(200, 200, 100, 100))
    f = Frame()
    f.pack()
    tkinter.Button(f, text='按钮1').pack(side=LEFT, padx=10)
    tkinter.Button(f, text='按钮2').pack(side=LEFT, padx=10)
    tkinter.Button(f, text='按钮3').pack(side=LEFT, padx=10)
    f1 = Frame()
    f1.pack()
    tkinter.Button(f1, text='按钮4').pack(side=LEFT, padx=10)
    tkinter.Button(f1, text='按钮5').pack(side=LEFT, padx=(20, 10))
    tkinter.Button(f1, text='按钮6').pack(side=LEFT, padx=(0, 10))
    w.mainloop()
