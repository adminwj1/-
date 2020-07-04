import sys
from PyQt5.QtWidgets import QWidget, QGridLayout,QPushButton, QApplication

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        positions = [(i,j) for i in range(5) for j in range(4)]

        for positions, names in zip(positions, names):
            if names == '':
                continue
            button = QPushButton(names)
            grid.addWidget(button, *positions)  # addWidget()方法把按钮放到布局里面

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())