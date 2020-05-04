import tkinter
def func():
	print("sunck is a good man!")
# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")
button1 = tkinter.Button(win, text='按钮1', command=func,
	).pack()


# lambda匿名函数
button2 = tkinter.Button(win, text='按钮2', command=lambda:print("sunck is a nice man"),
	).pack()

button1 = tkinter.Button(win, text='取消', command=quit,
	).pack()
win.mainloop()