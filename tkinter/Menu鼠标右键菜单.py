import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")
# 菜单条
menubar = tkinter.Menu(win)

# 菜单
menu = tkinter.Menu(menubar, tearoff=False)
for item in ['Python', 'C', 'C++', 'shell', 'C#', 'PHP', 'Java', 'Swift']:
	menu.add_command(label=item)

menubar.add_cascade(label='语言', menu=menu)

'''
post：显示鼠标右键后的菜单
x,y：鼠标右键的位置
<Button-3>：鼠标右键
<Button-1>：鼠标左键
<Button-1>：鼠标滚轮键
'''

def showMenu(event):
    menubar.post(event.x_root, event.y_root)
win.bind("<Button-3>", showMenu)
win.mainloop()