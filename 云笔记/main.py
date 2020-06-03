from tkinter import *
import os
import sys
import threading

class TK(object):
    def __init__(self):
        self.root = Tk()

        # 创建菜单条
        menubar = Menu(self.root)
        # 创建绑定变量
        self.menu = StringVar()
        filemenu = Menu(menubar, tearoff=0)
        for item in ['文件', '打开1', '打开2']:
            filemenu.add_radiobutton(label=item, variable=self.menu, command=self.OpenFile)
        menubar.add_cascade(label='File', menu=filemenu)


        func = Menu(menubar, tearoff=0)
        for item01 in ['同步', '导出', '导入']:
            func.add_radiobutton(label=item01, variable=self.menu, command=self.OpenFile)
        menubar.add_cascade(label='Func', menu=func)
        self.root['menu'] = menubar





        self.root.mainloop()
    def OpenFile(self):
        print(self.menu.get())



def main():

    tk = TK()
    # t = threading.Thread(target=tk.OpenFile)
    # t.start()
    # t.join()

if __name__ == '__main__':
    main()