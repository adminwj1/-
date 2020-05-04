import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")
def showInfo():
	print(entry.get())
entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win,text="按钮", command=showInfo).pack()

win.mainloop()