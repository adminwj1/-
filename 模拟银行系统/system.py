import tkinter as tk
class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=10, pady=10)  # padx，x轴的内边距  pady，y轴的内边距
        self.hi_there = tk.Button(frame, text="打招呼", bg="black", fg="white", command=self.say_hi)   # bg和fg分别表示背景色和前景色
        self.hi_there.pack()

    def say_hi(self):
        print("打招呼")


root = tk.Tk()
app = APP(root)
root.mainloop()
