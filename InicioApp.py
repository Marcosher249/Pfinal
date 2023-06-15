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
        

        self.ui.pushButton_2.clicked.connect(lambda: self.login_singup())

        self.ui.pushButton_13.clicked.connect(lambda: self.exchange("TF-BTC"))
        self.ui.pushButton_14.clicked.connect(lambda: self.exchange("MR-BTC"))
        self.ui.pushButton_15.clicked.connect(lambda: self.exchange("MC-BTC"))
        self.ui.pushButton_24.clicked.connect(lambda: self.exchange("TF-ETH"))
        self.ui.pushButton_25.clicked.connect(lambda: self.exchange("MR-ETH"))
        self.ui.pushButton_26.clicked.connect(lambda: self.exchange("MC-ETH"))
        self.ui.pushButton_27.clicked.connect(lambda: self.exchange("TF-BNB"))
        self.ui.pushButton_28.clicked.connect(lambda: self.exchange("MR-BNB"))
        self.ui.pushButton_29.clicked.connect(lambda: self.exchange("MC-BNB"))
        self.ui.pushButton_30.clicked.connect(lambda: self.exchange("TF-USDC"))
        self.ui.pushButton_31.clicked.connect(lambda: self.exchange("MR-USDC"))
        self.ui.pushButton_32.clicked.connect(lambda: self.exchange("MC-USDC"))


        self.ui.pushButton_8.clicked.connect(lambda: self.exchange("TF-BTC"))
        self.ui.pushButton_7.clicked.connect(lambda: self.exchange("MR-BTC"))
        self.ui.pushButton_9.clicked.connect(lambda: self.exchange("MC-BTC"))
        self.ui.pushButton_20.clicked.connect(lambda: self.exchange("TF-ETH"))
        self.ui.pushButton_19.clicked.connect(lambda: self.exchange("MR-ETH"))
        self.ui.pushButton_21.clicked.connect(lambda: self.exchange("MC-ETH"))
        self.ui.pushButton_11.clicked.connect(lambda: self.exchange("TF-BNB"))
        self.ui.pushButton_10.clicked.connect(lambda: self.exchange("MR-BNB"))
        self.ui.pushButton_12.clicked.connect(lambda: self.exchange("MC-BNB"))
        self.ui.pushButton_17.clicked.connect(lambda: self.exchange("TF-USDC"))
        self.ui.pushButton_16.clicked.connect(lambda: self.exchange("MR-USDC"))
        self.ui.pushButton_18.clicked.connect(lambda: self.exchange("MC-USDC"))

        self.ui.pushButton_3.clicked.connect(lambda: self.change_login_singup())
        
        inicio = self.ui.label_28.text()
        self.inicio = str(inicio)

        self.usdt = "0"
        self.tf_btc = "0"
        self.mr_btc ="0"
        self.mc_btc ="0"
        self.tf_eth = "0"
        self.mr_eth = "0"
        self.mc_eth = "0"
        self.tf_bnb = "0"
        self.mr_bnb = "0"
        self.mc_bnb = "0"
        self.tf_usdc = "0"
        self.mr_usdc = "0"
        self.mc_usdc = "0"
        self.setMinimumSize(850, 600)
        self.datos = api_bot.api()
        loadJsonStyle(self, self.ui)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.set_coins)
        self.timer.start(2000)
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.hola)
        self.timer2.start(3000)

        # Lanzar la función set_coins en segundo plano
    def hola(self):
        print("hola")

    def sell_buy(self,coin_compra,coin_venta):

        idUser = self.idUser
        
        str_compra =self.ui.lineEdit.text()
        compra = float(str_compra)
        str_venta =self.ui.lineEdit_2.text()
        venta = float(str_venta)
        respuesta = self.datos.sell_buy(idUser,coin_compra,compra,coin_venta,venta)
        
        
        if respuesta["respuesta"]=="si":
            self.sum_rest(coin_compra,compra,coin_venta,venta)
        else:
            pass

    def sum_rest(self,coin_compra,compra,coin_venta,venta):
        
        monedas = {
            'TF-BTC': ['tf_btc','label_5'],
            'MR-BTC': ['mr_btc','label_6'],
            'MC-BTC': ['mc_btc','label_12'],
            'TF-ETH': ['tf_eth','label_13'],
            'MR-ETH': ['mr_eth','label_14'],
            'MC-ETH': ['mc_eth','label_15'],
            'TF-BNB': ['tf_bnb','label_16'],
            'MR-BNB': ['mr_bnb','label_17'],
            'MC-BNB': ['mc_bnb','label_19'],
            'TF-USDC': ['tf_usdc','label_20'],
            'MR-USDC': ['mr_usdc','label_21'],
            'MC-USDC': ['mc_usdc','label_22']
        }

        if coin_compra in monedas:
            lista = monedas[coin_compra]
            moneda_compra= lista[0]
            nombre_obj=lista[1]
            objeto = getattr(self.ui, nombre_obj)
            self_coin_total = getattr(self, moneda_compra)
            coin_total = float(self_coin_total) + compra
            objeto.setText(str(coin_total))
            usdt = self.usdt
            usdt_total = float(usdt) - venta

        else:
            lista = monedas[coin_venta]
            moneda_venta= lista[0]
            nombre_obj=lista[1]
            objeto = getattr(self.ui, nombre_obj)
            self_coin_total = getattr(self, moneda_venta)
            coin_total = float(self_coin_total) - venta
            self_coin_total = str()
            objeto.setText(str(coin_total))
            usdt = self.usdt
            usdt_total = float(usdt) + compra

        self.ui.label_32.setText(str(coin_total))
        self.ui.label_4.setText(str(usdt_total))

        

    
    def exchange(self,moneda):

        monedas = {
            'TF-BTC': 'tf_btc',
            'MR-BTC': 'mr_btc',
            'MC-BTC': 'mc_btc',
            'TF-ETH': 'tf_eth',
            'MR-ETH': 'mr_eth',
            'MC-ETH': 'mc_eth',
            'TF-BNB': 'tf_bnb',
            'MR-BNB': 'mr_bnb',
            'MC-BNB': 'mc_bnb',
            'TF-USDC': 'tf_usdc',
            'MR-USDC': 'mr_usdc',
            'MC-USDC': 'mc_usdc'
        }

        if moneda in monedas:
            self_str = monedas[moneda]
            tope_str = getattr(self, self_str)

        usdtstr = self.usdt
        usdtint = float(usdtstr)
        tope_int = float(tope_str)

        self.int_validator = QIntValidator(0,usdtint)
        self.int_validator2 = QIntValidator(0,tope_int)
        self.ui.lineEdit_2.setValidator(self.int_validator2)
        self.ui.lineEdit.setValidator(self.int_validator)
        self.ui.lineEdit.textChanged.connect(self.focus("lineEdit",self_str,"lineEdit_2"))
        self.ui.lineEdit_2.textChanged.connect(self.focus("lineEdit_2",self_str,"lineEdit"))
        self.ui.label_32.setText(tope_str)
        self.ui.label_34.setText(usdtstr)
        self.ui.label_31.setText(moneda)
        self.ui.label_25.setText(moneda)
        self.ui.label_27.setText(moneda)
        self.ui.pushButton_33.clicked.connect(lambda: self.sell_buy("USDT",moneda,))
        self.ui.pushButton_34.clicked.connect(lambda: self.sell_buy(moneda,"USDT"))
        self.ui.stackedWidget_2.setCurrentIndex(5)
    
    def focus(self,nombre,self_str,nombre2):
        nombreButt= "pushButton_" +self_str
        
        objeto = getattr(self.ui, nombre)
        objeto2 = getattr(self.ui,nombreButt)
        objeto3 =getattr(self.ui,nombre2)
        if objeto.hasFocus():
            str_multiplicado = objeto.text()
            int_multiplicado = float(str_multiplicado)
            str_multiplicador = objeto2.text()
            int_multiplicador = float(str_multiplicador)
            total = int_multiplicado * int_multiplicador
            str_total = str(total)
            objeto3.setText(str_total)
            
            


    def login_singup(self):
        if self.inicio == "Login":
            email = str(self.ui.lineEdit_3.text())
            password = str(self.ui.lineEdit_4.text())
            datos = self.datos.login_api(email,password)

            self.idUser = datos["idUser"]
            self.usdt =datos["USDT"]
            self.tf_btc = datos["TF-BTC"]
            self.mr_btc = datos["MR-BTC"]
            self.mc_btc = datos["MC-BTC"]
            self.tf_eth = datos["TF-ETH"]
            self.mr_eth = datos["MR-ETH"]
            self.mc_eth = datos["MC-ETH"]
            self.tf_bnb = datos["TF-BNB"]
            self.mr_bnb = datos["MR-BNB"]
            self.mc_bnb = datos["MC-BNB"]
            self.tf_usdc = datos["TF-USDC"]
            self.mr_usdc = datos["MR-USDC"]
            self.mc_usdc = datos["MC-USDC"]

            self.ui.label_24.setText(str(self.usdt))
            self.ui.label_4.setText(str(self.usdt))
            self.ui.label_5.setText(str(self.tf_btc))
            self.ui.label_6.setText(str(self.mr_btc))
            self.ui.label_12.setText(str(self.mc_btc))
            self.ui.label_13.setText(str(self.tf_eth))
            self.ui.label_14.setText(str(self.mr_eth))
            self.ui.label_15.setText(str(self.mc_eth))
            self.ui.label_16.setText(str(self.tf_bnb))
            self.ui.label_17.setText(str(self.mr_bnb))
            self.ui.label_19.setText(str(self.mc_bnb))
            self.ui.label_20.setText(str(self.tf_usdc))
            self.ui.label_21.setText(str(self.mr_usdc))
            self.ui.label_22.setText(str(self.mc_usdc))

            self.ui.pushButton_6.setText("CERRAR SESIÓN")

            self.ui.stackedWidget.setCurrentIndex(0)
        else:
            email = str(self.ui.lineEdit_3.text())
            password = str(self.ui.lineEdit_4.text())
            datos = self.datos.sing_up_api(email,password)
            self.idUser = datos
            self.ui.pushButton_6.setText("CERRAR SESIÓN")

            self.ui.label_24.setText("1000")

            self.ui.stackedWidget.setCurrentIndex(0)
            
    
    def change_login_singup(self):
        if self.inicio == "Login":
            self.ui.label_28.setText("Sing Up")
            self.ui.pushButton_2.setText("Sing Up")
            self.ui.pushButton_3.setText("Login")
            self.inicio = "Sing Up"
        else:
            self.ui.label_28.setText("Login")
            self.ui.pushButton_2.setText("Login")
            self.ui.pushButton_3.setText("Sing Up")
            self.inicio = "Login"
        
                 

    def set_coins(self):
        total = 0.0
        data= self.datos.get_bet_bots()
        for par,lista_para_par_deseado in data.items():
            par =str(par)
            for item in lista_para_par_deseado:

                bot_type = item["bot_type"]
                bet = item["bet"]
                        
                if par == "BTC/USDT" and bot_type == "MeanReversionBot":
                    valor = str(bet)
                    self.ui.pushButton_mr_btc.setText(valor)
                    try:
                        value_bot=self.mr_btc
                        numero = float(value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")
                            
                elif par == "BTC/USDT" and bot_type == "TrendFollowingBot":
                    valor = str(bet)
                    self.ui.pushButton_tf_btc.setText(valor)
                    try:
                        value_bot=self.tf_btc
                        numero = float(value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")
                elif par == "BTC/USDT" and bot_type == "MovingAverageCrossoverBot":
                    valor = str(bet)
                    self.ui.pushButton_mc_btc.setText(valor)
                    try:
                        value_bot = self.mc_btc
                        numero = float(value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")
                            
                elif par == "ETH/USDT"and bot_type == "MeanReversionBot":
                    valor = str(bet)
                    self.ui.pushButton_mr_eth.setText(valor)
                    try:
                        value_bot = self.mr_eth
                        numero = float(value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")

                            
                elif par == "ETH/USDT" and bot_type == "TrendFollowingBot":
                    valor = str(bet)
                    self.ui.pushButton_tf_eth.setText(valor)
                    try:
                        value_bot=self.tf_eth
                        numero = float(value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")
                            
                elif par == "ETH/USDT" and bot_type == "MovingAverageCrossoverBot":
                    valor = str(bet)
                    self.ui.pushButton_mc_eth.setText(valor)
                    try:
                        value_bot = self.mc_eth
                        numero = float(value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")
                            
                elif par == "BNB/USDT" and bot_type == "MeanReversionBot":
                    valor = str(bet)
                    self.ui.pushButton_mr_bnb.setText(valor)
                    try:
                        value_bot = self.mr_bnb
                        numero = float(value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")
                            
                elif par == "BNB/USDT" and bot_type == "TrendFollowingBot":       
                    valor = str(bet)
                    self.ui.pushButton_tf_bnb.setText(valor)
                    try:
                        value_bot = self.tf_bnb
                        numero = float(value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")
                elif par == "BNB/USDT" and bot_type == "MovingAverageCrossoverBot":

                    valor = str(bet)
                    self.ui.pushButton_mc_bnb.setText(valor)
                    try:
                        value_bot = self.mc_bnb
                        numero = float(value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")
                            
                elif par == "USDC/USDT" and bot_type == "MeanReversionBot":
                    valor = str(bet)
                    self.ui.pushButton_mr_usdc.setText(valor)
                    try:
                        value_bot = self.mr_usdc
                        numero = float(value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")
                elif par == "USDC/USDT" and bot_type == "TrendFollowingBot":
                    valor = str(bet)
                    self.ui.pushButton_tf_usdc.setText(valor)
                    try:
                        value_bot =self.tf_usdc
                        numero = float( value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")                    
                            
                else:
                    valor = str(bet)
                    self.ui.pushButton_mc_usdc.setText(valor)
                    try:
                        value_bot =self.mc_usdc
                        numero = float(value_bot)
                        val =float(valor)
                        total += (numero*val)
                    except ValueError:
                        print("El texto no puede convertirse a float")


        usdt = float(self.usdt)
        self.ui.label_2.setText(str(total+usdt))
        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
