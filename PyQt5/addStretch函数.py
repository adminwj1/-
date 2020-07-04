"""
addStretch(int stretch=0) 函数用于在布局管理器中增加一个可伸缩的控件(QSpaceItem)，0 为最小值，并且将 stretch 作为伸缩量添加到布局末尾。
如果在第一个控件之前添加伸缩控件，那么所有的控件都会居右显示；反之，如果在最后一个控件之后添加伸缩控件，呢么所有的孔家都会居左显示。
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        hBox = QHBoxLayout()  # 水平布局
        self.setLayout(hBox)
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn1.setText('button 1')
        btn2.setText('button 2')
        btn3.setText('button 3')

        hBox.addStrut(5)
        hBox.addWidget(btn1)
        hBox.addStrut(5)
        hBox.addWidget(btn2)
        hBox.addStrut(5)
        hBox.addWidget(btn3)
        hBox.addStrut(5)

        self.setWindowTitle("addStretch Demo")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())

