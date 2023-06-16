# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfa_definitivaChjnOb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(931, 760)
        MainWindow.setMinimumSize(QSize(0, 30))
        MainWindow.setStyleSheet(u"#frame_2{\n"
"	background-color: rgb(33, 43, 51);\n"
"}\n"
"#label{\n"
"color:rgb(255,255,255)\n"
"}\n"
"#frame_4,#frame_6{\n"
"	background-color: rgb(33, 43, 51);\n"
"}\n"
"\n"
"#stackedWidget_2{\n"
"	background-color: rgba(61, 80, 95, 100)\n"
"}\n"
"#frame_2 QLabel,#frame QLabel,#checkBox{\n"
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
"#page_BTC QPushButton,#page_BNB QPushButton,#page_ETH QPushButton,#page_USDC QPushButton,#page_CARTERA QPushButton{\n"
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
""
                        "	border: none;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents,#frame_5 QPushButton,#scrollArea{\n"
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
"}\n"
"#page_2{\n"
"background: url(:/login/Login/P"
                        "osition-trading.jpg)\n"
"\n"
"}\n"
"#frame_42{\n"
"background-color:rgba(220, 228, 255,225);\n"
"radius: 5px;\n"
"border-radius:10px\n"
"}\n"
"#frame_42 QLineEdit{\n"
"background-color: rgba(62, 105, 183, 175);\n"
"border:none;\n"
"min-height: 30px;\n"
"border-radius:5px;\n"
"color: rgba(255, 255, 255, 200)\n"
"}\n"
"#pushButton_2{\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgba(51, 102, 144,150);\n"
"border-radius:5px;\n"
"font-size: 13px;\n"
"}\n"
"#label_29,#label_30{\n"
"color:rgb(255, 255, 255);\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"\n"
"}\n"
"#pushButton_3{\n"
"color:rgb(255, 255, 255);\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"background:transparent;\n"
"background-color:transparent;\n"
"\n"
"}\n"
"#frame_51 QPushButton{\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(19, 44, 127,100);\n"
"border:2px solid rgba(0, 0, 176,150);\n"
"\n"
"}\n"
"#frame_23,#frame_21, #frame_34, #frame_26{\n"
"background-color:trasparent;\n"
"background:trasparent;\n"
"}\n"
"")
        self.centralwidget1 = QWidget(MainWindow)
        self.centralwidget1.setObjectName(u"centralwidget1")
        self.horizontalLayout = QHBoxLayout(self.centralwidget1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget1)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_13 = QHBoxLayout(self.page)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.menu = QCustomSlideMenu(self.page)
        self.menu.setObjectName(u"menu")
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
        self.pushButton_BNB = QPushButton(self.frame_4)
        self.pushButton_BNB.setObjectName(u"pushButton_BNB")
        self.pushButton_BNB.setMinimumSize(QSize(0, 30))
        icon = QIcon()
        icon.addFile(u":/iconos/iconos/bnb.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_BNB.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_BNB, 1, 0, 1, 1)

        self.pushButton_CARTERA = QPushButton(self.frame_4)
        self.pushButton_CARTERA.setObjectName(u"pushButton_CARTERA")
        self.pushButton_CARTERA.setMinimumSize(QSize(0, 30))
        icon1 = QIcon()
        icon1.addFile(u":/iconos/iconos/wallet.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_CARTERA.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton_CARTERA, 4, 0, 1, 1)

        self.pushButton_ETH = QPushButton(self.frame_4)
        self.pushButton_ETH.setObjectName(u"pushButton_ETH")
        self.pushButton_ETH.setMinimumSize(QSize(0, 30))
        icon2 = QIcon()
        icon2.addFile(u":/iconos/iconos/ethereum.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_ETH.setIcon(icon2)

        self.gridLayout.addWidget(self.pushButton_ETH, 2, 0, 1, 1)

        self.pushButton_USDC = QPushButton(self.frame_4)
        self.pushButton_USDC.setObjectName(u"pushButton_USDC")
        self.pushButton_USDC.setMinimumSize(QSize(0, 30))
        icon3 = QIcon()
        icon3.addFile(u":/iconos/iconos/usdc.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_USDC.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton_USDC, 3, 0, 1, 1)

        self.pushButton_BTC = QPushButton(self.frame_4)
        self.pushButton_BTC.setObjectName(u"pushButton_BTC")
        self.pushButton_BTC.setMinimumSize(QSize(0, 30))
        self.pushButton_BTC.setLayoutDirection(Qt.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u":/iconos/iconos/bitcoin.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_BTC.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton_BTC, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        icon5 = QIcon()
        icon5.addFile(u":/navegacion/imagenes_navegacion/person.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)

        self.gridLayout.addWidget(self.pushButton_6, 5, 0, 1, 1)


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


        self.gridLayout_6.addWidget(self.frame_14, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 318, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_6)


        self.horizontalLayout_13.addWidget(self.menu)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 0, 3, 3)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
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
        icon6 = QIcon()
        icon6.addFile(u":/navegacion/imagenes_navegacion/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon6)
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

        self.horizontalLayout_4.setStretch(2, 4)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_7)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setFont(font)
        self.page_CARTERA = QWidget()
        self.page_CARTERA.setObjectName(u"page_CARTERA")
        self.verticalLayout_2 = QVBoxLayout(self.page_CARTERA)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_35 = QFrame(self.page_CARTERA)
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

        self.scrollArea = QScrollArea(self.page_CARTERA)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 744, 623))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(9)
        self.gridLayout_4.setContentsMargins(3, 9, 9, 3)
        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_16, 7, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_15.setObjectName(u"pushButton_15")
        icon7 = QIcon()
        icon7.addFile(u":/iconos/iconos/bitcoin (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon7)
        self.pushButton_15.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_15, 3, 0, 1, 1)

        self.pushButton_28 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_28.setObjectName(u"pushButton_28")
        icon8 = QIcon()
        icon8.addFile(u":/iconos/iconos/binance_color.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_28.setIcon(icon8)
        self.pushButton_28.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_28, 8, 0, 1, 1)

        self.pushButton_29 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setIcon(icon8)
        self.pushButton_29.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_29, 9, 0, 1, 1)

        self.pushButton_31 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_31.setObjectName(u"pushButton_31")
        icon9 = QIcon()
        icon9.addFile(u":/iconos/iconos/usdc_color.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_31.setIcon(icon9)
        self.pushButton_31.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_31, 11, 0, 1, 1)

        self.pushButton_30 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setIcon(icon9)
        self.pushButton_30.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_30, 10, 0, 1, 1)

        self.pushButton_24 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_24.setObjectName(u"pushButton_24")
        icon10 = QIcon()
        icon10.addFile(u":/iconos/iconos/ethereum_color.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon10)
        self.pushButton_24.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_24, 4, 0, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_21, 11, 1, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_20, 10, 1, 1, 1)

        self.pushButton_27 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setIcon(icon8)
        self.pushButton_27.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_27, 7, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setIcon(icon7)
        self.pushButton_13.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_13, 1, 0, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_22, 12, 1, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_19, 9, 1, 1, 1)

        self.pushButton_26 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setIcon(icon10)
        self.pushButton_26.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_26, 6, 0, 1, 1)

        self.pushButton_25 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setIcon(icon10)
        self.pushButton_25.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_25, 5, 0, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_15, 6, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_6, 2, 1, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_5, 1, 1, 1, 1)

        self.pushButton_32 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setIcon(icon9)
        self.pushButton_32.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_32, 12, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_14, 5, 1, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_17, 8, 1, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_13, 4, 1, 1, 1)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        icon11 = QIcon()
        icon11.addFile(u":/iconos/iconos/tether.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon11)
        self.pushButton.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_12, 3, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setIcon(icon7)
        self.pushButton_14.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.pushButton_14, 2, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.stackedWidget_2.addWidget(self.page_CARTERA)
        self.page_BNB = QWidget()
        self.page_BNB.setObjectName(u"page_BNB")
        self.gridLayout_5 = QGridLayout(self.page_BNB)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.page_BNB)
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

        self.frame_9 = QFrame(self.page_BNB)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 9, 9)
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

        self.pushButton_mr_bnb = QPushButton(self.frame_18)
        self.pushButton_mr_bnb.setObjectName(u"pushButton_mr_bnb")
        self.pushButton_mr_bnb.setMinimumSize(QSize(20, 30))
        self.pushButton_mr_bnb.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.pushButton_mr_bnb)

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

        self.pushButton_tf_bnb = QPushButton(self.frame_19)
        self.pushButton_tf_bnb.setObjectName(u"pushButton_tf_bnb")
        self.pushButton_tf_bnb.setMinimumSize(QSize(20, 30))

        self.horizontalLayout_11.addWidget(self.pushButton_tf_bnb)

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

        self.pushButton_mc_bnb = QPushButton(self.frame_24)
        self.pushButton_mc_bnb.setObjectName(u"pushButton_mc_bnb")
        self.pushButton_mc_bnb.setMinimumSize(QSize(20, 30))

        self.horizontalLayout_12.addWidget(self.pushButton_mc_bnb)

        self.horizontalLayout_12.setStretch(0, 4)

        self.verticalLayout_5.addWidget(self.frame_24)


        self.gridLayout_5.addWidget(self.frame_9, 1, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_BNB)
        self.page_USDC = QWidget()
        self.page_USDC.setObjectName(u"page_USDC")
        self.gridLayout_2 = QGridLayout(self.page_USDC)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.page_USDC)
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

        self.frame_10 = QFrame(self.page_USDC)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 0, 9, 9)
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

        self.pushButton_mr_usdc = QPushButton(self.frame_17)
        self.pushButton_mr_usdc.setObjectName(u"pushButton_mr_usdc")
        self.pushButton_mr_usdc.setMinimumSize(QSize(20, 30))

        self.horizontalLayout_16.addWidget(self.pushButton_mr_usdc)

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

        self.pushButton_tf_usdc = QPushButton(self.frame_27)
        self.pushButton_tf_usdc.setObjectName(u"pushButton_tf_usdc")
        self.pushButton_tf_usdc.setMinimumSize(QSize(20, 30))

        self.horizontalLayout_17.addWidget(self.pushButton_tf_usdc)

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

        self.pushButton_mc_usdc = QPushButton(self.frame_28)
        self.pushButton_mc_usdc.setObjectName(u"pushButton_mc_usdc")
        self.pushButton_mc_usdc.setMinimumSize(QSize(20, 30))

        self.horizontalLayout_18.addWidget(self.pushButton_mc_usdc)

        self.horizontalLayout_18.setStretch(0, 4)

        self.verticalLayout_7.addWidget(self.frame_28)


        self.gridLayout_2.addWidget(self.frame_10, 1, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_USDC)
        self.page_ETH = QWidget()
        self.page_ETH.setObjectName(u"page_ETH")
        self.gridLayout_3 = QGridLayout(self.page_ETH)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.page_ETH)
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

        self.frame_29 = QFrame(self.page_ETH)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_29)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 0, 9, 9)
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

        self.pushButton_mr_eth = QPushButton(self.frame_30)
        self.pushButton_mr_eth.setObjectName(u"pushButton_mr_eth")
        self.pushButton_mr_eth.setMinimumSize(QSize(20, 30))

        self.horizontalLayout_19.addWidget(self.pushButton_mr_eth)

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

        self.pushButton_tf_eth = QPushButton(self.frame_31)
        self.pushButton_tf_eth.setObjectName(u"pushButton_tf_eth")
        self.pushButton_tf_eth.setMinimumSize(QSize(20, 30))

        self.horizontalLayout_20.addWidget(self.pushButton_tf_eth)

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

        self.pushButton_mc_eth = QPushButton(self.frame_32)
        self.pushButton_mc_eth.setObjectName(u"pushButton_mc_eth")
        self.pushButton_mc_eth.setMinimumSize(QSize(20, 30))

        self.horizontalLayout_21.addWidget(self.pushButton_mc_eth)

        self.horizontalLayout_21.setStretch(0, 4)

        self.verticalLayout_8.addWidget(self.frame_32)


        self.gridLayout_3.addWidget(self.frame_29, 1, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_ETH)
        self.page_BTC = QWidget()
        self.page_BTC.setObjectName(u"page_BTC")
        self.gridLayout_8 = QGridLayout(self.page_BTC)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.page_BTC)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, 9, 9)
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

        self.pushButton_mr_btc = QPushButton(self.frame_11)
        self.pushButton_mr_btc.setObjectName(u"pushButton_mr_btc")
        self.pushButton_mr_btc.setMinimumSize(QSize(20, 30))

        self.horizontalLayout_6.addWidget(self.pushButton_mr_btc)

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

        self.pushButton_tf_btc = QPushButton(self.frame_13)
        self.pushButton_tf_btc.setObjectName(u"pushButton_tf_btc")
        self.pushButton_tf_btc.setMinimumSize(QSize(20, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_tf_btc)

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

        self.pushButton_mc_btc = QPushButton(self.frame_12)
        self.pushButton_mc_btc.setObjectName(u"pushButton_mc_btc")
        self.pushButton_mc_btc.setMinimumSize(QSize(20, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_mc_btc)

        self.horizontalLayout_8.setStretch(0, 4)

        self.verticalLayout_4.addWidget(self.frame_12)


        self.gridLayout_8.addWidget(self.frame_8, 1, 0, 1, 1)

        self.frame_20 = QFrame(self.page_BTC)
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

        self.stackedWidget_2.addWidget(self.page_BTC)
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
        self.frame_48 = QFrame(self.frame_39)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(0, 70))
        self.frame_48.setMaximumSize(QSize(16777215, 70))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_48)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_48)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, 0)
        self.label_31 = QLabel(self.frame_47)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_23.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_47)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_23.addWidget(self.label_32)


        self.verticalLayout_16.addWidget(self.frame_47)

        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.label_33 = QLabel(self.frame_49)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_24.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_49)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_24.addWidget(self.label_34)


        self.verticalLayout_16.addWidget(self.frame_49)


        self.verticalLayout_13.addWidget(self.frame_48)

        self.verticalSpacer_2 = QSpacerItem(20, 260, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_2)

        self.frame_51 = QFrame(self.frame_39)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_51)
        self.verticalLayout_17.setSpacing(2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 3)
        self.label_27 = QLabel(self.frame_51)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_17.addWidget(self.label_27)

        self.lineEdit_2 = QLineEdit(self.frame_51)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_2.setMaxLength(100)

        self.verticalLayout_17.addWidget(self.lineEdit_2)

        self.label_26 = QLabel(self.frame_51)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_17.addWidget(self.label_26)

        self.lineEdit = QLineEdit(self.frame_51)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setMaxLength(100)

        self.verticalLayout_17.addWidget(self.lineEdit)


        self.verticalLayout_13.addWidget(self.frame_51)


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

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_10.addWidget(self.frame_36)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.stackedWidget_2.addWidget(self.page_6)

        self.verticalLayout_9.addWidget(self.stackedWidget_2)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_13.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_15 = QHBoxLayout(self.page_2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QFrame(self.page_2)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_45)

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(400, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(400, 16777215))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.frame)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(400, 500))
        self.frame_42.setMaximumSize(QSize(400, 500))
        self.frame_42.setStyleSheet(u"")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_42)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(75, 0, 75, 0)
        self.label_28 = QLabel(self.frame_42)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(250, 200))
        font1 = QFont()
        font1.setFamily(u"Bauhaus 93")
        font1.setPointSize(18)
        self.label_28.setFont(font1)
        self.label_28.setStyleSheet(u"color:rgb(255, 255, 255);border-radius:5px")
        self.label_28.setTextFormat(Qt.PlainText)
        self.label_28.setScaledContents(False)
        self.label_28.setAlignment(Qt.AlignCenter)
        self.label_28.setMargin(0)

        self.verticalLayout_15.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_42)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_15.addWidget(self.label_29)

        self.lineEdit_3 = QLineEdit(self.frame_42)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_3.setStyleSheet(u"")

        self.verticalLayout_15.addWidget(self.lineEdit_3)

        self.label_30 = QLabel(self.frame_42)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 20))
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.label_30)

        self.lineEdit_4 = QLineEdit(self.frame_42)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_4.setStyleSheet(u"")
        self.lineEdit_4.setEchoMode(QLineEdit.Password)

        self.verticalLayout_15.addWidget(self.lineEdit_4)

        self.checkBox = QCheckBox(self.frame_42)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_15.addWidget(self.checkBox)

        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(0, 0))
        self.frame_43.setMaximumSize(QSize(250, 16777215))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(15, -1, 15, -1)
        self.pushButton_2 = QPushButton(self.frame_43)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setMaximumSize(QSize(200, 16777215))
        self.pushButton_2.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.pushButton_2)


        self.verticalLayout_15.addWidget(self.frame_43)


        self.verticalLayout_14.addWidget(self.frame_42)

        self.frame_44 = QFrame(self.frame)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMaximumSize(QSize(16777215, 16777215))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_3 = QPushButton(self.frame_44)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_22.addWidget(self.pushButton_3)


        self.verticalLayout_14.addWidget(self.frame_44)


        self.horizontalLayout_15.addWidget(self.frame)

        self.frame_46 = QFrame(self.page_2)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_46)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget1)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"BOT TRADE", None))
        self.pushButton_BNB.setText(QCoreApplication.translate("MainWindow", u"BNB/USDT", None))
        self.pushButton_CARTERA.setText(QCoreApplication.translate("MainWindow", u"CARTERA", None))
        self.pushButton_ETH.setText(QCoreApplication.translate("MainWindow", u"ETH/USDT", None))
        self.pushButton_USDC.setText(QCoreApplication.translate("MainWindow", u"USDC/USDT", None))
        self.pushButton_BTC.setText(QCoreApplication.translate("MainWindow", u"BTC/USDT", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"INICIAR SESION", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"USDT:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"USDT", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"MC-BTC", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"MR-BNB", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"MC-BNB", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"MR-USDC", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"TF-USDC", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"TF-ETH", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"TF-BNB", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"TF-BTC", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"MC-ETH", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"MR-ETH", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"MC-USDC", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"USDT", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"MR-BTC", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"BNB/USDT", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"MeanReversionBot", None))
        self.pushButton_mr_bnb.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"TrendFollowingBot", None))
        self.pushButton_tf_bnb.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"MovingAverageCrossoverBot", None))
        self.pushButton_mc_bnb.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"USDC/USDT", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"MeanReversionBot", None))
        self.pushButton_mr_usdc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"TrendFollowingBot", None))
        self.pushButton_tf_usdc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"MovingAverageCrossoverBot", None))
        self.pushButton_mc_usdc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ETH/USDT", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"MeanReversionBot", None))
        self.pushButton_mr_eth.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"TrendFollowingBot", None))
        self.pushButton_tf_eth.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"MovingAverageCrossoverBot", None))
        self.pushButton_mc_eth.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"MeanReversionBot", None))
        self.pushButton_mr_btc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"TrendFollowingBot", None))
        self.pushButton_tf_btc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"MovingAverageCrossoverBot", None))
        self.pushButton_mc_btc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"BTC/USDT", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"coin", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"USDT", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lineEdit_2.setPlaceholderText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"USDT", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"USDT", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Vender", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Comprar", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Recuerdame", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Sing Up", None))
    # retranslateUi

