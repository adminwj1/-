from tkinter import *
from tkinter import messagebox
import pymysql
class Delete(object):
    def __init__(self):
        self.root =Tk()
        self.root.title('学生信息系统-删除模块')
        self.root.geometry("380x200")
        self.root.resizable(width=False, height=False)
        self.lable = Label(self.root, text='学号：', font=('微软雅黑,'))
        self.entry = Entry(self.root)
        self.button = Button(self.root, text='删除', width=10, command=self.delete)

        self.lable.place(x=50, y=70)
        self.entry.place(x=120, y=70, height=30)
        self.button.place(x=280, y=70)
        self.root.mainloop()

    def delete(self):
        delchoice = self.entry.get()
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'studentsystem')
        cursor = db.cursor()
        try:
            sql1 = "select * from info where id = " + delchoice  # 对输入的学号进行判断，是否存在该学号
            cursor.execute(sql1)
            reslist = cursor.fetchall()
            if reslist:
                sql = "delete from info where id = " + delchoice
                cursor.execute(sql)
                db.commit()
                messagebox.showinfo(title='删除', message='删除成功！')
                self.entry.delete(0, END)
            else:
                messagebox.showinfo(title='删除', message='未查到数据，删除失败！')
                self.entry.delete(0, END)

        except:
            db.rollback()
            cursor.close()
            db.close()


if __name__ == '__main__':
    d = Delete()