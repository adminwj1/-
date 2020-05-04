from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from  PIL import  ImageTk, Image
import os
import pymysql

class Login(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry('700x500')
        self.root.resizable(width=FALSE,height=FALSE)
        # 背景图片设置
        self.image = Image.open(r'D:\教务系统\img\timg.png')
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background_label = Label(self.root, image=self.background_image)
        # relheight 指定组件相对于父组件的高度， relwidth 指定该组件相对于父组件的宽度取值范围都是0.0~1.0
        # self.background_label.place(x=0, y=0,relwidth=1,relheight=1)

        self.root.mainloop()





if __name__ == '__main__':
    L = Login()