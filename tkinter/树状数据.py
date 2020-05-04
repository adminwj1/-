import tkinter
from tkinter import ttk
# 创建主窗口
win = tkinter.Tk()		# T是大写k是小写
win.title("窗口标题")

win.geometry("400x200")
# 创建树
tree = ttk.Treeview(win)
tree.pack()

# 添加一级树枝
treeF1 = tree.insert("", 0, '中国', text='中国China', values=('F1'))    # treeF1：表示一级树枝的第一个
treeF2 = tree.insert("", 1, '美国', text='美国', values=('F2'))
treeF3 = tree.insert("", 2, '英国', text='英国', values=('F3'))

# 添加二级树枝
treeF1_1 = tree.insert(treeF1, 0, "黑龙江", text="中国黑龙江")  # treeF1_1：表示F1的第一个二级数枝
treeF1_2 = tree.insert(treeF1, 1, "吉林", text="中国吉林")  # treeF1_1：表示F1的第二个二级数枝
treeF1_3 = tree.insert(treeF1, 2, "辽宁", text="中国辽宁")  # treeF1_1：表示F1的第三个二级数枝


# 添加三级数枝
treeF1_1_1 = tree.insert(treeF1_1, 0, "哈尔滨", text="中国哈尔滨")  # treeF1_1_1：表示二级数枝的第一级
treeF1_1_2 = tree.insert(treeF1_1, 1, "五常", text="中国五常")  # treeF1_1_1：表示二级数枝的第一级


win.mainloop()