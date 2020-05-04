from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk
class Add(object):
    def __init__(self):
        # 模块去区
        self.root = Tk()
        self.root.title('学生管理系统')
        self.root.geometry("800x500")
        self.root.resizable(width=False, height=False)
        # 第一行数据
        self.id = Label(self.root, text='学号：')
        self.input_id = Entry(self.root, width=12)
        self.name = Label(self.root, text='姓名：')
        self.input_name = Entry(self.root, width=12)
        self.gender = Label(self.root, text='性别：')
        self.gender_a = ttk.Combobox(self.root, width=5)
        self.gender_a['value'] = ('男', '女')
        self.gender_a.current('0')
        self.age = Label(self.root, text='年龄：')
        self.input_age = Entry(self.root, width=12)
        # 第二行数据
        self.cardid = Label(self.root, text='身份证：')
        self.input_cardid = Entry(self.root, width=12)
        self.date = Label(self.root, text='出生日期：')
        self.input_date = Entry(self.root, width=12)
        self.address = Label(self.root, text='地址：')
        self.input_address = Entry(self.root,width=12)
        self.department = Label(self.root, text='系部：')
        self.input_department = Entry(self.root, width=12)
        # 第三行数据
        self.major = Label(self.root, text='专业：')
        self.input_major = Entry(self.root, width=12)
        self.Class = Label(self.root, text='班级：')
        self.input_Class = Entry(self.root, width=12)
        self.phone = Label(self.root, text='手机号：')
        self.input_phone = Entry(self.root, width=12)
        self.mail = Label(self.root, text='邮箱：')
        self.input_mail = Entry(self.root, width=12)
        self.QQ = Label(self.root, text='QQ号：')
        self.input_QQ = Entry(self.root, width=12)
        self.add = Button(self.root, text='添加', width=20, command=self.SQL)
        # 布局区
        # 第一行布局
        self.id.place(x=10, y=14)
        self.input_id.place(x=50, y=14)
        self.name.place(x=200, y=14)
        self.input_name.place(x=250, y=14)
        self.gender.place(x=400, y=14)
        self.gender_a.place(x=448, y=14)
        self.age.place(x=580, y=14)
        self.input_age.place(x=630, y=14)
        # 第二行布局
        self.cardid.place(x=10, y=100)
        self.input_cardid.place(x=60, y=100)
        self.date.place(x=200, y=100)
        self.input_date.place(x=270, y=100)
        self.address.place(x=400, y=100)
        self.input_address.place(x=450, y=100)
        self.department.place(x=580, y=100)
        self.input_department.place(x=630, y=100)
        # 第三行布局
        self.major.place(x=10, y=200)
        self.input_major.place(x=50, y=200)
        self.Class.place(x=200, y=200)
        self.input_Class.place(x=270, y=200)
        self.phone.place(x=400, y=200)
        self.input_phone.place(x=450, y=200)
        self.mail.place(x=580, y=200)
        self.input_mail.place(x=630, y=200)
        self.QQ.place(x=10, y=300)
        self.input_QQ.place(x=60, y=300)
        self.add.place(x=580, y=300, height=50)
        self.root.mainloop()
        # 连接数据库
    def SQL(self):
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'studentsystem')
        cursor = db.cursor()
        if not self.Verifi():
            messagebox.showinfo(title='增加', message='省份证输入有误！')
            return -1
        try:
            sql = 'insert into info values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",{},"{}","{}")'. \
                    format(self.input_id.get(), self.input_name.get(), self.gender_a.get(), self.input_age.get(),
                           self.input_cardid.get(), self.input_date.get(), self.input_address.get(),
                           self.input_department.get(), self.input_major.get(), self.input_Class.get(),
                           self.input_phone.get(), self.input_mail.get(), self.input_QQ.get())
            cursor.execute(sql)
            db.commit()
            messagebox.showinfo(title='增加', message='增加成功！')
        except:
            db.rollback()
            cursor.close()
            messagebox.showinfo(title='增加', message='增加失败！')
        finally:
            db.close()

    def Verifi(self):
        cardId = self.input_cardid.get()
        if len(cardId) == 18 and cardId.isdigit():
            return True
        return False
if __name__ == '__main__':
    add = Add()
    add.SQL()