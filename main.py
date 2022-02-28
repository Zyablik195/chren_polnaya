from PyQt5 import uic, QtCore, QtMultimedia
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from random import randint

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle('Рисование')

        self.pushButton = QPushButton('нарисовать', self)
        self.pushButton.move(20, 10)
        self.pushButton.resize(160, 20)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        for i in range(6):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            r = randint(30, 80)
            qp.drawEllipse(QPoint(randint(0, 700 - r), randint(0, 500 - r)), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyWidget()
    main_window.show()
    sys.exit(app.exec_())
