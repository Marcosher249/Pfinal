import sys
from PySide2.QtCore import Qt, QDateTime, QTimer
from PySide2.QtGui import QPainter, QColor, QBrush
from PySide2.QtCharts import QtCharts
from PySide2.QtWidgets import QMainWindow, QApplication, QFrame, QVBoxLayout
import pandas as pd
import sys
import ccxt as c
import pandas as pd
import asyncio
import json
import multiprocessing




async def tabla(moneda):
    datos = await dataframe(moneda)
    tabla = pd.DataFrame(datos, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    tabla['Date'] = pd.to_datetime(tabla['Date'], unit='ms')
    tabla = tabla.set_index('Date')
    tabla.index = tabla.index.tz_localize('UTC').tz_convert('Europe/Madrid')
    tabla.index = tabla.index.strftime('%Y-%m-%d %H:%M:%S')
    print(tabla)
    if moneda == "BTC/USDT":
        tabla.to_csv('csv/datos_btc.csv')
    elif moneda == "ETH/USDT":
        tabla.to_csv('csv/datos_eth.csv')
    elif moneda == "BNB/USDT":
        tabla.to_csv('csv/datos_bnb.csv')
    else:
        tabla.to_csv('csv/datos_usdc.csv')

    

async def dataframe(moneda):
        
    try:
        kuco = c.kucoin()
        datos = kuco.fetch_ohlcv(moneda, timeframe='1m', limit=5)
        return datos
    except Exception as e:
        print(f'error en kucoin' + str(e))
    try:
        binan = c.binance()
        datos = binan.fetch_ohlcv(moneda, timeframe='1m', limit=5)
        return datos
    except Exception as e:       
        print('error en binance' + str(e))
    try:
        coin = c.coinbase()
        datos = coin.fetch_ohlcv(moneda, timeframe='1m', limit=5)
        return datos
    except Exception as e:
        print('error en coinbase' + str(e))
    try:
        coin = c.ace()
        datos = coin.fetch_ohlcv(moneda, timeframe='1m', limit=5)
        return datos
    except Exception as e:
        print('error en ace' + str(e))
    try:
        coin = c.alpaca()
        datos = coin.fetch_ohlcv(moneda, timeframe='1m', limit=5)
        return datos
    except Exception as e:
        print('error en alpaca' + str(e))
    try:
        coin = c.ascendex()
        datos = coin.fetch_ohlcv(moneda, timeframe='1m', limit=5)
        return datos
    except Exception as e:
        print('error en ascendex' + str(e))
        return datos
async def datos_graficas():
    while True:
        monedas = ["BNB/USDT"]
        tasks = [tabla(moneda) for moneda in monedas]
        await asyncio.gather(*tasks)
        print("se graban nuevos datos")
        await asyncio.sleep(30)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear los marcos para las gráficas
        self.frame_23 = QFrame()


        # Crear los diseños verticales para los marcos


        # Cargar los datos y crear las gráficas
        self.listcsv = {'csv/datos_bnb.csv': 'frame_23'}
        self.series = {}  # Diccionario para almacenar las series de datos
        for csv, frame in self.listcsv.items():
            self.series[frame] = self.create_chart_series(csv)
            self.create_chart(frame)

        # Configurar los marcos como widgets centrales de la ventana principal
        self.setCentralWidget(self.frame_23)

        # Configurar el tamaño de la ventana
        self.resize(800, 600)
        self.setWindowTitle("Gráficas de datos")

        # Crear el temporizador para actualizar las gráficas cada 30 segundos
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_charts)
        self.timer.start(3000)  # 30 segundos en milisegundos

        # Mostrar la ventana principal
        self.show()

    def create_chart_series(self, csv_file):
        df = pd.read_csv(csv_file)
        series = QtCharts.QLineSeries()

        for index, row in df.iterrows():
            date_str = row['Date']
            close = row['Close']
            date_time = QDateTime.fromString(date_str, "yyyy-MM-dd hh:mm:ss")
            series.append(date_time.toSecsSinceEpoch(), close)

        return series

    def create_chart(self, frame):
        q_frame = getattr(self, frame)

        chart = QtCharts.QChart()
        chart.addSeries(self.series[frame])
        chart.createDefaultAxes()

        axis_x = QtCharts.QDateTimeAxis()
        axis_x.setLabelsVisible(False)
        chart.setAxisX(axis_x, self.series[frame])

        background_color = QColor(148, 148, 148, 175)
        chart.setBackgroundBrush(QBrush(background_color))
        chart_view = QtCharts.QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing, True)
        layout = QVBoxLayout(q_frame)
        layout.addWidget(chart_view)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

    def update_charts(self):
        for csv_file, frame in self.listcsv.items():
            series = self.series[frame]  # Obtener la serie existente
            new_series = self.create_chart_series(csv_file)  # Crear una nueva serie con los datos actualizados

            # Limpiar la serie existente y agregar los nuevos puntos de datos
            series.clear()
            for i in range(new_series.count()):
                point = new_series.at(i)
                series.append(point)

            # Actualizar la vista del gráfico
            chart_view = getattr(self, frame).layout().itemAt(0).widget()
            chart_view.chart().axisX().setRange(series.at(0).x(), series.at(series.count() - 1).x())

def run_bot_manager ():
    asyncio.run(datos_graficas())


if __name__ == "__main__":
        # Crear un proceso para ejecutar el BotManager
    bot_manager_process = multiprocessing.Process(target=run_bot_manager)
    bot_manager_process.start()
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
