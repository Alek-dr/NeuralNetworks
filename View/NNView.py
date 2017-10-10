from PyQt4 import QtGui

from PyQt4.QtGui import QMainWindow, QDoubleValidator, QFileDialog, QTreeWidgetItem, QPixmap, QMenu, QAction
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import Qt

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

        #Добавляем обработчики событий
        self.ui.add_class.clicked.connect(self.add_class)
        self.ui.Learn.clicked.connect(self.learn_clicked)
        self.ui.Hebb.clicked.connect(self.learn_alg)
        self.ui.LMS.clicked.connect(self.learn_alg)
        self.ui.polar.clicked.connect(self.signal_changed)
        self.ui.biPolar.clicked.connect(self.signal_changed)
        self.ui.bipolar_lbl.clicked.connect(self.lbl_type_changed)
        self.ui.binary_lbl.clicked.connect(self.lbl_type_changed)
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)
        self.ui.test_btn.clicked.connect(self.test_clicked)

        self.treeSettings()
        self.ui.img_1.setScaledContents(True)
        self.ui.img_2.setScaledContents(True)
        self.ui.img_3.setScaledContents(True)
        self.current_test_id = 0

        self.active_class_item = None
        self.connect(self.ui.data_tree, SIGNAL("itemClicked(QTreeWidgetItem*, int)"), self.onClickItem)
        self.connect(self.ui.activation, SIGNAL("activated(const QString&)"), self.activation_changed)

        validator = QtGui.QDoubleValidator()
        self.ui.bias.setValidator(validator)

        self.mController.modelIsChanged(self.ui.tabWidget.currentWidget().objectName())
        act_functions = ['Бинарный порог', 'Биполярный порог']
        self.ui.activation.addItems(act_functions)
        self.params = {
            'Signal' :'',
            'Learn'  :'',
            'Label'  :'',
            'Neurons':'',
            'Activation':'',
            'Bias': ''
        }

    def set_params(self):
        self.signal_changed()
        self.learn_alg()
        self.lbl_type_changed()
        self.params['Neurons'] = self.ui.number_neurons.value()
        self.params['Activation'] = self.ui.activation.currentText()
        bias = self.ui.bias.text()
        if bias=='':
            bias = 0
        self.params['Bias'] = bias

    def add_class(self):
        count = self.ui.data_tree.topLevelItemCount()
        item = QTreeWidgetItem(['Класс '+str(count)])
        self.ui.data_tree.addTopLevelItem(item)

    def tab_changed(self):
        self.mController.modelIsChanged(self.ui.tabWidget.currentWidget().objectName())

    def activation_changed(self):
        self.set_params()
        self.mController.activation_changed(self.params)

    def test_clicked(self):
        self.ui.info.clear()
        outputs = self.mController.test(self.current_test_id)
        text = self.ui.info.text()
        self.ui.info.setText(text + '\n' + 'Выходы нейронов: ' + '\n')
        for i in outputs:
            self.ui.info.setText(self.ui.info.text() + str(i) + '\n')

    def signal_changed(self):
        btn = self.sender()
        #self.mController.signal_type_changed(btn.objectName())
        if self.ui.tabWidget.currentWidget().objectName()=='SLP':
            if self.ui.polar.isChecked():
                self.params['Signal'] = 'binary'
            elif self.ui.biPolar.isChecked():
                self.params['Signal'] = 'bi_polar'
            self.mController.signal_type_changed(self.params)

    def lbl_type_changed(self):
        btn = self.sender()
        if self.ui.tabWidget.currentWidget().objectName() == 'SLP':
            if self.ui.bipolar_lbl.isChecked():
                self.params['Label'] = 'bi_polar'
            elif self.ui.binary_lbl.isChecked():
                self.params['Label'] = 'binary'
            self.mController.label_type_changed(self.params)

    def learn_alg(self):
        if self.ui.tabWidget.currentWidget().objectName()=='SLP':
            if self.ui.Hebb.isChecked():
                self.params['Learn'] = 'Hebb'
            elif self.ui.LMS.isChecked():
                self.params['Learn'] = 'LMS'

    def learn_clicked(self):
        self.ui.info.clear()
        self.set_params()
        iter = self.mController.learn(self.params)
        text = 'Количество итераций: ' + str(iter)
        self.ui.info.setText(text)

    def treeSettings(self):
        self.ui.data_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.data_tree.customContextMenuRequested.connect(self.on_context_menu)
        self.popMenu = QMenu(self)
        self.popMenu.addAction(QtGui.QAction('Загрузить данные', self))
        self.popMenu.addAction(QtGui.QAction('Очистить', self))
        self.popMenu.triggered[QAction].connect(self.processtrigger)
        item = QTreeWidgetItem(['Тест'])
        self.ui.data_tree.addTopLevelItem(item)

    def processtrigger(self,q):
        self.set_params()
        if q.text()=='Загрузить данные':
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            dlg.setFileMode(QFileDialog.ExistingFiles)
            filenames = QStringListModel()
            if dlg.exec_():
                filenames = dlg.selectedFiles()
            if self.active_class_item is not None:
                for f in filenames:
                    self.active_class_item.addChild(QTreeWidgetItem([str(f)]))
                    img = imread(f, mode='P')
                    lbl = self.active_class_item.text(0)[-1] #считаем, что не будет двузначных меток
                    if self.active_class_item.text(0) == 'Тест':
                        self.mController.add_test(img,self.params)
                    else:
                        self.mController.add_data(img,lbl,self.params)
        elif q.text()=='Очистить':
            count = self.active_class_item.childCount()
            for _ in range(count):
                self.active_class_item.removeChild(self.active_class_item.child(0))
            if self.active_class_item.text(0)=='Тест':
                self.mController.delete_test()
            else:
                lbl = self.active_class_item.text(0)[-1]
                self.mController.delete_data(lbl)
        self.active_class_item = None

    def on_context_menu(self, point):
        # show context menu
        index = self.ui.data_tree.indexAt(point)
        if not index.isValid():
            return
        item = self.ui.data_tree.itemAt(point)
        self.active_class_item = item
        self.popMenu.exec_(self.ui.data_tree.mapToGlobal(point))

    def modelIsChanged(self):
        pass

    def onClickItem(self, item, column):
        try:
            parent = 'Класс '
            parent_name = item.parent().text(0)
            i = 1
            if parent_name=='Тест':
                for j in range(item.parent().childCount()):
                    if item.parent().child(j) == item:
                        self.current_test_id = j
                        break
                path = item.text(column)
                self.ui.img_3.setPixmap(QPixmap(path))
                img = imread(path)
                self.current_test = img
            else:
                parent_ = parent + str(i)
                while parent_name!=parent_:
                    parent_ = parent + str(i)
                    i+=1
                path = item.text(column)

                if parent_=='Класс 1':
                    self.ui.img_1.setPixmap(QPixmap(path))
                else:
                    self.ui.img_2.setPixmap(QPixmap(path))
        except:
            pass