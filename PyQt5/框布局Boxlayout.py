from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout,QVBoxLayout,QApplication
import sys
"""
QBoxLayout 类支持在水平和垂直方向上排列控件，其子类有 QHBoxLayout（水平布局） 和 QVBoxLayout（垂直布局）。
"""
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")


        hbox = QHBoxLayout()    # 创建水平布局
        hbox.addStretch(1)      # 增加一些弹性空间
        hbox.addWidget(okButton)    # 布局中添加控件，伸缩量只适用于 QBoxLayout，控件和窗口会随着伸缩量的变大而变大
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()    # 创建垂直布局
        vbox.addStretch(1)
        vbox.addLayout(hbox)    # 将水平布局放置垂直布局中


        self.setLayout(vbox)    # 将元素放置在右下角
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())