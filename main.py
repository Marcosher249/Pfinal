import sys
from grafica import datos_graficas

from PySide2.QtGui import QPainter
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QTimer
from ui_bottrade import *
from Custom_Widgets.Widgets import *
import pandas as pd
import api_bot
import multiprocessing
import asyncio
from ui_ventana_de_dialogo import Ui_Dialog


#######################################################################################
################################# User Interface ######################################
 
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_6.clicked.connect(lambda: self.login_logout())
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)

        self.ui.pushButton_BTC.clicked.connect(lambda: self.cambio_diconnect(4))
        self.ui.pushButton_BNB.clicked.connect(lambda: self.cambio_diconnect(1))
        self.ui.pushButton_ETH.clicked.connect(lambda: self.cambio_diconnect(3))
        self.ui.pushButton_USDC.clicked.connect(lambda: self.cambio_diconnect(2))
        self.ui.pushButton_CARTERA.clicked.connect(lambda: self.cambio_diconnect(0))

        
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
        
        self.dialog = QDialog()
        self.ui2 = Ui_Dialog()
        self.ui2.setupUi(self.dialog)


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
        self.conect= 0
        self.graf = 0

        with open("jsonUser/id_user.json", "r") as archivo:
            datos = json.load(archivo)
        
        if len(datos)!=0:
            for email in datos:
                emailRecordado = email
                contraseña = datos[email]
            self.login_o_recordar(emailRecordado,contraseña)


        self.ui.layoutExchange = QVBoxLayout(self.ui.frame_37)
        self.ui.layout_bnb = QVBoxLayout(self.ui.frame_23)
        self.ui.layout_btc = QVBoxLayout(self.ui.frame_21)
        self.ui.layout_eth = QVBoxLayout(self.ui.frame_34)
        self.ui.layout_usdc = QVBoxLayout(self.ui.frame_26)
        self.ui.frame_37.setStyleSheet("background-color: transparent;")
        self.ui.frame_23.setStyleSheet("background-color: transparent;")
        self.ui.frame_21.setStyleSheet("background-color: transparent;")
        self.ui.frame_34.setStyleSheet("background-color: transparent;")
        self.ui.frame_26.setStyleSheet("background-color: transparent;")

        self.listcsv = {'csv/datos_bnb.csv':'layout_bnb', 'csv/datos_btc.csv':'layout_btc', 'csv/datos_eth.csv':'layout_eth',
                    'csv/datos_usdc.csv':'layout_usdc'}
        for csv in self.listcsv:
            self.load_data_and_create_chart(csv, self.listcsv[csv])
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.update_charts)
        self.timer2.start(30000)
        self.timer3 = QTimer()
    


    


    ###############################################################################
    ################     Funcion crear graficas y actualizarlas      ##############
    
    def load_data_and_create_chart(self, csv_file, layoot):
        obj_layout = getattr(self.ui, layoot)

        # Eliminar el diseño vertical existente, si lo hay

        df = pd.read_csv(csv_file)
        series = QtCharts.QLineSeries()

        for index, row in df.iterrows():
            date_str = row['Date']
            close = row['Close']
            date_time = QDateTime.fromString(date_str, "yyyy-MM-dd hh:mm:ss")
            series.append(date_time.toSecsSinceEpoch(), close)

    def load_data_and_create_chart(self, csv_file_or_list,layoot,moneda=""):
        obj_layout = getattr(self.ui, layoot)

        # Eliminar el diseño vertical existente, si lo hay

        series = QtCharts.QLineSeries()

        if moneda == "":
            df = pd.read_csv(csv_file_or_list)
            
            for index, row in df.iterrows():
                date_str = row['Date']
                close = row['Close']
                date_time = QDateTime.fromString(date_str, "yyyy-MM-dd hh:mm:ss")
                series.append(date_time.toSecsSinceEpoch(), close)
        else:
            lista = self.datos.get_dataf_pair_bot(moneda)
            for data_point in lista:
                date_str = data_point['date']
                close = data_point['bet']
                date_time = QDateTime.fromString(date_str, "yyyy-MM-dd hh:mm:ss")
                series.append(date_time.toSecsSinceEpoch(), close)
                print("se actualiza el que no se tiene que actualizar")
                if self.graf == 0:
                    self.graf=1

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()

        axis_x = QtCharts.QDateTimeAxis()
        axis_x.setLabelsVisible(False)
        chart.setAxisX(axis_x, series)

        background_color = QColor(148, 148, 148, 175)
        chart.setBackgroundBrush(QBrush(background_color))
        chart_view = QtCharts.QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing, True)

        if self.graf !=0:
            while obj_layout.count() > 0:
                item = obj_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        
        obj_layout.addWidget(chart_view)
        obj_layout.setContentsMargins(0, 0, 0, 0)
        obj_layout.setSpacing(0)
        self.graf=1
        

    def update_charts(self):
        for csv in self.listcsv:
            self.load_data_and_create_chart(csv, self.listcsv[csv])
            print("se actualiza")


 

    ###############################################################################



    ###############################################################################
    ######################### Funcion de reseteo de conexiones #################### 
    def cambio_diconnect(self, indice):
        self.ui.stackedWidget_2.setCurrentIndex(indice)
        if self.conect != 0:
            self.ui.pushButton_34.clicked.disconnect()
            self.ui.pushButton_33.clicked.disconnect()
            self.ui.lineEdit.textChanged.disconnect()
            self.ui.lineEdit_2.textChanged.disconnect()

            self.conect= 0
    ###############################################################################


    ###############################################################################
    ####### Funciones en la pagina para realizar las compras y ventas ############# 
  
    def exchange(self,moneda):

        self.conect= 1
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
            print(self_str)
            tope_str = getattr(self, self_str)

        

        usdtstr = self.usdt
        self.ui.label_32.setText(tope_str)
        self.ui.label_34.setText(usdtstr)

        self.timer3.timeout.connect(self.load_data_and_create_chart("","layoutExchange",moneda))
        self.timer3.start(1000)


        usdtint = float(usdtstr)
        tope_int = float(tope_str)

        self.int_validator = QIntValidator(0,usdtint)
        self.int_validator2 = QIntValidator(0,tope_int)
        self.ui.lineEdit_2.setValidator(self.int_validator2)
        self.ui.lineEdit.setValidator(self.int_validator)
        self.ui.lineEdit.textChanged.connect(lambda: self.focus("lineEdit",self_str,"lineEdit_2"))
        self.ui.lineEdit_2.textChanged.connect(lambda: self.focus("lineEdit_2",self_str,"lineEdit"))
        
        self.ui.label_31.setText(moneda)
        self.ui.label_25.setText(moneda)
        self.ui.label_27.setText(moneda)
        self.ui.pushButton_33.clicked.connect(lambda: self.sell_buy("USDT",moneda,))
        self.ui.pushButton_34.clicked.connect(lambda: self.sell_buy(moneda,"USDT"))
        self.ui.stackedWidget_2.setCurrentIndex(5)

            


    
    def focus(self, nombre, self_str, nombre2):
        nombreButt = "pushButton_" + self_str

        objeto = getattr(self.ui, nombre)
        objeto2 = getattr(self.ui, nombreButt)
        objeto3 = getattr(self.ui, nombre2)

        if objeto.hasFocus():
            str_multiplicado = objeto.text()
            str_multiplicador = objeto2.text()

            if str_multiplicado and str_multiplicador:  # Verificar que las cadenas no estén vacías
                int_multiplicado = float(str_multiplicado)
                int_multiplicador = float(str_multiplicador)

                if nombre == "lineEdit":
                    total = int_multiplicado * int_multiplicador
                else:
                    total = int_multiplicado / int_multiplicador

                str_total = str(total)
                objeto3.setText(str_total)
            else:
                objeto3.setText("")      
            
            
    def sell_buy(self,coin_compra,coin_venta):

        idUser = self.idUser
        
        str_compra =self.ui.lineEdit.text()
        compra = float(str_compra)
        str_venta =self.ui.lineEdit_2.text()
        venta = float(str_venta)
        respuesta = self.datos.sell_buy(idUser,coin_compra,str(compra),coin_venta,str(venta))
        
        
        if respuesta["Respuesta"]=="si":
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
        self.ui.label_24.setText(str(usdt_total))

        


    ###############################################################################


    ###############################################################################
    ################ Funciones de la pagina de login/singup #######################
    def login_logout(self):
        estado = self.ui.pushButton_6.text()

        if estado == "INICIAR SESION":
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui2.pushButton.clicked.connect(lambda: self.exchange())
            self.ui2.pushButton.clicked.connect(lambda: self.reinstaurarData())
            self.dialog.exec_()
            

    def cerrar(self):
        self.dialog.close()
    
    def reinstaurarData(self):
        self.idUser = ""
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

        self.ui.label_24.setText(self.usdt)
        self.ui.label_4.setText(self.usdt)
        self.ui.label_5.setText(self.tf_btc)
        self.ui.label_6.setText(self.mr_btc)
        self.ui.label_12.setText(self.mc_btc)
        self.ui.label_13.setText(self.tf_eth)
        self.ui.label_14.setText(self.mr_eth)
        self.ui.label_15.setText(self.mc_eth)
        self.ui.label_16.setText(self.tf_bnb)
        self.ui.label_17.setText(self.mr_bnb)
        self.ui.label_19.setText(self.mc_bnb)
        self.ui.label_20.setText(self.tf_usdc)
        self.ui.label_21.setText(self.mr_usdc)
        self.ui.label_22.setText(self.mc_usdc)
        datos = {}
        with open("jsonUser/id_user.json", "w") as archivo:
            json.dump(datos, archivo)
        self.ui.pushButton_6.setText("CERRAR SESIÓN")
        self.dialog.close()
        


        

    def login_singup(self, estado =""):
        if self.inicio == "Login" or estado =="Login":
            email = str(self.ui.lineEdit_3.text())
            password = str(self.ui.lineEdit_4.text())
            self.login_o_recordar(email,password)

        else:
            email = str(self.ui.lineEdit_3.text())
            password = str(self.ui.lineEdit_4.text())
            datos = self.datos.sing_up_api(email,password)
            self.idUser = datos
            self.ui.pushButton_6.setText("CERRAR SESIÓN")

            self.ui.label_24.setText("1000")
            self.ui.label_4.setText("1000")

        if self.ui.checkBox.isChecked():
            self.guardar_user(email,password)
            print("El checkbox está seleccionado")

        self.ui.stackedWidget.setCurrentIndex(0)

    def login_o_recordar(self,email,password):

        datos = self.datos.login_api(email,password)
        print(datos)

        self.idUser = datos["idUser"]
        dato_round = round(datos["USDT"],3)
        self.usdt =str(dato_round)
        dato_round = round(datos["TF-BTC"],3)
        self.tf_btc = str(dato_round)
        dato_round = round(datos["MR-BTC"],3)
        self.mr_btc = str(dato_round)
        dato_round = round(datos["MC-BTC"],3)
        self.mc_btc = str(dato_round)
        dato_round = round(datos["TF-ETH"],3)
        self.tf_eth = str(dato_round)
        dato_round = round(datos["MR-ETH"],3)
        self.mr_eth = str(dato_round)
        dato_round = round(datos["MC-ETH"],3)
        self.mc_eth = str(dato_round)
        dato_round = round(datos["TF-BNB"],3)
        self.tf_bnb = str(dato_round)
        dato_round = round(datos["MR-BNB"],3)
        self.mr_bnb = str(dato_round)
        dato_round = round(datos["MC-BNB"],3)
        self.mc_bnb = str(dato_round)
        dato_round = round(datos["TF-USDC"],3)
        self.tf_usdc = str(dato_round)
        dato_round = round(datos["MR-USDC"],3)
        self.mr_usdc = str(dato_round)
        dato_round = round(datos["MC-USDC"],3)
        self.mc_usdc = str(dato_round)

        self.ui.label_24.setText(self.usdt)
        self.ui.label_4.setText(self.usdt)
        self.ui.label_5.setText(self.tf_btc)
        self.ui.label_6.setText(self.mr_btc)
        self.ui.label_12.setText(self.mc_btc)
        self.ui.label_13.setText(self.tf_eth)
        self.ui.label_14.setText(self.mr_eth)
        self.ui.label_15.setText(self.mc_eth)
        self.ui.label_16.setText(self.tf_bnb)
        self.ui.label_17.setText(self.mr_bnb)
        self.ui.label_19.setText(self.mc_bnb)
        self.ui.label_20.setText(self.tf_usdc)
        self.ui.label_21.setText(self.mr_usdc)
        self.ui.label_22.setText(self.mc_usdc)

        self.ui.pushButton_6.setText("CERRAR SESIÓN")



    def guardar_user(self,email,password):
        datos = {email:password}
        with open("jsonUser/id_user.json", "w") as archivo:
            json.dump(datos, archivo)
        
             
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
                        numero =float(value_bot)
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
        self.ui.label_2.setText(str(round((total+usdt),3)))
    ###############################################################################    

#######################################################################################
def data_grafica ():
    asyncio.run(datos_graficas())





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    data_grafica_proces = multiprocessing.Process(target=data_grafica)
    data_grafica_proces.start()
    window.show()

    sys.exit(app.exec_())
