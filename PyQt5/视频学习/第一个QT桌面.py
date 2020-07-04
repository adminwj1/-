import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建一个QQpplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(300, 150)
    # 窗口显示在屏幕的位置
    w.move(300, 300)
    # 窗口标题
    w.setWindowTitle('第一个基于PyQt5de桌面应用')
    w.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())

