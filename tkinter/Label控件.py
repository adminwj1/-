import tkinter

# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")
win.geometry("400x200")
'''
Label：标签空间
可以显示文本
参数：
win：父窗体
test：显示的文本内容
bg：背景色
fg：字体颜色
font：字体样式和字体大小
width：宽度
height：高度
wraplength：指定text文本中多宽进行换行
justify：设置换行后的对齐方式
anchor：位置
参数：
东西南方
n、s、e、w、nw、sw、se、ne、center（默认值）
'''
Label = tkinter.Label(win, text='sunck',
	bg='pink',fg='red',font=('微软雅黑,20'),
	width=10, height=3, wraplength=100,
	justify="left",anchor="n").pack()





win.mainloop()