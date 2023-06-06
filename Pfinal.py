import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QScrollArea, QToolBar, QSizePolicy
from PyQt5.QtGui import QFont, QPainter, QColor, QPainterPath
from PyQt5.QtCore import Qt, QTimer
import ccxt as c
import pandas as pd
import pyqtgraph as pg
import asyncio
import Grafica as p
from individual import GraphWindow

class CircleButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(40, 40)
        self.setStyleSheet("QPushButton { color: white; background-color: black; border: none; }")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addEllipse(0, 0, self.width(), self.height())
        painter.fillPath(path, self.palette().button())

        painter.setPen(self.palette().dark().color())
        painter.drawText(event.rect(), Qt.AlignCenter, self.text())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TeadignBot")
        self.setGeometry(100, 100, 900, 500)

        scroll_area = QScrollArea()
        self.setCentralWidget(scroll_area)

        content_widget = QWidget()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(content_widget)

        layout = QVBoxLayout(content_widget)

        toolbar = QToolBar()
        toolbar.setStyleSheet("QToolBar { background-color: white; }")
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toolbar.addWidget(spacer)

        button = CircleButton('Salir')
        button.clicked.connect(self.close)
        toolbar.addWidget(button)

        pairs = self.load_pairs_from_json("pares.json")
        self.graficas = []
        self.create_all_widgets(layout, pairs)

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_all_plots)
        self.update_timer.start(2000)  # Actualizar cada 5 segundos

    def load_pairs_from_json(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
        return list(data.items())

    def create_all_widgets(self, layout, pairs):
        for pair, color in pairs:
            grafica = p.Grafica(pair)
            self.graficas.append(grafica)

            label = QLabel("Gráfica de " + pair)
            label.setFont(QFont("Arial", 14))
            layout.addWidget(label)

            plot_widget = pg.PlotWidget()
            plot_widget.setBackground('k')
            plot_widget.setMouseEnabled(x=False, y=False)  # Desactivar zoom
            plot_widget.setAutoVisible(y=False) 
            layout.addWidget(plot_widget)

            plot_widget.scene().sigMouseClicked.connect(lambda _, p=pair, c=color: self.open_graph_window(p, c))

    def update_all_plots(self):
        count = 0
        for grafica, plot_widget in zip(self.graficas, self.findChildren(pg.PlotWidget)):
            if not grafica.data_obtenida:  # Verifica si se ha obtenido el DataFrame
                tabla = asyncio.run(grafica.tabla())
                grafica.data_obtenida = True  # Marca la grafica como actualizada
                plot_widget.clear()
                plot_widget.plot(tabla.index, tabla['Close'], pen="g")
                count += 1
        if count == 0:
            self.update_timer.stop()

    def open_graph_window(self, pair, color):
        graph_window = GraphWindow(pair, color, self)
        graph_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
