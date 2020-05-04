from tkinter import *
from sel import Select
from dele import Delete
from add import Add
from mail import Mail
from up import Update
class Sys(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('学生管理系统')
        self.root.geometry("700x400")
        self.root.resizable(width=False, height=False)
        self.label = Label(self.root,width=700, height=1, text='东 方 红 学 生 信 息 管 理 系 统', font=('微软雅黑', 20),fg="gray")
        self.button1 = Button(self.root, text='添加学生信息', command=self.add, width=10)
        self.button2 = Button(self.root, text='删除学生信息', command=self.Del, width=10)
        self.button3 = Button(self.root, text='修改学生信息', width=10, command=self.up)
        self.button4 = Button(self.root, text='查询学生信息', command=self.select, width=10)
        self.button5 = Button(self.root, text='发送邮件', width=10, command=self.Mail)
        self.button6 = Button(self.root, text='退出系统', command=quit, width=10)

    # def gui_arrang(self):
    #     # 绝对布局
        self.label.pack(side=TOP, ipady=25)
        self.button1.place(x=50, y=140)
        self.button2.place(x=50, y=250)
        self.button3.place(x=300, y=140)
        self.button4.place(x=300, y=250)
        self.button5.place(x=550, y=140)
        self.button6.place(x=550, y=250)
        self.root.mainloop()

    def add(self):
        add = Add()


    def select(self):
        sel = Select()


    def Del(self):
        delete = Delete()

    def Mail(self):
        M = Mail()
    def up(self):
        U = Update()
def main():
    sys = Sys()
    # sys.gui_arrang()

if __name__ == '__main__':
    main()