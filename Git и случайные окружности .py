import sys
from random import randint
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor
import numpy as np


class MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.pshb = QtWidgets.QPushButton(Form)
        self.pshb.setGeometry(QtCore.QRect(370, 280, 93, 28))
        self.pshb.setObjectName("MainWindow")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pshb.setText(_translate("Form", "Окружность"))


class MyWidget(QtWidgets.QWidget, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.drawF = False
        self.pshb.clicked.connect(self.run)

    def run(self):
        self.drawF = True
        self.update()

    def paintEvent(self, event):
        if self.drawF:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(*np.random.choice(range(255), size=3)))
            r = randint(20, 100)
            qp.drawEllipse(randint(100, 700), randint(100, 500), r, r)
            qp.end()


app = QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
