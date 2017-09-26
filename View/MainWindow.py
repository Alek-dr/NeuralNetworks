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
        MainWindow.resize(768, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.data_tree = QtGui.QTreeWidget(self.centralwidget)
        self.data_tree.setObjectName(_fromUtf8("data_tree"))
        self.horizontalLayout.addWidget(self.data_tree)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.class_1 = QtGui.QPushButton(self.centralwidget)
        self.class_1.setObjectName(_fromUtf8("class_1"))
        self.gridLayout.addWidget(self.class_1, 1, 0, 1, 1)
        self.class_2 = QtGui.QPushButton(self.centralwidget)
        self.class_2.setObjectName(_fromUtf8("class_2"))
        self.gridLayout.addWidget(self.class_2, 2, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.img_3 = QtGui.QLabel(self.tab)
        self.img_3.setGeometry(QtCore.QRect(10, 150, 100, 100))
        self.img_3.setFrameShape(QtGui.QFrame.Box)
        self.img_3.setText(_fromUtf8(""))
        self.img_3.setObjectName(_fromUtf8("img_3"))
        self.img_2 = QtGui.QLabel(self.tab)
        self.img_2.setGeometry(QtCore.QRect(140, 9, 100, 100))
        self.img_2.setFrameShape(QtGui.QFrame.Box)
        self.img_2.setText(_fromUtf8(""))
        self.img_2.setObjectName(_fromUtf8("img_2"))
        self.img_1 = QtGui.QLabel(self.tab)
        self.img_1.setGeometry(QtCore.QRect(9, 9, 100, 100))
        self.img_1.setFrameShape(QtGui.QFrame.Box)
        self.img_1.setText(_fromUtf8(""))
        self.img_1.setObjectName(_fromUtf8("img_1"))
        self.lbl1 = QtGui.QLabel(self.tab)
        self.lbl1.setGeometry(QtCore.QRect(140, 150, 59, 14))
        self.lbl1.setObjectName(_fromUtf8("lbl1"))
        self.lbl2 = QtGui.QLabel(self.tab)
        self.lbl2.setGeometry(QtCore.QRect(140, 180, 59, 14))
        self.lbl2.setObjectName(_fromUtf8("lbl2"))
        self.sim_1 = QtGui.QLabel(self.tab)
        self.sim_1.setGeometry(QtCore.QRect(200, 150, 59, 14))
        self.sim_1.setText(_fromUtf8(""))
        self.sim_1.setObjectName(_fromUtf8("sim_1"))
        self.sim_2 = QtGui.QLabel(self.tab)
        self.sim_2.setGeometry(QtCore.QRect(200, 180, 59, 14))
        self.sim_2.setText(_fromUtf8(""))
        self.sim_2.setObjectName(_fromUtf8("sim_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.Learn = QtGui.QPushButton(self.centralwidget)
        self.Learn.setObjectName(_fromUtf8("Learn"))
        self.gridLayout.addWidget(self.Learn, 0, 2, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 3, 1, 1)
        self.test_class = QtGui.QPushButton(self.centralwidget)
        self.test_class.setObjectName(_fromUtf8("test_class"))
        self.gridLayout.addWidget(self.test_class, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 22))
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
        self.data_tree.headerItem().setText(0, _translate("MainWindow", "Данные", None))
        self.class_1.setText(_translate("MainWindow", "Класс 1 +", None))
        self.class_2.setText(_translate("MainWindow", "Класс 2 +", None))
        self.lbl1.setText(_translate("MainWindow", "Класс 1:", None))
        self.lbl2.setText(_translate("MainWindow", "Класс 2:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Однослойный персептрон", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Многослойный персептрон", None))
        self.Learn.setText(_translate("MainWindow", "Обучить", None))
        self.test_class.setText(_translate("MainWindow", " Тест +", None))

