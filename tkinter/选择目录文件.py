import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

'''
    tkinter.filedialog.asksaveasfilename():选择以什么文件名保存，返回文件名
    tkinter.filedialog.asksaveasfile():选择以什么文件保存，创建文件并返回文件流对象
    tkinter.filedialog.askopenfilename():选择打开什么文件，返回文件名
    tkinter.filedialog.askopenfile():选择打开什么文件，返回IO流对象
    tkinter.filedialog.askdirectory():选择目录，返回目录名
    tkinter.filedialog.askopenfilenames():选择打开多个文件，以元组形式返回多个文件名
    tkinter.filedialog.askopenfiles():选择打开多个文件，以列表形式返回多个IO流对象'''

file_path = filedialog.asksaveasfilename(filetypes=[("PNG",".png"),("GPF",".gpf"),("JPG",".jpg"),("python",".py")])


mainloop()
print(file_path) # 打印文件的路径



# root=Tk()

# def callback():
#     fileName =filedialog.askopenfilename(filetypes=[("PNG",".png"),("GPF",".gpf"),("JPG",".jpg"),("python",".py")])
#     print(fileName)
# #打开文件askopenfilename
# #defaultextension自动添加后缀
# Button(root, text="Openfile",command =callback).pack()    



# mainloop()

