import sys
import io

from random import randrange

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.Qt import QPointF

from UI import Ui_Form


class Circle(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw)
        self.flag = False

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        if self.flag:
            qp.setBrush(QColor(randrange(0, 256), randrange(0, 256),
                               randrange(0, 256)))
            size = randrange(30, 200)
            qp.drawEllipse(QPointF(215, 200), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec_())
