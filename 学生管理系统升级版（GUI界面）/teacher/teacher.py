from tkinter import*
import pymysql
from tkinter import ttk
from tkinter import messagebox
import os
class Teacher(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('学生信息系统-登录模块')
        self.root['width'] = 500
        self.root['height'] = 200
        self.root.resizable(width=False, height=False)
        


def main():
    # 初始化对象
    T = Teacher()
    # 进行布局
    T.gui_arrang()
    # 主程序执行
    mainloop()
if __name__ == '__main__':
    main()