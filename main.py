import sys
import os
import re
import numpy as np
import random

from module import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.rangeMinGraphic = -8
        self.rangeMaxGraphic = 8
        self.rangeMinSlider = -25
        self.rangeMaxSlider = 25

        self.zoom_factor = 1.2

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
        self.ui.button_clean.clicked.connect(self.click_clean)
        self.canvas.mpl_connect("button_press_event", self.click_insert_point_mouse)
        self.ui.slider_weight_01.valueChanged.connect(self.change_slider_value)
        self.ui.slider_weight_02.valueChanged.connect(self.change_slider_value)
        self.ui.slider_bias.valueChanged.connect(self.change_slider_value)

        self.canvas.mpl_connect("scroll_event", self.on_scroll)

        self.init_plot()
        self.init_sliders()
        self.show()
    
    def on_scroll(self, event):
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        x_center = (xlim[0] + xlim[1]) / 2
        y_center = (ylim[0] + ylim[1]) / 2

        if event.step > 0:  # Zoom in
            scale_factor = 1 / self.zoom_factor
        else:  # Zoom out
            scale_factor = self.zoom_factor

        new_xlim = [(x - x_center) * scale_factor + x_center for x in xlim]
        new_ylim = [(y - y_center) * scale_factor + y_center for y in ylim]

        self.ax.set_xlim(new_xlim)
        self.ax.set_ylim(new_ylim)
        self.canvas.draw()

    @Slot()
    def click_point_generate(self):
        quantity = int(self.ui.input_quantity.toPlainText())

        self.points.clear()
        self.points = self.point_generate(quantity, self.rangeMinGraphic, self.rangeMaxGraphic)
        self.update_plot()

    @Slot()
    def click_insert_point(self):
        x = int(self.ui.input_coord_x.toPlainText())
        y = int(self.ui.input_coord_y.toPlainText())

        self.ui.input_coord_x.setText("")
        self.ui.input_coord_y.setText("")

        self.points.append((x, y))

        self.update_plot()

    @Slot()
    def click_clean(self):
        self.points.clear()

        self.init_sliders()
        self.init_inputs()
        self.init_labels()
        self.update_plot()


    def click_insert_point_mouse(self, event):
        if event.xdata is not None and event.ydata is not None:
            coord = (event.xdata, event.ydata)
            self.points.append(coord)

            weight_01 = self.ui.slider_weight_01.value() / 10.0
            weight_02 = self.ui.slider_weight_02.value() / 10.0
            bias = self.ui.slider_bias.value() / 10.0

            perceptron = Perceptron(weight_01, weight_02, bias)

            self.ax.plot(coord[0], coord[1], 'o', color='blue', markersize=4)
            self.ax.annotate(f'({perceptron.predict(coord[0], coord[1])})', (coord[0], coord[1]), textcoords="offset points", xytext=(0,5), ha='center')
            self.canvas.draw_idle()

            #self.update_plot()
    
    @Slot()
    def change_slider_value(self, value):
        weight_01 = self.ui.slider_weight_01.value() / 10.0
        weight_02 = self.ui.slider_weight_02.value() / 10.0
        bias = self.ui.slider_bias.value() / 10.0

        self.ui.label_weight_01.setText(str(weight_01))
        self.ui.label_weight_02.setText(str(weight_02))
        self.ui.label_bias.setText(str(bias))

        perceptron = Perceptron(weight_01, weight_02, bias)

        result = perceptron.get_MB_equation_line()

        if result is not None:
            m, b = result

            self.draw_equation_line(self.rangeMinGraphic, self.rangeMaxGraphic, m, b)


    def point_generate(self, quantity, lower_limit, upper_limit):
        x = np.random.randint(lower_limit, upper_limit + 1, size = quantity)
        y = np.random.randint(lower_limit, upper_limit + 1, size = quantity)

        return list(zip(x, y))

    def init_plot(self):
        self.ax.set_xlim(self.rangeMinGraphic, self.rangeMaxGraphic)
        self.ax.set_ylim(self.rangeMinGraphic, self.rangeMaxGraphic)
        self.ax.set_aspect('equal')

        self.ax.spines["left"].set_position("zero")
        self.ax.spines["bottom"].set_position("zero")
        self.ax.spines["right"].set_color("none")
        self.ax.spines["top"].set_color("none")

        self.ax.grid(True, linestyle="--", linewidth=0.5)

        self.ax.set_xticks(np.arange(self.rangeMinGraphic, self.rangeMaxGraphic + 1, 1))
        self.ax.set_yticks(np.arange(self.rangeMinGraphic, self.rangeMaxGraphic + 1, 1))
    
    def update_plot(self):
        weight_01 = self.ui.slider_weight_01.value() / 10.0
        weight_02 = self.ui.slider_weight_02.value() / 10.0
        bias = self.ui.slider_bias.value() / 10.0

        perceptron = Perceptron(weight_01, weight_02, bias)

        self.ax.clear()
        self.init_plot()

        if self.points:
            x_data, y_data = zip(*self.points)
            self.ax.plot(x_data, y_data, 'o', color='blue', markersize=4)  

            for i, (x, y) in enumerate(zip(x_data, y_data)):
                self.ax.annotate(f'({perceptron.predict(x, y)})', (x, y), textcoords="offset points", xytext=(0,5), ha='center')

        # for point in self.points:
        #     self.ax.scatter(point[0], point[1], marker="o", color="r", s=50)

        self.canvas.draw_idle()

    def init_sliders(self):
        self.ui.slider_weight_01.setRange(self.rangeMinSlider * 10, self.rangeMaxSlider * 10)
        self.ui.slider_weight_01.setValue(0)

        self.ui.slider_weight_02.setRange(self.rangeMinSlider * 10, self.rangeMaxSlider * 10)
        self.ui.slider_weight_02.setValue(0)

        self.ui.slider_bias.setRange(self.rangeMinSlider * 10, self.rangeMaxSlider * 10)
        self.ui.slider_bias.setValue(0)
    
    def init_labels(self):
        self.ui.label_weight_01.setText("0")
        self.ui.label_weight_02.setText("0")
        self.ui.label_bias.setText("0")
    
    def init_inputs(self):
        self.ui.input_coord_x.setText("")
        self.ui.input_coord_y.setText("")
        self.ui.input_quantity.setText("")

    def draw_equation_line(self, x_min, x_max, m, b):
        x = np.linspace(x_min, x_max + 1, 1000)
        y = m * x + b

        self.update_plot()
        self.ax.plot(x, y, color='red', label=f'y = {m:.2f}x + {b:.2f} ')
        self.ax.legend()
        self.canvas.draw_idle()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
