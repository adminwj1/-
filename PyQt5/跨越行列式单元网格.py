import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.initUI()

    def initUI(self):
        name = QLabel('昵称')
        hobby = QLabel('兴趣爱好')
        signature = QLabel('个性标签名')

        nameEdit = QLineEdit()  # 单行文本框
        hobbyEdit = QLineEdit()
        signatureEdit = QTextEdit()     # 多行文本框
        grid = QGridLayout()    # 网格布局
        grid.setSpacing(10)     # 控件与控件之间的间距
        grid.addWidget(name, 1, 0)
        grid.addWidget(nameEdit, 1, 1)
        grid.addWidget(hobby, 2, 0)
        grid.addWidget(hobbyEdit, 2, 1)
        grid.addWidget(signature, 3, 0)
        grid.addWidget(signatureEdit, 3, 1, 5, 1)
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())