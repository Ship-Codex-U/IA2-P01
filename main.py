import sys
import os
import re
import numpy as np
import random

from module import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.rangeMin = -5
        self.rangeMax = 5

        self.points = []


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.figure = Figure()
        self.figure.subplots_adjust(left=0.07, right=0.95, bottom=0.07, top=0.95)
        self.canvas = FigureCanvas(self.figure)

        self.ax = self.figure.add_subplot(111)

        self.ui.layout_graphic.addWidget(self.canvas)
        self.ui.button_generate_points.clicked.connect(self.click_point_generate)
        self.ui.button_insert_points.clicked.connect(self.click_insert_point)
        self.canvas.mpl_connect("button_press_event", self.click_insert_point_mouse)
        self.ui.slider_weight_01.valueChanged.connect(self.change_slider_weight_01)
        self.ui.slider_weight_02.valueChanged.connect(self.change_slider_weight_02)
        self.ui.slider_bias.valueChanged.connect(self.change_slider_bias)

        self.init_plot()
        self.init_sliders()
        self.show()

    @Slot()
    def click_point_generate(self):
        quantity = int(self.ui.input_quantity.toPlainText())

        self.points.clear()
        self.points = self.point_generate(quantity, self.rangeMin, self.rangeMax)
        self.update_plot()

    @Slot()
    def click_insert_point(self):
        x = int(self.ui.input_coord_x.toPlainText())
        y = int(self.ui.input_coord_y.toPlainText())

        self.ui.input_coord_x.setText("")
        self.ui.input_coord_y.setText("")

        self.points.append((x, y))

        self.update_plot()

    def click_insert_point_mouse(self, event):
        if event.xdata is not None and event.ydata is not None:
            coord = (event.xdata, event.ydata)
            self.points.append(coord)

            self.update_plot()
    
    @Slot()
    def change_slider_weight_01(self, value):
        decimal_value = value / 10.0
        self.ui.label_weight_01.setText(str(decimal_value))

    @Slot()
    def change_slider_weight_02(self, value):
        decimal_value = value / 10.0
        self.ui.label_weight_02.setText(str(decimal_value))

    @Slot()
    def change_slider_bias(self, value):
        decimal_value = value / 10.0
        self.ui.label_bias.setText(str(decimal_value))

    def point_generate(self, quantity, lower_limit, upper_limit):
        x = np.random.randint(lower_limit, upper_limit + 1, size = quantity)
        y = np.random.randint(lower_limit, upper_limit + 1, size = quantity)

        return list(zip(x, y))

    def init_plot(self):
        self.ax.set_xlim(self.rangeMin, self.rangeMax)
        self.ax.set_ylim(self.rangeMin, self.rangeMax)
        self.ax.set_aspect('equal')

        self.ax.spines["left"].set_position("zero")
        self.ax.spines["bottom"].set_position("zero")
        self.ax.spines["right"].set_color("none")
        self.ax.spines["top"].set_color("none")

        self.ax.grid(True, linestyle="--", linewidth=0.5)

        self.ax.set_xticks(np.arange(self.rangeMin, self.rangeMax + 1, 1))
        self.ax.set_yticks(np.arange(self.rangeMin, self.rangeMax + 1, 1))
    
    def update_plot(self):
        self.ax.clear()
        self.init_plot()

        if self.points:
            x_data, y_data = zip(*self.points)
            self.ax.plot(x_data, y_data, 'o', color='black', markersize=4)  

        # for point in self.points:
        #     self.ax.scatter(point[0], point[1], marker="o", color="r", s=50)

        self.canvas.draw_idle()

    def init_sliders(self):
        rangeMin = -5
        rangeMax = 5

        self.ui.slider_weight_01.setRange(rangeMin * 10, rangeMax * 10)
        self.ui.slider_weight_01.setValue(0)

        self.ui.slider_weight_02.setRange(rangeMin * 10, rangeMax * 10)
        self.ui.slider_weight_02.setValue(0)

        self.ui.slider_bias.setRange(rangeMin * 10, rangeMax * 10)
        self.ui.slider_bias.setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
