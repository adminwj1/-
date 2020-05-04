from tkinter import *
import smtplib
# email用于构建邮件内容
from email.mime.text import  MIMEText
# 用于构建邮件头
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from tkinter import filedialog


class Mail(object):
    """编写邮件发送功能，占时只写单发，纯文本格式的邮件"""

    def __init__(self):
        self.root = Tk()
        self.root.title('学生信息系统-邮件发送模块')
        self.root.geometry("800x660")
        self.root.resizable(width=FALSE, height=FALSE)
        self.label = Label(self.root, text='收件人：', font=('微软雅黑', 13))
        self.entry = Entry(self.root, width=25)     # 收件人输入框
        self.head = Label(self.root, text='标题：', font=('微软雅黑', 13))
        self.head_a = Entry(self.root, width=25, font=('微软雅黑', 10))

        # 创建滚动条
        self.scroll = Scrollbar()
        self.text = Text(self.root, font=('微软雅黑', '12'), width=83)
        self.button1 = Button(self.root, text='发送内容', width=15, font=('微软雅黑', '12'), command=self.mail)
        self.button2 = Button(self.root, text='重置内容', width=15, font=('微软雅黑', '12'), command=self.Empty)
        self.button3 = Button(self.root, text='附件', width=10, font=('微软雅黑', '12'), command=self.Accessory)
        # 布局
        self.label.place(x=15, y=15)
        self.entry.place(x=80, y=15, height=30)
        self.head.place(x=510, y=15)
        self.head_a.place(x=560, y=15, height=30)
        self.text.place(x=15, y=80)
        self.button1.place(x=15, y=600, height=46)
        self.button2.place(x=580, y=600, height=46)
        self.scroll.pack(side=RIGHT, fill=Y)
        # 配置滚动条和text多行文本的关联
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)
        self.button3.place(x=330, y=15,height=30)
        self.root.mainloop()

    def Accessory(self):
        self.file_path = filedialog.askopenfilename()
        print(type(self.file_path))
        print(self.file_path)


    def mail(self):
        '''
        1、先获取控件中的内容
        2、编写邮件格式
        '''

        # 收件人邮箱信息
        # 循环去掉最后一个元素中的\n
        to_addr = list(self.entry.get().split(','))
        '''调试代码'''
        # print(type(to_addr))
        # print(to_addr)
        # 标题
        head = self.head_a.get()
        # 邮件内容
        text = self.text.get('0.0', 'end')


        # 发送服务器
        message = MIMEMultipart()
        smtp_server = 'smtp.qq.com'
        # 邮箱功能设置
        from_addr = '654109102@qq.com'
        password = 'wnauzgsceppkbfdh'
        # 邮件正文内容
        # msg = MIMEText(text, 'plain', 'utf-8')

        # 邮件头信息
        message['From'] = Header(from_addr, 'utf-8')
        # msg['To'] = Header('管理员')
        message['Subject'] = Header(head,'utf-8')
        # 邮件正文内容
        message.attach(MIMEText(text,'piain', 'utf-8'))
        # 构造附件1，发送图片
        att1 = MIMEText(open(self.file_path,'rb').read(),'base64','utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以随意写，些什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="02.jpg"'
        message.attach(att1)
        # 发送邮件
        try:
            # 配置服务器
            server = smtplib.SMTP()
            server.connect(smtp_server, 25)
            # 登录邮箱
            server.login(from_addr, password)
            # 发送功能
            server.sendmail(from_addr, to_addr, message.as_string())
            messagebox.showinfo(title='邮件', message='发送成功！')
        except smtplib.SMTPException:
            messagebox.showinfo(title='邮件', message='发送失败！')
        finally:
            # 关闭是服务器
            server.quit()





    def Empty(self):
        self.text.delete('0.0', 'end')
        self.entry.delete(0, END)
        self.head_a.delete(0, END)
def main():
    M = Mail()




if __name__ == '__main__':
    main()










