"""
QHBoxLayout，水平布局，顾名思义，是一种水平方向上从左向右的顺序添加控件的布局方式。
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class WinForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("水平布局示例")
        self.resize(550, 400)
        # 对齐方式主要通过对齐方式参数 Qt.Alignment 来设置
        hLayout = QHBoxLayout()
        hLayout.addWidget(QPushButton(str(1)), 0, Qt.AlignTop)  # 靠顶部
        hLayout.addWidget(QPushButton(str(2)), 0, Qt.AlignLeft | Qt.AlignTop)   # 顶部靠右布局
        hLayout.addWidget(QPushButton(str(3)))
        hLayout.addWidget(QPushButton(str(4)), 0, Qt.AlignLeft | Qt.AlignBottom)    # 底部靠右布局
        hLayout.addWidget(QPushButton(str(5)), 0, Qt.AlignLeft | Qt.AlignBottom)
        hLayout.setSpacing(50)  # 控件与控件之间的间距
        self.setLayout(hLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())