import random
from tkinter import *
number = random.randint(0, 10)
running = True
num = 0     # 猜的次数
nmax = 10
nminn = 0
def eBtnClose(event):
    root.destroy()

def eBtnGuess(event):
    global nmax
    global nminn
    global num
    global running
    if running:
        val_a = int(entry_a.get())
        if val_a == number:
            labelqval("恭喜答对了！")
            num += 1
            running = False
            numGuess()
        elif val_a < number:
            if val_a > nminn:
                nminn = val_a
                num += 1
                labelqval("小了哦，请输入" + str(nminn)+"到" + str(nmax) + "之间的整数：")
        else:
            if val_a < nmax:
                nmax = val_a    # 如果接收的值大于了number也小于number最大值，就将接收的值赋值给nmax
                num += 1
                labelqval("大了哦，请输入" + str(nminn)+"到" + str(nmax) + "之间的整数：")
    else:
        labelqval("你已经答对啦...")

# 显示猜的次数
def numGuess():
    if num == 1:
        labelqval("一次答对！")
    elif num < 10:
        labelqval("==十次以内答对了牛。。。猜数次数：" + str(num))
    else:
        labelqval("好吧，您都试了超过10次了。。。尝试次数：" + str(num))
def labelqval(vText):
    label_val_q.config(label_val_q, text=vText)
root = Tk(className="猜数字游戏")
root.geometry("400x90+200+200")
root.resizable(width=FALSE, height=FALSE)
label_val_q = Label(root, width=80)
label_val_q.pack(side="top")
entry_a = Entry(root, width=40)
btnGuess = Button(root, text="猜")
entry_a.pack(side="left")
entry_a.bind('<Return>', eBtnGuess)
btnGuess.bind('<Button-1>', eBtnGuess)
btnGuess.pack(side="left")
btnClose = Button(root, text="关闭")
btnClose.pack(side="left")
btnClose.bind('<Button-1>', eBtnClose)
labelqval("请输入0到10之间任意整数：")
entry_a.focus_set()
print(number)
root.mainloop()


