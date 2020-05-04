import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x400")

lable1 = tkinter.Label(win, text="good", bg="blue")
lable2 = tkinter.Label(win, text="nice", bg="red")
lable3 = tkinter.Label(win, text="cool", bg="pink")

# 相对布局，窗体改变对控件有影响
# tkinter.BOTH
lable1.pack(fill=tkinter.Y, side=tkinter.LEFT)
lable2.pack(fill=tkinter.X, side=tkinter.TOP)
lable3.pack(fill=tkinter.X, side=tkinter.BOTTOM)





win.mainloop()