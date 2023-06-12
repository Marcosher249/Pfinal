import os
import sys

from ui_bottrade import *
from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts

from Custom_Widgets.Widgets import *

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
    "frame_6",
    "frame_7"
}

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(850, 600)
        self.show()
        for x in elementos_ocultos:
            effect = QtWidgets.QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0,0,0,255))
            getattr(self.ui, x).setGraphicsEffect(effect)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()  # Utiliza la instancia de MainWindow existente
    window.show()
    sys.exit(app.exec_())

