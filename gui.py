# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 557)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 750, 136, 18))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 831, 361))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.zoomIn = QtWidgets.QPushButton(self.centralwidget)
        self.zoomIn.setGeometry(QtCore.QRect(780, 490, 75, 23))
        self.zoomIn.setObjectName("zoomIn")
        self.zoomOut = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOut.setGeometry(QtCore.QRect(690, 490, 75, 23))
        self.zoomOut.setObjectName("zoomOut")
        self.input_label = QtWidgets.QLabel(self.widget)
        self.input_label.setObjectName("input_label")
        self.verticalLayout_3.addWidget(self.input_label)

        styles = {'color':'b', 'font-size':'5px'}

        self.input_signal = pg.PlotWidget()
        self.input_signal.setBackground('w')
        self.input_signal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_signal.setLabel('left', 'Amplitude', **styles)
        self.input_signal.setLabel('bottom', 'time (sec)', **styles)
        self.input_signal.showGrid(x=True, y=True)
        self.input_signal.setXRange(0, 0.7)

        self.verticalLayout_3.addWidget(self.input_signal)
        self.output_label = QtWidgets.QLabel(self.widget)
        self.output_label.setObjectName("output_label")
        self.verticalLayout_3.addWidget(self.output_label)

        self.output_signal = pg.PlotWidget()
        self.output_signal.setBackground('w')
        self.output_signal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output_signal.setLabel('left', 'Amplitude', **styles)
        self.output_signal.setLabel('bottom', 'time (sec)', **styles)
        self.output_signal.showGrid(x=True, y=True)
        self.output_signal.setXRange(0, 0.7)

        self.verticalLayout_3.addWidget(self.output_signal)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        # Interpret image data as row-major instead of col-major
        pg.setConfigOptions(imageAxisOrder='row-major')

        pg.mkQApp()
        self.win = pg.GraphicsLayoutWidget()
        # A plot area (ViewBox + axes) for displaying the image
        self.SpectrogramPlotItem = self.win.addPlot()
        # Add labels to the axis
        self.SpectrogramPlotItem.setLabel('bottom', "Time", units='sec')
        # If you include the units, Pyqtgraph automatically scales the axis and adjusts the SI prefix (in this case kHz)
        # self.SpectrogramPlotItem.setLabel('left', "Frequency", units='Hz')

        # Item for displaying image data
        self.output_spectrogram = pg.ImageItem()
        self.SpectrogramPlotItem.addItem(self.output_spectrogram)
        # Add a histogram with which to control the gradient of the image
        self.hist = pg.HistogramLUTItem()
        # Link the histogram to the image
        self.hist.setImageItem(self.output_spectrogram)
        # If you don't add the histogram to the window, it stays invisible, but I find it useful.
        self.win.addItem(self.hist)
        # Show the window
        self.win.show()

        self.verticalLayout.addWidget(self.win)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(5, 130, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem)

        self.sliders = [QtWidgets.QSlider(self.widget) for i in range(10)]
        for slider in self.sliders:
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setSliderPosition(20)
            slider.setOrientation(QtCore.Qt.Vertical)
            self.horizontalLayout.addWidget(slider)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.max_slider = QtWidgets.QSlider(self.widget)
        self.max_slider.setOrientation(QtCore.Qt.Horizontal)
        self.max_slider.setObjectName("max_slider")
        self.max_slider.setMinimum(0)
        self.max_slider.setMaximum(1000)
        self.max_slider.setSliderPosition(1000)
        self.verticalLayout_4.addWidget(self.max_slider)
        self.pallet = QtWidgets.QSlider(self.widget)
        self.pallet.setOrientation(QtCore.Qt.Horizontal)
        self.pallet.setObjectName("pallet")
        self.pallet.setMinimum(0)
        self.pallet.setMaximum(4)
        self.pallet.setSliderPosition(0)
        self.verticalLayout_4.addWidget(self.pallet)
        self.min_slider = QtWidgets.QSlider(self.widget)
        self.min_slider.setOrientation(QtCore.Qt.Horizontal)
        self.min_slider.setObjectName("min_slider")
        self.min_slider.setMinimum(0)
        self.min_slider.setMaximum(1000)
        self.min_slider.setSliderPosition(0)
        self.verticalLayout_4.addWidget(self.min_slider)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.scroll = QtWidgets.QSlider(self.widget)
        self.scroll.setOrientation(QtCore.Qt.Horizontal)
        self.scroll.setObjectName("scroll")
        self.min_slider.setMinimum(0)
        self.min_slider.setMaximum(100)
        self.min_slider.setSliderPosition(0)
        self.verticalLayout_5.addWidget(self.scroll)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        MainWindow.setMenuBar(self.menubar)
        self.open = QtWidgets.QAction(MainWindow)
        self.open.setObjectName("open")
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.file.addAction(self.open)
        self.file.addAction(self.save)
        self.menubar.addAction(self.file.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_label.setText(_translate("MainWindow", "Input signal"))
        self.output_label.setText(_translate("MainWindow", "Output signal"))
        self.label_2.setText(_translate("MainWindow", "output spectrogram"))
        self.file.setTitle(_translate("MainWindow", "file"))
        self.open.setText(_translate("MainWindow", "open"))
        self.save.setText(_translate("MainWindow", "save"))
        self.zoomIn.setText(_translate("MainWindow", "zoom in"))
        self.zoomOut.setText(_translate("MainWindow", "zoom out"))