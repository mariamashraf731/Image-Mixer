# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.image1_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.image1_combobox.setObjectName("image1_combobox")
        self.image1_combobox.addItem("")
        self.image1_combobox.addItem("")
        self.image1_combobox.addItem("")
        self.image1_combobox.addItem("")
        self.image1_combobox.addItem("")
        self.gridLayout_2.addWidget(self.image1_combobox, 0, 1, 1, 1)
        self.Original_image1 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Original_image1.sizePolicy().hasHeightForWidth())
        self.Original_image1.setSizePolicy(sizePolicy)
        self.Original_image1.setMinimumSize(QtCore.QSize(0, 0))
        self.Original_image1.setStyleSheet("")
        self.Original_image1.setObjectName("Original_image1")
        self.gridLayout_2.addWidget(self.Original_image1, 1, 0, 1, 1)
        self.Modified_image1 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Modified_image1.sizePolicy().hasHeightForWidth())
        self.Modified_image1.setSizePolicy(sizePolicy)
        self.Modified_image1.setMinimumSize(QtCore.QSize(0, 0))
        self.Modified_image1.setStyleSheet("")
        self.Modified_image1.setObjectName("Modified_image1")
        self.gridLayout_2.addWidget(self.Modified_image1, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Component2_slider = QtWidgets.QSlider(self.centralwidget)
        self.Component2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Component2_slider.setMinimum(0)
        self.Component2_slider.setMaximum(100)
        self.Component2_slider.setValue(0)
        self.Component2_slider.setSingleStep(10)
        self.Component2_slider.setObjectName("Component2_slider")
        self.gridLayout.addWidget(self.Component2_slider, 3, 3, 1, 1)
        self.choose_image1 = QtWidgets.QComboBox(self.centralwidget)
        self.choose_image1.setObjectName("choose_image1")
        self.choose_image1.addItem("")
        self.choose_image1.addItem("")
        self.choose_image1.addItem("")
        self.gridLayout.addWidget(self.choose_image1, 1, 1, 1, 1)
        self.choose_image2 = QtWidgets.QComboBox(self.centralwidget)
        self.choose_image2.setObjectName("choose_image2")
        self.choose_image2.addItem("")
        self.choose_image2.addItem("")
        self.choose_image2.addItem("")
        self.gridLayout.addWidget(self.choose_image2, 3, 1, 1, 1)
        self.Component1_slider = QtWidgets.QSlider(self.centralwidget)
        self.Component1_slider.setMinimum(0)
        self.Component1_slider.setMaximum(100)
        self.Component1_slider.setValue(100)
        self.Component1_slider.setSingleStep(10)
        self.Component1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Component1_slider.setObjectName("Component1_slider")
        self.gridLayout.addWidget(self.Component1_slider, 1, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 4, 1, 1)
        self.Component1_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.Component1_combobox.setObjectName("Component1_combobox")
        self.Component1_combobox.addItem("")
        self.Component1_combobox.addItem("")
        self.Component1_combobox.addItem("")
        self.Component1_combobox.addItem("")
        self.Component1_combobox.addItem("")
        self.Component1_combobox.addItem("")
        self.Component1_combobox.addItem("")
        self.gridLayout.addWidget(self.Component1_combobox, 2, 1, 1, 4)
        self.output_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.output_combobox.setObjectName("output_combobox")
        self.output_combobox.addItem("")
        self.output_combobox.addItem("")
        self.output_combobox.addItem("")
        self.gridLayout.addWidget(self.output_combobox, 0, 1, 1, 4)
        self.Component2_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.Component2_combobox.setObjectName("Component2_combobox")
        self.Component2_combobox.addItem("")
        self.gridLayout.addWidget(self.Component2_combobox, 4, 1, 1, 4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.image2_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.image2_combobox.setObjectName("image2_combobox")
        self.image2_combobox.addItem("")
        self.image2_combobox.addItem("")
        self.image2_combobox.addItem("")
        self.image2_combobox.addItem("")
        self.image2_combobox.addItem("")
        self.gridLayout_4.addWidget(self.image2_combobox, 0, 1, 1, 1)
        self.Original_image2 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Original_image2.sizePolicy().hasHeightForWidth())
        self.Original_image2.setSizePolicy(sizePolicy)
        self.Original_image2.setMinimumSize(QtCore.QSize(0, 0))
        self.Original_image2.setStyleSheet("")
        self.Original_image2.setObjectName("Original_image2")
        self.gridLayout_4.addWidget(self.Original_image2, 1, 0, 1, 1)
        self.Modified_image2 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Modified_image2.sizePolicy().hasHeightForWidth())
        self.Modified_image2.setSizePolicy(sizePolicy)
        self.Modified_image2.setMinimumSize(QtCore.QSize(0, 0))
        self.Modified_image2.setStyleSheet("")
        self.Modified_image2.setObjectName("Modified_image2")
        self.gridLayout_4.addWidget(self.Modified_image2, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(13)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.Output_image1 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Output_image1.sizePolicy().hasHeightForWidth())
        self.Output_image1.setSizePolicy(sizePolicy)
        self.Output_image1.setMinimumSize(QtCore.QSize(0, 0))
        self.Output_image1.setStyleSheet("")
        self.Output_image1.setObjectName("Output_image1")
        self.gridLayout_3.addWidget(self.Output_image1, 1, 0, 1, 1)
        self.Output_image2 = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Output_image2.sizePolicy().hasHeightForWidth())
        self.Output_image2.setSizePolicy(sizePolicy)
        self.Output_image2.setMinimumSize(QtCore.QSize(0, 0))
        self.Output_image2.setStyleSheet("")
        self.Output_image2.setObjectName("Output_image2")
        self.gridLayout_3.addWidget(self.Output_image2, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_File = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_File.setObjectName("menuOpen_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImage_1 = QtWidgets.QAction(MainWindow)
        self.actionImage_1.setObjectName("actionImage_1")
        self.actionImage_2 = QtWidgets.QAction(MainWindow)
        self.actionImage_2.setObjectName("actionImage_2")
        self.menuOpen_File.addAction(self.actionImage_1)
        self.menuOpen_File.addAction(self.actionImage_2)
        self.menuFile.addAction(self.menuOpen_File.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.img_labels=[self.Original_image1,self.Original_image2,self.Modified_image1,self.Modified_image2,self.Output_image1,self.Output_image2]
        for i in range(6):
            self.img_labels[i].ui.histogram.hide()
            self.img_labels[i].ui.roiBtn.hide()
            self.img_labels[i].ui.menuBtn.hide()
            self.img_labels[i].ui.roiPlot.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Image 1"))
        self.image1_combobox.setItemText(0, _translate("MainWindow", "Select Component"))
        self.image1_combobox.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.image1_combobox.setItemText(2, _translate("MainWindow", "Phase"))
        self.image1_combobox.setItemText(3, _translate("MainWindow", "Real"))
        self.image1_combobox.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.choose_image1.setItemText(0, _translate("MainWindow", "Select Image"))
        self.choose_image1.setItemText(1, _translate("MainWindow", "Image 1"))
        self.choose_image1.setItemText(2, _translate("MainWindow", "Image 2"))
        self.choose_image2.setItemText(0, _translate("MainWindow", "Select Image"))
        self.choose_image2.setItemText(1, _translate("MainWindow", "Image 1"))
        self.choose_image2.setItemText(2, _translate("MainWindow", "Image 2"))
        self.label_4.setText(_translate("MainWindow", "Mixer Output To"))
        self.label_15.setText(_translate("MainWindow", "%"))
        self.label_16.setText(_translate("MainWindow", "%"))
        self.Component1_combobox.setItemText(0, _translate("MainWindow", "Select Component"))
        self.Component1_combobox.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.Component1_combobox.setItemText(2, _translate("MainWindow", "Phase"))
        self.Component1_combobox.setItemText(3, _translate("MainWindow", "Real"))
        self.Component1_combobox.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.Component1_combobox.setItemText(5, _translate("MainWindow", "Uni Magnitude"))
        self.Component1_combobox.setItemText(6, _translate("MainWindow", "Uni Phase"))
        self.output_combobox.setItemText(0, _translate("MainWindow", "Select Output"))
        self.output_combobox.setItemText(1, _translate("MainWindow", "Output 1"))
        self.output_combobox.setItemText(2, _translate("MainWindow", "Output 2"))
        self.Component2_combobox.setItemText(0, _translate("MainWindow", "Select Component"))
        self.label_6.setText(_translate("MainWindow", "Component 2       "))
        self.label_14.setText(_translate("MainWindow", "Component 1      "))
        self.label_7.setText(_translate("MainWindow", "Image 2"))
        self.image2_combobox.setItemText(0, _translate("MainWindow", "Select Component"))
        self.image2_combobox.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.image2_combobox.setItemText(2, _translate("MainWindow", "Phase"))
        self.image2_combobox.setItemText(3, _translate("MainWindow", "Real"))
        self.image2_combobox.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.label_13.setText(_translate("MainWindow", "Output 1"))
        self.label_11.setText(_translate("MainWindow", "Output 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_File.setTitle(_translate("MainWindow", "Open"))
        self.actionImage_1.setText(_translate("MainWindow", "Image 1"))
        self.actionImage_2.setText(_translate("MainWindow", "Image 2"))

from pyqtgraph import ImageView

