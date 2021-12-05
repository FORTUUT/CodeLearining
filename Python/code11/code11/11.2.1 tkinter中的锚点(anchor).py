import tkinter as tk

root= tk.Tk()
root.title('锚点问题')
root.geometry('800x600')    # 设置窗口为500x500

canvas = tk.Canvas(root, width=800, height=600, bg='yellow')   # 创建800x800，背景为黄色的画布
image_file = tk.PhotoImage(file='pic1.png')  # 创建图片对象
image = canvas.create_image(200, 200,  anchor='w', image=image_file)     # 将图片放置在画布上
canvas.pack()         # 放置画布

root.mainloop()