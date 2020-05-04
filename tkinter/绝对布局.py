import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

lable1 = tkinter.Label(win, text="good", bg="blue")
lable2 = tkinter.Label(win, text="nice", bg="red")
lable3 = tkinter.Label(win, text="cool", bg="pink")
# 绝对布局，窗口的变化对位置没有影响
lable1.place(x=10, y=10)
lable2.place(x=50, y=50)
lable3.place(x=100, y=100)


win.mainloop()