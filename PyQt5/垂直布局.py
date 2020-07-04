"""
QVBoxLayout 类，支持从上到下的顺序添加控件
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.setWindowTitle("垂直布局示例")
        vLayout = QVBoxLayout()
        self.resize(200, 300)
        vLayout.addWidget(QPushButton(str(1)), 0, Qt.AlignTop)
        vLayout.addWidget(QPushButton(str(2)), 0, Qt.AlignLeft | Qt.AlignTop)
        vLayout.addWidget(QPushButton(str(3)))
        vLayout.addWidget(QPushButton(str(4)))
        vLayout.addWidget(QPushButton(str(5)))
        self.setLayout(vLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    sys.exit(app.exec_())
