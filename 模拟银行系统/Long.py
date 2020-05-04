from tkinter import *
root =Tk()
Label(root, text='账号：').grid(row=0, sticky=W)
Entry(root).grid(row=0, column=1)
Label(root, text='密码：').grid(row=1, sticky=W)
Entry(root).grid(row=1, column=1)
Button(root, text='确定').grid(row=2, column=1, sticky=E)
root.mainloop()