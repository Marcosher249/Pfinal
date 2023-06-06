from login import LoginRegisterWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import firebase_admin
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginRegisterWindow()
    window.show()
    sys.exit(app.exec_())