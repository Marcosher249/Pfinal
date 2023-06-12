# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dise�o_graficasNpXECY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(675, 556)
        MainWindow.setStyleSheet(u"#menu,#frame_2{\n"
"	background-color: rgb(33, 43, 51);\n"
"}\n"
"#frame_4,#frame_6{\n"
"	background-color: rgba(61, 80, 95, 100);\n"
"}\n"
"\n"
"#stackedWidget{\n"
"	background-color: rgba(61, 80, 95, 100)\n"
"}\n"
"#frame_2 QLabel,#frame QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#frame_3,#frame_5{\n"
"	background-color: rgb(61, 80, 95)\n"
"}\n"
"\n"
"#frame_4 QPushButton{\n"
"	background-color: rgba(28, 57, 94, 175);\n"
"	font-size: 15px;\n"
"	border: rgba(69, 72, 80,175);\n"
"	color: rgb(255, 255, 255);\n"
"	text-align: left;\n"
"	padding-left: 5px; \n"
"}\n"
"#page QPushButton,#page_1 QPushButton,#page_2 QPushButton,#page_3 QPushButton,#page_4 QPushButton,#page_5 QPushButton{\n"
"	background-color: rgba(61, 80, 95, 100);\n"
"	font-size: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	text-align: left;\n"
"	border:none;\n"
"    min-height: 30px;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"#frame_4 QPushButton:hover {\n"
"	background-color: rgba(17, 34, 56, 125);\n"
"	border: none;\n"
"}\n"
"\n"
"#scrollA"
                        "reaWidgetContents,#frame_5 QPushButton,#scrollArea{\n"
"	background: transparent;\n"
"	border:transpaernt;\n"
"}\n"
"#scrollArea QScrollBar {\n"
"    background-color: rgba(61, 80, 95, 100);\n"
"}\n"
"#scrollArea QLabel{\n"
"	background-color: rgba(61, 80, 95, 100);\n"
"	font-size: 15px;\n"
"	min-height: 30px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"#pushButton_34{\n"
"	background-color: rgba(0, 170, 0,100);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#pushButton_33{\n"
"	background-color: rgba(255, 0, 0,100);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#label_38{\n"
"	background-color: rgba(255, 0, 0,100);\n"
"}\n"
"#frame_39 QLineEdit{\n"
"	background-color: rgba(61, 60, 95, 100);\n"
"	border: 3px solid rgb(61, 60, 95);\n"
"	color: rgba(255, 255, 255,100);\n"
"}\n"
"#frame_38,#frame_37 {\n"
"background-color: rgba(61, 80, 95, 100);\n"
"}\n"
"#frame_14 QLabel {\n"
"   color: rgb(255, 255, 255);\n"
"	font-size: 15px;\n"
"	\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 8, -1, -1)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 30))
        self.label_3.setMaximumSize(QSize(30, 30))
        self.label_3.setPixmap(QPixmap(u":/navegacion/imagenes_navegacion/trading.svg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.menu)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(0, 3, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/iconos/iconos/bitcoin.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 30))
        icon1 = QIcon()
        icon1.addFile(u":/iconos/iconos/ethereum.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_23 = QPushButton(self.frame_4)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(0, 30))
        icon2 = QIcon()
        icon2.addFile(u":/iconos/iconos/bnb.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_23.setIcon(icon2)

        self.gridLayout.addWidget(self.pushButton_23, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        icon3 = QIcon()
        icon3.addFile(u":/iconos/iconos/usdc.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.pushButton_22 = QPushButton(self.frame_4)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(0, 30))
        icon4 = QIcon()
        icon4.addFile(u":/iconos/iconos/wallet.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_22.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton_22, 4, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.menu)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(3, -1, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 318, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 30))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 0, 0, 0)
        self.label_23 = QLabel(self.frame_14)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(45, 16777215))
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_14)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_3.addWidget(self.label_24)


        self.gridLayout_6.addWidget(self.frame_14, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.menu)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 0, 3, 3)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(500, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 0, 1, 1)
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(30, 30))
        self.pushButton_5.setMaximumSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u":/navegacion/imagenes_navegacion/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.horizontalSpacer = QSpacerItem(384, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(30, 30))
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/navegacion/imagenes_navegacion/person.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_6)

        self.horizontalLayout_4.setStretch(2, 4)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_7)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_2 = QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_35 = QFrame(self.page_3)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_2 = QLabel(self.frame_35)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setToolTipDuration(-2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_2)

        self.label_18 = QLabel(self.frame_35)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.horizontalLayout_29.addWidget(self.label_18)


        self.verticalLayout_2.addWidget(self.frame_35)

        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 125, 510))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(9)
        self.gridLayout_4.setContentsMargins(3, 9, 9, 3)
        self.pushButton_15 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_15.setObjectName(u"pushButton_15")
        icon7 = QIcon()
        icon7.addFile(u":/iconos/iconos/bitcoin (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon7)
        self.pushButton_15.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_15, 3, 0, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_13, 4, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_14, 2, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_6, 2, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)

        self.pushButton_27 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_27.setObjectName(u"pushButton_27")
        icon8 = QIcon()
        icon8.addFile(u":/iconos/iconos/binance_color.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_27.setIcon(icon8)
        self.pushButton_27.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_27, 7, 0, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_21, 11, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setIcon(icon7)
        self.pushButton_13.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_13, 1, 0, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_20, 10, 1, 1, 1)

        self.pushButton_31 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_31.setObjectName(u"pushButton_31")
        icon9 = QIcon()
        icon9.addFile(u":/iconos/iconos/usdc_color.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_31.setIcon(icon9)
        self.pushButton_31.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_31, 11, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_14, 5, 1, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_16, 7, 1, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_12, 3, 1, 1, 1)

        self.pushButton_24 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_24.setObjectName(u"pushButton_24")
        icon10 = QIcon()
        icon10.addFile(u":/iconos/iconos/ethereum_color.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon10)
        self.pushButton_24.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_24, 4, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_5, 1, 1, 1, 1)

        self.pushButton_25 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setIcon(icon10)
        self.pushButton_25.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_25, 5, 0, 1, 1)

        self.pushButton_26 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setIcon(icon10)
        self.pushButton_26.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_26, 6, 0, 1, 1)

        self.pushButton_29 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setIcon(icon8)
        self.pushButton_29.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_29, 9, 0, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_15, 6, 1, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_17, 8, 1, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_19, 9, 1, 1, 1)

        self.pushButton_28 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setIcon(icon8)
        self.pushButton_28.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_28, 8, 0, 1, 1)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        icon11 = QIcon()
        icon11.addFile(u":/iconos/iconos/tether.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon11)
        self.pushButton.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_30 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setIcon(icon9)
        self.pushButton_30.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_30, 10, 0, 1, 1)

        self.pushButton_32 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setIcon(icon9)
        self.pushButton_32.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_32, 12, 0, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_22, 12, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_3)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_5 = QGridLayout(self.page_5)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.page_5)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_22)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_22)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)

        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.frame_23, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_22, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.page_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, 0, 3, 0)
        self.frame_18 = QFrame(self.frame_9)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_18)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_10.addWidget(self.pushButton_10)

        self.horizontalLayout_10.setStretch(0, 4)

        self.verticalLayout_5.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_9)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.frame_19)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_11.addWidget(self.pushButton_11)

        self.horizontalLayout_11.setStretch(0, 4)

        self.verticalLayout_5.addWidget(self.frame_19)

        self.frame_24 = QFrame(self.frame_9)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_12 = QPushButton(self.frame_24)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_12.addWidget(self.pushButton_12)

        self.horizontalLayout_12.setStretch(0, 4)

        self.verticalLayout_5.addWidget(self.frame_24)


        self.gridLayout_5.addWidget(self.frame_9, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.page)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_25)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_25)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 1)

        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.gridLayout_10.addWidget(self.frame_26, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_25, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 0, 3, 0)
        self.frame_17 = QFrame(self.frame_10)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.pushButton_16 = QPushButton(self.frame_17)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_16.addWidget(self.pushButton_16)

        self.horizontalLayout_16.setStretch(0, 4)

        self.verticalLayout_7.addWidget(self.frame_17)

        self.frame_27 = QFrame(self.frame_10)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pushButton_17 = QPushButton(self.frame_27)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_17.addWidget(self.pushButton_17)

        self.horizontalLayout_17.setStretch(0, 4)

        self.verticalLayout_7.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_10)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.pushButton_18 = QPushButton(self.frame_28)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_18.addWidget(self.pushButton_18)

        self.horizontalLayout_18.setStretch(0, 4)

        self.verticalLayout_7.addWidget(self.frame_28)


        self.gridLayout_2.addWidget(self.frame_10, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.page_2)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_33)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_33)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_11, 0, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.gridLayout_11.addWidget(self.frame_34, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_33, 0, 0, 1, 1)

        self.frame_29 = QFrame(self.page_2)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_29)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 0, 3, 0)
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.pushButton_19 = QPushButton(self.frame_30)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_19.addWidget(self.pushButton_19)

        self.horizontalLayout_19.setStretch(0, 4)

        self.verticalLayout_8.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pushButton_20 = QPushButton(self.frame_31)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_20.addWidget(self.pushButton_20)

        self.horizontalLayout_20.setStretch(0, 4)

        self.verticalLayout_8.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_29)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.pushButton_21 = QPushButton(self.frame_32)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.horizontalLayout_21.addWidget(self.pushButton_21)

        self.horizontalLayout_21.setStretch(0, 4)

        self.verticalLayout_8.addWidget(self.frame_32)


        self.gridLayout_3.addWidget(self.frame_29, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_8 = QGridLayout(self.page_4)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.page_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 0, 3, 0)
        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_11)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_6.addWidget(self.pushButton_7)

        self.horizontalLayout_6.setStretch(0, 4)

        self.verticalLayout_4.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame_13)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_7.addWidget(self.pushButton_8)

        self.horizontalLayout_7.setStretch(0, 4)

        self.verticalLayout_4.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_12)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_8.addWidget(self.pushButton_9)

        self.horizontalLayout_8.setStretch(0, 4)

        self.verticalLayout_4.addWidget(self.frame_12)


        self.gridLayout_8.addWidget(self.frame_8, 1, 0, 1, 1)

        self.frame_20 = QFrame(self.page_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_20)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_20)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.frame_21, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_20, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_6 = QVBoxLayout(self.page_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.frame_15 = QFrame(self.page_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 30))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_16)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 30))
        self.label_25.setFont(font)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_25)


        self.verticalLayout_10.addWidget(self.frame_16)

        self.frame_36 = QFrame(self.frame_15)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_36)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(200, 16777215))
        self.frame_38.setStyleSheet(u"")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_38)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, -1, 0, 0)
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_39)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(3, 0, 3, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 260, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.label_27 = QLabel(self.frame_39)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_13.addWidget(self.label_27)

        self.lineEdit_2 = QLineEdit(self.frame_39)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_2.setMaxLength(100)

        self.verticalLayout_13.addWidget(self.lineEdit_2)

        self.label_26 = QLabel(self.frame_39)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_13.addWidget(self.label_26)

        self.lineEdit = QLineEdit(self.frame_39)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setMaxLength(100)

        self.verticalLayout_13.addWidget(self.lineEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)


        self.verticalLayout_12.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(16777215, 50))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_33 = QPushButton(self.frame_40)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_9.addWidget(self.pushButton_33)

        self.pushButton_34 = QPushButton(self.frame_40)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_9.addWidget(self.pushButton_34)


        self.verticalLayout_12.addWidget(self.frame_40)


        self.horizontalLayout_5.addWidget(self.frame_38)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_10.addWidget(self.frame_36)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"BOT TRADE", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"BTC/USDT", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"ETH/USDT", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"BNB/USDT", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"USDC/USDT", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"CARTERA", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"USDT:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.pushButton_6.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"USDT", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"MC-BTC", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"MR-BTC", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"TF-BNB", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"TF-BTC", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"MR-USDC", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"TF-ETH", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"MR-ETH", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"MC-ETH", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"MC-BNB", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"MR-BNB", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"USDT", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"TF-USDC", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"MC-USDC", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"BNB/USDT", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"MeanReversionBot", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"TrendFollowingBot", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"MovingAverageCrossoverBot", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"USDC/USDT", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"MeanReversionBot", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"TrendFollowingBot", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"MovingAverageCrossoverBot", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ETH/USDT", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"MeanReversionBot", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"TrendFollowingBot", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"MovingAverageCrossoverBot", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"MeanReversionBot", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"TrendFollowingBot", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"MovingAverageCrossoverBot", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"BTC/USDT", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"USDT", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Comprar", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Vender", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())