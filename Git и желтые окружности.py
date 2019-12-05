import sys
from random import randint
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtGui import QPainter, QColor
import numpy as np


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.drawF = False
        self.pshb.clicked.connect(self.run)

    def run(self):
        self.drawF = True
        self.update()

    def paintEvent(self, event):
        if self.drawF:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('yellow'))
            r = randint(20, 100)
            qp.drawEllipse(randint(100, 700), randint(100, 500), r, r)
            qp.end()


app = QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
