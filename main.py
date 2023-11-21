import sys
import io

from random import randrange

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.Qt import QPointF

desing = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>471</width>
    <height>546</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>140</x>
     <y>440</y>
     <width>171</width>
     <height>61</height>
    </rect>
   </property>
   <property name="text">
    <string>СГЕНЕРИРОВАТЬ</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(desing)
        uic.loadUi(f, self)
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
            qp.setBrush(QColor(255, 255, 0))
            size = randrange(30, 200)
            qp.drawEllipse(QPointF(215, 200), size, size)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec_())
