import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")

# <Button-1>鼠标左键，bind绑定事件
def func(event):
    print(event.x, event.y)

# button1 = tkinter.Button(win, text="leftmouse button")
button1 = tkinter.Label(win, text="leftmouse button")
button1.bind("<Button-1>", func)
button1.pack()




# <Button-3>鼠标右键
# <Button-2>鼠标滑轮
def func(event):
    print(event.x, event.y)

button2 = tkinter.Button(win, text="rightmouse button")
# button1 = tkinter.Label(win, text="leftmouse button")
button2.bind("<Button-3>", func)
button2.pack()



# 左键双击事件
'''
<Double-Button-1>	鼠标左键双击
<Double-Button-3>	鼠标中键双击
<Double-Button-2>	鼠标右键双击
<Triple-Button-1>	鼠标左键三双击
<Triple-Button-3>	鼠标中键三双击
<Triple-Button-2>	鼠标右键三双击
'''
button3 = tkinter.Button(win, text="leftmouse button")
# button1 = tkinter.Label(win, text="leftmouse button")
button3.bind("<Double-Button-1>", func)
button3.pack()


# 鼠标三击事件
button4 = tkinter.Button(win, text="leftmouse button")
# button1 = tkinter.Label(win, text="leftmouse button")
button4.bind("<Triple-Button-1>", func)
button4.pack()
win.mainloop()