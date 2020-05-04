from email import encoders
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
#  第三方SMTP
mail_host ="smtp.qq.com"
mail_user = '654109102@qq.com'   # 用户
mail_pass = 'wnauzgsceppkbfdh'
sender = '654109102@qq.com'  #  发送者邮箱
receivers = ['17608391679@163.com', 'admiwj@outlook.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 创建一个带有附件的实例，有几个附件就创建几个附件的实例
message = MIMEMultipart()
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
#message = MIMEText('每天开心', 'plain', 'utf-8')
message['from'] = Header("新年祝福", 'utf-8')#  主题
message['to'] =  Header("tom", 'utf-8') #收件人的名称
subject = 'Python SMTP 邮件'  #  标题
message['Subject'] = Header(subject, 'utf-8')
# 邮件正文内容
message.attach(MIMEText('这个文件很重要请及时查收，并第一时间回复！！！', 'plain', 'utf-8'))
# 构造附件1，传送.txt文件
att1 = MIMEText(open('D:/1.jpg','rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以随意写，些什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="02.jpg"'
message.attach(att1)
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  #  25为SMTP端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
finally:
    smtpObj.quit()