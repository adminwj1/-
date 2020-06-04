import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon  # 添加应用程序的图标时倒入

app = QApplication(sys.argv)
w = QWidget()
w.resize(400, 350)
w.move(300, 300)
w.setWindowTitle('钉钉')
# 设置窗体的图标
w.setWindowIcon(QIcon('logo.ico'))
w.show()

sys.exit(app.exec_())