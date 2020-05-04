import tkinter
from tkinter import ttk
# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("600x200")

# 创建表格数据
tree = ttk.Treeview(win)
tree.pack()
# 创建列
tree['columns'] = ("姓名", "年龄", "身高", "体重")
# 设置每一个列，要和列中的内容一样
tree.column("姓名", width=100)
tree.column("年龄", width=100)
tree.column("身高", width=100)
tree.column("体重", width=100)

# 设置标头（显示列），真正显示的是：text='name'
tree.heading("姓名", text='name')
tree.heading("年龄", text='age')
tree.heading("身高", text='height')
tree.heading("体重", text='weight')


# 添加数据，参数1为空，参数2为索引值，参数三为列名，参数四为数据内容（类型为元组）
tree.insert("", 0, text='line1', values=("陆彦旭", "28", "165", "80"))
tree.insert("", 1, text='line2', values=("范育宾", "29", "167", "70"))

win.mainloop()