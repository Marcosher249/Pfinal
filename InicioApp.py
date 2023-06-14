import os
import sys


from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QTimer
from ui_bottrade import *
from Custom_Widgets.Widgets import *
import asyncio
import timer
import api_bot


from functools import partial

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = LoginRegisterWindow()
#     window.show()
#     sys.exit(app.exec_())



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.stackedWidget.setCurrentIndex(0)
        self.int_validator = QIntValidator()
        self.ui.lineEdit_2.setValidator(self.int_validator)
        self.ui.lineEdit.setValidator(self.int_validator)
        self.ui.pushButton_2.clicked.connect(lambda: self.login())


        self.setMinimumSize(850, 600)
        self.datos = api_bot.api()
        loadJsonStyle(self, self.ui)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.set_coins)
        self.timer.start(2000)

        # Lanzar la función set_coins en segundo plano

    def login(self):
        email = str(self.ui.lineEdit_3.text())
        password = str(self.ui.lineEdit_4.text())
        datos = self.datos.login_api(email,password)
       
        usdt =datos["USDT"]
        tf_btc = datos["TF-BTC"]
        mr_btc = datos["MR-BTC"]
        mc_btc = datos["MC-BTC"]
        tf_eth = datos["TF-ETH"]
        mr_eth = datos["MR-ETH"]
        mc_eth = datos["MC-ETH"]
        tf_bnb = datos["TF-BNB"]
        mr_bnb = datos["MR-BNB"]
        mc_bnb = datos["MC-BNB"]
        tf_usdc = datos["TF-USDC"]
        mr_usdc = datos["MR-USDC"]
        mc_usdc = datos["MC-USDC"]


        self.ui.label_4.setText(str(usdt))
        self.ui.label_5.setText(str(tf_btc))
        self.ui.label_6.setText(str(mr_btc))
        self.ui.label_12.setText(str(mc_btc))
        self.ui.label_13.setText(str(tf_eth))
        self.ui.label_14.setText(str(mr_eth))
        self.ui.label_15.setText(str(mc_eth))
        self.ui.label_16.setText(str(tf_bnb))
        self.ui.label_17.setText(str(mr_bnb))
        self.ui.label_19.setText(str(mc_bnb))
        self.ui.label_20.setText(str(tf_usdc))
        self.ui.label_21.setText(str(mr_usdc))
        self.ui.label_22.setText(str(mc_usdc))

        self.ui.stackedWidget.setCurrentIndex(0)
                 

    def set_coins(self):
        print("Llega a la funcion de set coins")

        data= self.datos.get_bet_bots()
        for par,lista_para_par_deseado in data.items():
            par =str(par)
            for item in lista_para_par_deseado:

                bot_type = item["bot_type"]
                bet = item["bet"]
                        
                if par == "BTC/USDT" and bot_type == "MeanReversionBot":
                            # Acción cuando par y bot_type están vacíos
                    self.ui.pushButton_35.setText(str(bet))
                            
                elif par == "BTC/USDT" and bot_type == "TrendFollowingBot":
                            # Acción cuando par está vacío y bot_type no
                    self.ui.pushButton_36.setText(str(bet))
                            
                elif par == "BTC/USDT" and bot_type == "MovingAverageCrossoverBot":
                            # Acción cuando par no está vacío y bot_type está vacío
                    self.ui.pushButton_37.setText(str(bet))
                            
                elif par == "ETH/USDT"and bot_type == "MeanReversionBot":
                            # Acción cuando par está vacío
                    self.ui.pushButton_38.setText(str(bet))

                            
                elif par == "ETH/USDT" and bot_type == "TrendFollowingBot":
                            # Acción cuando par no está vacío y bot_type está vacío
                    self.ui.pushButton_39.setText(str(bet))
                            
                elif par == "ETH/USDT" and bot_type == "MovingAverageCrossoverBot":
                            # Acción cuando par no está vacío y bot_type está vacío
                    self.ui.pushButton_40.setText(str(bet))
                            
                elif par == "BNB/USDT" and bot_type == "MeanReversionBot":
                            # Acción cuando par está vacío
                    self.ui.pushButton_4.setText(str(bet))
                            
                elif par == "BNB/USDT" and bot_type == "TrendFollowingBot":
                            # Acción cuando par está vacío
                    self.ui.pushButton_22.setText(str(bet))
                elif par == "BNB/USDT" and bot_type == "MovingAverageCrossoverBot":
                            # Acción cuando par está vacío
                    self.ui.pushButton_23.setText(str(bet))
                            
                elif par == "USDC/USDT" and bot_type == "MeanReversionBot":
                            # Acción cuando par está vacío
                    self.ui.pushButton_41.setText(str(bet))
                elif par == "USDC/USDT" and bot_type == "TrendFollowingBot":
                            # Acción cuando par está vacío
                    self.ui.pushButton_42.setText(str(bet))
                            
                else:
                            # Acción por defecto
                    self.ui.pushButton_43.setText(str(bet))
                    print("se ha cambiado algo")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
