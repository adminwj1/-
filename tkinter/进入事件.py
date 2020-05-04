import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

'''
<Enter>     进入事件，只有当鼠标移动至空间内才会触发事件
'''
label = tkinter.Label(win, text='sunck is a good man', bg='red')
label.pack()
def fun(event):
    print(event.x, event.y)
label.bind("<Enter>",fun)

win.mainloop()