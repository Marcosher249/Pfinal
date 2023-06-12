from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QScrollArea, QApplication, QTableWidget, QTableWidgetItem,QLabel, QHBoxLayout, QSpacerItem, QSizePolicy,QPushButton,QDialog,QGridLayout
from PyQt5.QtGui import QFont, QMouseEvent
import pyqtgraph as pg
import sys
from PyQt5.QtCore import Qt, QTimer
import Grafica as p
import asyncio
import requests
import datetime
import matplotlib.dates as mdates
import numpy as np

class ClickableHBoxLayout(QWidget):
    def __init__(self, pair, color, bot, parent=None):
        super().__init__(parent)
        self.pair = pair
        self.color = color
        self.bot = bot

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.row_label = QLabel(self.bot)
        self.row_number = QLabel()
        self.row_label.setFont(QFont())
        self.row_number.setFont(QFont())
        self.row_label.setAlignment(Qt.AlignLeft)
        self.row_number.setAlignment(Qt.AlignRight)

        layout.addWidget(self.row_label)
        layout.addWidget(self.row_number)

        self.setMouseTracking(True)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.open_graph_window()

    def enterEvent(self, event: QMouseEvent) -> None:
        self.setStyleSheet("background-color: lightgray;")

    def leaveEvent(self, event: QMouseEvent) -> None:
        self.setStyleSheet("background-color: transparent;")

    def open_graph_window(self):
        dialog = QDialog()
        dialog.setWindowTitle("Graph Window")
        layout = QGridLayout(dialog)
        dialog.setLayout(layout)

        # Widget gráfico
        plot_widget = pg.PlotWidget()
        plot_widget.setMouseEnabled(x=False, y=False)  # Desactivar zoom
        plot_widget.setAutoVisible(y=False)

        layout.addWidget(plot_widget, 0, 0, 1, 2)

        # Obtener y actualizar los datos de la gráfica
        url = f"http://192.168.1.136:8000/bot_data/{self.bot}/{self.pair}"  # Nueva URL de la API
        response = requests.get(url)
        data = response.json()

        dates = [datetime.datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S') for item in data]
        bets = [item['bet'] for item in data]

        plot_widget.clear()
        x = np.array([mdates.date2num(date) for date in dates])
        y = np.array(bets)

        # Luego, puedes trazar el gráfico con los nuevos datos convertidos
        plot_widget.plot(x, y, pen=self.color)

        # Agregar botones
        buy_button = QPushButton("Comprar")
        sell_button = QPushButton("Vender")

        layout.addWidget(buy_button, 1, 0)
        layout.addWidget(sell_button, 1, 1)

        dialog.exec_()

class GraphWindow(QMainWindow):
    def __init__(self, pair, color, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Graph Window")
        try:
            url = f"http://192.168.1.136:8000/bot_data/{self.pair}"
            response = requests.get(url)
            data = response.json()
        except Exception as e:
            data = {"MovingAverageCrossoverBot":1, "MeanReversionBot":1, "TrendFollowingBot":1}

        # Widget gráfico
        plot_widget = pg.PlotWidget()
        plot_widget.setMouseEnabled(x=False, y=False)  # Desactivar zoom
        plot_widget.setAutoVisible(y=False) 

        # Ajustar espaciados
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 30)  # Espaciados izquierdo, superior, derecho, inferior
        layout.addWidget(plot_widget)
        layout.addSpacing(20)

        # Crear widget contenedor
        container_widget = QWidget()
        container_widget.setLayout(layout)

        # Agregar el widget contenedor al área desplazable
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(container_widget)
        self.setCentralWidget(scroll_area)

        # Obtener y actualizar los datos de la gráfica
        # Utiliza los métodos existentes en la clase MainWindow
        self.grafica = p.Grafica(pair)

        def update_plot():
            count = 0
            if not self.grafica.data_obtenida: 
                tabla = asyncio.run(self.grafica.tabla())
                plot_widget.clear()
                plot_widget.plot(tabla.index, tabla['Close'], pen=color)
                self.grafica.data_obtenida = True
                count = 1
            if count == 0:
                self.update_timer.stop()

        # Configurar actualización periódica
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(update_plot)
        self.update_timer.start(2000)  # Actualizar cada 5 segundos

        

        # Agregar las filas con nombres y números
        # Agregar las filas con nombres y números
        font = QFont()
        font.setPointSize(11)  # Tamaño de fuente más grande
        for key, value in data.items():
            row_layout = ClickableHBoxLayout(pair, color, key)
            row_layout.row_number.setText(str(value))
            row_layout.row_label.setFont(font)
            row_layout.row_number.setFont(font)
            row_layout.row_label.setAlignment(Qt.AlignLeft)
            row_layout.row_number.setAlignment(Qt.AlignRight)
            layout.addWidget(row_layout)
            layout.addSpacing(5)


# Ejemplo de uso
if __name__ == '__main__':
    app = QApplication(sys.argv)
    pair = 'BTC/USDT'  # Obtener el par deseado
    color = 'g'  # Obtener el color deseado
    graph_window = GraphWindow(pair, color)
    graph_window.show()
    sys.exit(app.exec_())
