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
        MainWindow.resize(806, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(618, -1, 181, 551))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Learn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Learn.setObjectName(_fromUtf8("Learn"))
        self.verticalLayout_3.addWidget(self.Learn, QtCore.Qt.AlignTop)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.polar = QtGui.QRadioButton(self.groupBox)
        self.polar.setGeometry(QtCore.QRect(0, 40, 109, 21))
        self.polar.setChecked(True)
        self.polar.setObjectName(_fromUtf8("polar"))
        self.biPolar = QtGui.QRadioButton(self.groupBox)
        self.biPolar.setGeometry(QtCore.QRect(0, 70, 109, 21))
        self.biPolar.setObjectName(_fromUtf8("biPolar"))
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.LMS = QtGui.QRadioButton(self.groupBox_2)
        self.LMS.setGeometry(QtCore.QRect(0, 60, 106, 21))
        self.LMS.setObjectName(_fromUtf8("LMS"))
        self.Hebb = QtGui.QRadioButton(self.groupBox_2)
        self.Hebb.setGeometry(QtCore.QRect(0, 30, 151, 21))
        self.Hebb.setChecked(True)
        self.Hebb.setObjectName(_fromUtf8("Hebb"))
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, -1, 161, 551))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.data_tree = QtGui.QTreeWidget(self.verticalLayoutWidget_2)
        self.data_tree.setObjectName(_fromUtf8("data_tree"))
        self.verticalLayout.addWidget(self.data_tree)
        self.class_1 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.class_1.setObjectName(_fromUtf8("class_1"))
        self.verticalLayout.addWidget(self.class_1)
        self.class_2 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.class_2.setObjectName(_fromUtf8("class_2"))
        self.verticalLayout.addWidget(self.class_2)
        self.test_class = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.test_class.setObjectName(_fromUtf8("test_class"))
        self.verticalLayout.addWidget(self.test_class)
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
        self.lbl1 = QtGui.QLabel(self.SLP)
        self.lbl1.setGeometry(QtCore.QRect(140, 150, 59, 14))
        self.lbl1.setObjectName(_fromUtf8("lbl1"))
        self.lbl2 = QtGui.QLabel(self.SLP)
        self.lbl2.setGeometry(QtCore.QRect(140, 180, 59, 14))
        self.lbl2.setObjectName(_fromUtf8("lbl2"))
        self.sim_1 = QtGui.QLabel(self.SLP)
        self.sim_1.setGeometry(QtCore.QRect(200, 150, 59, 14))
        self.sim_1.setText(_fromUtf8(""))
        self.sim_1.setObjectName(_fromUtf8("sim_1"))
        self.sim_2 = QtGui.QLabel(self.SLP)
        self.sim_2.setGeometry(QtCore.QRect(200, 180, 59, 14))
        self.sim_2.setText(_fromUtf8(""))
        self.sim_2.setObjectName(_fromUtf8("sim_2"))
        self.tabWidget.addTab(self.SLP, _fromUtf8(""))
        self.MLP = QtGui.QWidget()
        self.MLP.setObjectName(_fromUtf8("MLP"))
        self.tabWidget.addTab(self.MLP, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 22))
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
        self.LMS.setText(_translate("MainWindow", "LMS", None))
        self.Hebb.setText(_translate("MainWindow", "Обучение Хебба", None))
        self.data_tree.headerItem().setText(0, _translate("MainWindow", "Данные", None))
        self.class_1.setText(_translate("MainWindow", "Класс 1 +", None))
        self.class_2.setText(_translate("MainWindow", "Класс 2 +", None))
        self.test_class.setText(_translate("MainWindow", " Тест +", None))
        self.lbl1.setText(_translate("MainWindow", "Класс 1:", None))
        self.lbl2.setText(_translate("MainWindow", "Класс 2:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SLP), _translate("MainWindow", "Однослойный персептрон", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MLP), _translate("MainWindow", "Многослойный персептрон", None))

