from PyQt5 import uic, QtCore, QtMultimedia
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from random import randint

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
            qp.setBrush(QColor(255, 255, 0))
            r = randint(40, 100)
            qp.drawEllipse(QPoint(randint(0, 700 - r), randint(0, 500 - r)), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyWidget()
    main_window.show()
    sys.exit(app.exec_())
