# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_de_dialogoCXxvaZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(406, 288)
        Dialog.setStyleSheet(u"#frame {background-color: rgba(61, 80, 95, 100)}")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(28, 57, 94, 175);\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255); \n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u00bfEst\u00e1 seguro de que quiere cerrar sesi\u00f3n?", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"si", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"no", None))
    # retranslateUi

