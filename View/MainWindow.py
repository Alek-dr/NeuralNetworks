# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(958, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(618, -1, 161, 551))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Learn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Learn.setObjectName(_fromUtf8("Learn"))
        self.verticalLayout_3.addWidget(self.Learn)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.polar = QtGui.QRadioButton(self.groupBox)
        self.polar.setGeometry(QtCore.QRect(10, 0, 110, 21))
        self.polar.setChecked(True)
        self.polar.setObjectName(_fromUtf8("polar"))
        self.biPolar = QtGui.QRadioButton(self.groupBox)
        self.biPolar.setGeometry(QtCore.QRect(10, 30, 109, 21))
        self.biPolar.setObjectName(_fromUtf8("biPolar"))
        self.verticalLayout_3.addWidget(self.groupBox)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.groupBox_3 = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.binary_lbl = QtGui.QRadioButton(self.groupBox_3)
        self.binary_lbl.setGeometry(QtCore.QRect(10, 0, 109, 21))
        self.binary_lbl.setChecked(True)
        self.binary_lbl.setObjectName(_fromUtf8("binary_lbl"))
        self.bipolar_lbl = QtGui.QRadioButton(self.groupBox_3)
        self.bipolar_lbl.setGeometry(QtCore.QRect(10, 30, 109, 21))
        self.bipolar_lbl.setObjectName(_fromUtf8("bipolar_lbl"))
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.LMS = QtGui.QRadioButton(self.groupBox_2)
        self.LMS.setGeometry(QtCore.QRect(10, 60, 106, 21))
        self.LMS.setObjectName(_fromUtf8("LMS"))
        self.Hebb = QtGui.QRadioButton(self.groupBox_2)
        self.Hebb.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.Hebb.setChecked(True)
        self.Hebb.setObjectName(_fromUtf8("Hebb"))
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.number_neurons = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.number_neurons.setMinimum(1)
        self.number_neurons.setObjectName(_fromUtf8("number_neurons"))
        self.verticalLayout_3.addWidget(self.number_neurons)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, -1, 161, 551))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.data_tree = QtGui.QTreeWidget(self.verticalLayoutWidget_2)
        self.data_tree.setObjectName(_fromUtf8("data_tree"))
        self.verticalLayout.addWidget(self.data_tree)
        self.add_class = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.add_class.setObjectName(_fromUtf8("add_class"))
        self.verticalLayout.addWidget(self.add_class)
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(169, -1, 451, 551))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.SLP = QtGui.QWidget()
        self.SLP.setObjectName(_fromUtf8("SLP"))
        self.img_3 = QtGui.QLabel(self.SLP)
        self.img_3.setGeometry(QtCore.QRect(10, 150, 100, 100))
        self.img_3.setFrameShape(QtGui.QFrame.Box)
        self.img_3.setText(_fromUtf8(""))
        self.img_3.setObjectName(_fromUtf8("img_3"))
        self.img_2 = QtGui.QLabel(self.SLP)
        self.img_2.setGeometry(QtCore.QRect(140, 9, 100, 100))
        self.img_2.setFrameShape(QtGui.QFrame.Box)
        self.img_2.setText(_fromUtf8(""))
        self.img_2.setObjectName(_fromUtf8("img_2"))
        self.img_1 = QtGui.QLabel(self.SLP)
        self.img_1.setGeometry(QtCore.QRect(9, 9, 100, 100))
        self.img_1.setFrameShape(QtGui.QFrame.Box)
        self.img_1.setText(_fromUtf8(""))
        self.img_1.setObjectName(_fromUtf8("img_1"))
        self.info = QtGui.QLabel(self.SLP)
        self.info.setGeometry(QtCore.QRect(138, 150, 271, 101))
        self.info.setText(_fromUtf8(""))
        self.info.setObjectName(_fromUtf8("info"))
        self.test_btn = QtGui.QPushButton(self.SLP)
        self.test_btn.setGeometry(QtCore.QRect(10, 270, 101, 27))
        self.test_btn.setObjectName(_fromUtf8("test_btn"))
        self.test_lbl = QtGui.QLabel(self.SLP)
        self.test_lbl.setGeometry(QtCore.QRect(200, 220, 59, 14))
        self.test_lbl.setText(_fromUtf8(""))
        self.test_lbl.setObjectName(_fromUtf8("test_lbl"))
        self.iterations_lbl = QtGui.QLabel(self.SLP)
        self.iterations_lbl.setGeometry(QtCore.QRect(220, 250, 59, 14))
        self.iterations_lbl.setText(_fromUtf8(""))
        self.iterations_lbl.setObjectName(_fromUtf8("iterations_lbl"))
        self.learn_info = QtGui.QLabel(self.SLP)
        self.learn_info.setGeometry(QtCore.QRect(138, 270, 271, 101))
        self.learn_info.setText(_fromUtf8(""))
        self.learn_info.setObjectName(_fromUtf8("learn_info"))
        self.tabWidget.addTab(self.SLP, _fromUtf8(""))
        self.MLP = QtGui.QWidget()
        self.MLP.setObjectName(_fromUtf8("MLP"))
        self.tabWidget.addTab(self.MLP, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(780, 29, 171, 521))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.activation = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.activation.setObjectName(_fromUtf8("activation"))
        self.verticalLayout_4.addWidget(self.activation)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.bias = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.bias.setObjectName(_fromUtf8("bias"))
        self.verticalLayout_4.addWidget(self.bias)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Learn.setText(_translate("MainWindow", "Обучить", None))
        self.label.setText(_translate("MainWindow", "Входной сигнал", None))
        self.polar.setText(_translate("MainWindow", "Полярный", None))
        self.biPolar.setText(_translate("MainWindow", "Биполярный", None))
        self.label_2.setText(_translate("MainWindow", "Метки классов", None))
        self.binary_lbl.setText(_translate("MainWindow", "(0,  1)", None))
        self.bipolar_lbl.setText(_translate("MainWindow", "(1, -1)", None))
        self.LMS.setText(_translate("MainWindow", "LMS", None))
        self.Hebb.setText(_translate("MainWindow", "Обучение Хебба", None))
        self.label_3.setText(_translate("MainWindow", "Число нейронов", None))
        self.data_tree.headerItem().setText(0, _translate("MainWindow", "Данные", None))
        self.add_class.setText(_translate("MainWindow", "Класс +", None))
        self.test_btn.setText(_translate("MainWindow", "Тест", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SLP), _translate("MainWindow", "Однослойный персептрон", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MLP), _translate("MainWindow", "Многослойный персептрон", None))
        self.label_4.setText(_translate("MainWindow", "Функция активации", None))
        self.label_5.setText(_translate("MainWindow", "Сигнал смещения", None))

