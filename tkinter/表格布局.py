import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

lable1 = tkinter.Label(win, text="good", bg="blue")
lable2 = tkinter.Label(win, text="nice", bg="red")
lable3 = tkinter.Label(win, text="cool", bg="pink")
lable4 = tkinter.Label(win, text="handsome", bg="yellow")

# 表格布局
lable1.grid(row=0, column=0)
lable2.grid(row=0, column=1)
lable3.grid(row=1, column=0)
lable4.grid(row=1, column=1)



win.mainloop()