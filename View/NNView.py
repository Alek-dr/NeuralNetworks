from PyQt4.QtGui import QMainWindow, QDoubleValidator, QFileDialog, QTreeWidgetItem, QPixmap
from PyQt4.QtCore import SIGNAL
from Utility.NNModelObserver import NNModelObserver
from Utility.NNMeta import NNMeta
from View.MainWindow import Ui_MainWindow
from PyQt4.Qt import QStringListModel
from scipy.ndimage import imread
from Model.NeuralNetwork.Metrics import similarity

class NNView(QMainWindow, NNModelObserver, metaclass=NNMeta):

    def __init__(self, inController, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.mController = inController

        #Визуальное представление
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #регистрируем представление в качестве наблюдателя
        #self.mModel.addObserver(self)

        #Добавляем обработчики событий
        self.ui.class_1.clicked.connect(self.addDataX)
        self.ui.class_2.clicked.connect(self.addDataY)
        self.ui.test_class.clicked.connect(self.addTest)
        self.ui.Learn.clicked.connect(self.learn_clicked)
        self.ui.Hebb.clicked.connect(self.learn_alg)
        self.ui.LMS.clicked.connect(self.learn_alg)
        self.ui.polar.clicked.connect(self.signal_change)
        self.ui.biPolar.clicked.connect(self.signal_change)
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)
        self.ui.test_btn.clicked.connect(self.test_clicked)

        self.treeSettings()
        self.ui.img_1.setScaledContents(True)
        self.ui.img_2.setScaledContents(True)
        self.ui.img_3.setScaledContents(True)

        self.current_class_1 = None
        self.current_class_2 = None
        self.current_test = None

        self.mController.modelIsChanged(self.ui.tabWidget.currentWidget().objectName())

    def tab_changed(self):
        self.mController.modelIsChanged(self.ui.tabWidget.currentWidget().objectName())

    def test_clicked(self):
        label = self.mController.test(0)
        self.ui.test_lbl.setText(str(label))

    def signal_change(self):
        btn = self.sender()
        self.mController.signal_type_changed(btn.objectName())
        self.mController.set_params()

    def learn_alg(self):
        self.mController.set_params()

    def learn_clicked(self):
        self.mController.set_params()
        iter = self.mController.learn()
        self.ui.iterations_lbl.setText(str(iter))

    def treeSettings(self):
        self.item1 = QTreeWidgetItem(['Класс 1'])
        self.item2 = QTreeWidgetItem(['Класс 2'])
        self.item3 = QTreeWidgetItem(['Тест'])
        self.ui.data_tree.addTopLevelItem(self.item1)
        self.ui.data_tree.addTopLevelItem(self.item2)
        self.ui.data_tree.addTopLevelItem(self.item3)
        self.connect(self.ui.data_tree, SIGNAL("itemClicked(QTreeWidgetItem*, int)"), self.onClickItem)

    def modelIsChanged(self):
        pass

    def onClickItem(self, item, column):
        try:
            path = item.text(column)
            parent = item.parent().text(0)
            if parent=='Класс 1':
                img = imread(path)
                self.ui.img_1.setPixmap(QPixmap(path))
                self.current_class_1 = imread(path)
                if self.current_test is not None:
                    sim_1 = similarity(img, self.current_test)
                    self.ui.sim_1.setText(str(sim_1))
            if parent=='Класс 2':
                img = imread(path)
                self.ui.img_2.setPixmap(QPixmap(path))
                self.current_class_2 = imread(path)
                if self.current_test is not None:
                    sim_2 = similarity(img, self.current_test)
                    self.ui.sim_2.setText(str(sim_2))
            if parent=='Тест':
                self.ui.img_3.setPixmap(QPixmap(path))
                img = imread(path)
                self.current_test = img
                if self.current_class_1 is not None:
                    sim_1 = similarity(img, self.current_class_1)
                    self.ui.sim_1.setText(str(sim_1))
                if self.current_class_2 is not None:
                    sim_2 = similarity(img, self.current_class_2)
                    self.ui.sim_2.setText(str(sim_2))
        except:
            pass

    def addDataX(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFileMode(QFileDialog.ExistingFiles)
        filenames = QStringListModel()
        if dlg.exec_():
            filenames = dlg.selectedFiles()
        for f in filenames:
            self.item1.addChild(QTreeWidgetItem([str(f)]))
            img = imread(f, mode='P')
            self.mController.addDataX(img)

    def addDataY(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFileMode(QFileDialog.ExistingFiles)
        filenames = QStringListModel()
        if dlg.exec_():
            filenames = dlg.selectedFiles()
        for f in filenames:
            self.item2.addChild(QTreeWidgetItem([str(f)]))
            img = imread(f, mode='P')
            self.mController.addDataY(img)

    def addTest(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFileMode(QFileDialog.ExistingFiles)
        filenames = QStringListModel()
        if dlg.exec_():
            filenames = dlg.selectedFiles()
        for f in filenames:
            self.item3.addChild(QTreeWidgetItem([str(f)]))
            img = imread(f, mode='P')
            self.mController.addDataTest(img)