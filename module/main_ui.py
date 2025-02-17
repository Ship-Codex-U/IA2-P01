# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(890, 518)
        MainWindow.setStyleSheet(u"QTextEdit {\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #45a049;\n"
"border-radius: 7px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, -1, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 200))
        self.frame.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(31, 31, 31);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.layout_graphic = QVBoxLayout()
        self.layout_graphic.setObjectName(u"layout_graphic")

        self.horizontalLayout_5.addLayout(self.layout_graphic)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(10, 134, 169);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_10.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_7.addWidget(self.label_11)

        self.input_coord_x = QTextEdit(self.frame_2)
        self.input_coord_x.setObjectName(u"input_coord_x")
        self.input_coord_x.setMaximumSize(QSize(16777215, 25))
        self.input_coord_x.setStyleSheet(u"				background-color: rgb(236, 243, 244);")
        self.input_coord_x.setTabChangesFocus(True)

        self.verticalLayout_7.addWidget(self.input_coord_x)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_8.addWidget(self.label_12)

        self.input_coord_y = QTextEdit(self.frame_2)
        self.input_coord_y.setObjectName(u"input_coord_y")
        self.input_coord_y.setMaximumSize(QSize(16777215, 25))
        self.input_coord_y.setStyleSheet(u"background-color: rgb(236, 243, 244);")
        self.input_coord_y.setTabChangesFocus(True)

        self.verticalLayout_8.addWidget(self.input_coord_y)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_9.addWidget(self.label_13)

        self.input_quantity = QTextEdit(self.frame_2)
        self.input_quantity.setObjectName(u"input_quantity")
        self.input_quantity.setMaximumSize(QSize(16777215, 25))
        self.input_quantity.setStyleSheet(u"background-color: rgb(236, 243, 244);")
        self.input_quantity.setTabChangesFocus(True)

        self.verticalLayout_9.addWidget(self.input_quantity)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.button_insert_points = QPushButton(self.frame_2)
        self.button_insert_points.setObjectName(u"button_insert_points")
        self.button_insert_points.setMinimumSize(QSize(0, 40))
        self.button_insert_points.setMaximumSize(QSize(16777215, 16777215))
        self.button_insert_points.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.button_insert_points.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.verticalLayout_4.addWidget(self.button_insert_points)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.button_clean = QPushButton(self.frame_2)
        self.button_clean.setObjectName(u"button_clean")
        self.button_clean.setMinimumSize(QSize(0, 40))
        self.button_clean.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.verticalLayout_5.addWidget(self.button_clean)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.button_generate_points = QPushButton(self.frame_2)
        self.button_generate_points.setObjectName(u"button_generate_points")
        self.button_generate_points.setMinimumSize(QSize(0, 40))
        self.button_generate_points.setStyleSheet(u"background-color: rgb(0, 87, 111);")

        self.verticalLayout_14.addWidget(self.button_generate_points)


        self.horizontalLayout_3.addLayout(self.verticalLayout_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.v3 = QVBoxLayout()
        self.v3.setSpacing(12)
        self.v3.setObjectName(u"v3")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.v3.addWidget(self.label_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.slider_weight_01 = QSlider(self.frame_2)
        self.slider_weight_01.setObjectName(u"slider_weight_01")
        self.slider_weight_01.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_6.addWidget(self.slider_weight_01)

        self.label_weight_01 = QLabel(self.frame_2)
        self.label_weight_01.setObjectName(u"label_weight_01")
        self.label_weight_01.setFont(font1)
        self.label_weight_01.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_weight_01)


        self.v3.addLayout(self.verticalLayout_6)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_10.addWidget(self.label_3)

        self.slider_weight_02 = QSlider(self.frame_2)
        self.slider_weight_02.setObjectName(u"slider_weight_02")
        self.slider_weight_02.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_10.addWidget(self.slider_weight_02)

        self.label_weight_02 = QLabel(self.frame_2)
        self.label_weight_02.setObjectName(u"label_weight_02")
        self.label_weight_02.setFont(font1)
        self.label_weight_02.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_weight_02)


        self.v3.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4)

        self.slider_bias = QSlider(self.frame_2)
        self.slider_bias.setObjectName(u"slider_bias")
        self.slider_bias.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_11.addWidget(self.slider_bias)

        self.label_bias = QLabel(self.frame_2)
        self.label_bias.setObjectName(u"label_bias")
        self.label_bias.setFont(font1)
        self.label_bias.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_bias)


        self.v3.addLayout(self.verticalLayout_11)


        self.verticalLayout_3.addLayout(self.v3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Perceptr\u00f3n", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Insertar puntos.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Coordenada X", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Coordenada Y", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.button_insert_points.setText(QCoreApplication.translate("MainWindow", u"Insertar", None))
        self.button_clean.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.button_generate_points.setText(QCoreApplication.translate("MainWindow", u"Generar \n"
"Aleatoriamente", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Modificaci\u00f3n de los parametros.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Peso 01", None))
        self.label_weight_01.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Peso 02", None))
        self.label_weight_02.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bias", None))
        self.label_bias.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

