from PyQt4.QtGui import QMainWindow, QDoubleValidator, QFileDialog, QTreeWidgetItem
from PyQt4.QtCore import SIGNAL
from Utility.NNModelObserver import NNModelObserver
from Utility.NNMeta import NNMeta
from View.MainWindow import Ui_MainWindow
from PyQt4.Qt import QStringListModel

class NNView(QMainWindow, NNModelObserver, metaclass=NNMeta):

    def __init__(self, inController, inModel, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.mController = inController
        self.mModel = inModel

        #Визуальное представление
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #регистрируем представление в качестве наблюдателя
        self.mModel.addObserver(self)

        #Добавляем обработчики событий
        self.ui.class_1.clicked.connect(self.addDataX)

        self.additionalSettings()

    def additionalSettings(self):
        item1 = QTreeWidgetItem(['Класс 1'])
        item1.addChild(QTreeWidgetItem(['']))
        item2 = QTreeWidgetItem(['Класс 2'])
        item2.addChild(QTreeWidgetItem(['']))
        item3 = QTreeWidgetItem(['Тест'])
        item3.addChild(QTreeWidgetItem(['']))
        self.ui.data_tree.addTopLevelItem(item1)
        self.ui.data_tree.addTopLevelItem(item2)
        self.ui.data_tree.addTopLevelItem(item3)

    def modelIsChanged(self):
        pass

    def addDataX(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFileMode(QFileDialog.ExistingFiles)
        filenames = QStringListModel()
        if dlg.exec_():
            filenames = dlg.selectedFiles()
        for f in filenames:
            print(f)
