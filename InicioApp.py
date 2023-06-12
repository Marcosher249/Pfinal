import os
import sys

from ui_bottrade import *
from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts

from functools import partial

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = LoginRegisterWindow()
#     window.show()
#     sys.exit(app.exec_())
elementos_ocultos = {
    "menu",
    "frame_3",
    "frame_4",
    "frame_6"
}

class MainWindow(QMainWindow()):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

