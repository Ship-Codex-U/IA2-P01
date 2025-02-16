import sys
import os
import re

from module import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()

    def dataGrafic(self):
        plt

    
    # def paintEvent(self, event):
    #     """ Dibuja los ejes y los puntos en el plano cartesiano """
    #     painter = QPainter(self)
    #     painter.setRenderHint(QPainter.Antialiasing)

    #     # Dibujar ejes
    #     width = self.width()
    #     height = self.height()
    #     center_x = width // 2
    #     center_y = height // 2

    #     pen = QPen(Qt.black, 2)
    #     painter.setPen(pen)
    #     painter.drawLine(0, center_y, width, center_y)  # Eje X
    #     painter.drawLine(center_x, 0, center_x, height)  # Eje Y

    
    # def mousePressEvent(self, event: QMouseEvent):
    #     """ Captura la posición del clic y la almacena """
    #     if event.button() == Qt.LeftButton:

    #         # Objeto de tipo QPoint
    #         print(f"({event.position().toPoint()})")
    #         self.update()

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         widget_width = self.width()
    #         widget_height = self.height()

    #         # Centro del widget es el (0,0) en el sistema cartesiano
    #         center_x = widget_width // 2
    #         center_y = widget_height // 2

    #         # Obtener coordenadas del clic
    #         click_x = event.position().toPoint().x()
    #         click_y = event.position().toPoint().y()

    #         # Convertir a coordenadas cartesianas
    #         cart_x = click_x - center_x
    #         cart_y = -(click_y - center_y)  # Invertimos Y porque en Qt Y crece hacia abajo

    #         print(f"Coordenada en el sistema cartesiano: ({cart_x}, {cart_y})")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
