import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton,
                             QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 设置一个用于显示工具提示的字体
        QToolTip.setFont(QFont('SansSerif', 10))

        # 创建一个提示，称之为settooltip()方法
        self.setToolTip('This is a <b>QWidget</b> widget')  # 主窗口也显示提示
        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QWidget</b> widget')
        # btn,sizeHint() 显示按钮为默认尺寸
        btn.resize(btn.sizeHint())
        btn.move(50, 50)    # x和y轴的位置
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.setWindowIcon(QIcon('logo.ico'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())