import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

lable = tkinter.Label(win, text="sunck is a good man")
lable.pack()
'''
移动事件：当鼠标左键被按住在小构件且移动鼠标事件发生
B1-Motion：B是固定，1表示鼠标左键移动
B2-Motion：B是固定，2表示鼠标右键移动
B3-Motion：B是固定，3表示鼠标中键移动
'''
def func(event):
    print(event.x, event.y)
lable.bind("<B1-Motion>", func)


win.mainloop()