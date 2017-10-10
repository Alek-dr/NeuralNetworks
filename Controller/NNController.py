from View.NNView import NNView
from Model.NeuralNetwork.Perceptron import Perceptron
import numpy as np

class NNController():

    def __init__(self, inModel):
        self.mModel = inModel
        self.mView = NNView(self)
        self.mView.show()

    def modelIsChanged(self, model):
        if model=='SLP':
            self.mModel = Perceptron()
        elif model=='MLP':
            pass

    #region add data to model

    def add_data(self, val, lbl, params):
        #Добавление данных для обучения
        if self.mModel.__class__ == Perceptron:
            if params['Signal'] == 'binary':
                val = self.binary(val)
            elif params['Signal'] == 'bi_polar':
                val = self.biPolar(val)
            self.mModel.labels.append(lbl)
            self.mModel.data.append(val)

    def add_test(self, val, params):
        #Добавление данных для теста
        #эти данные не содержат метки класса
        if self.mModel.__class__ == Perceptron:
            if params['Signal'] == 'binary':
                val = self.binary(val)
            elif params['Signal'] == 'bi_polar':
                val = self.biPolar(val)
            self.mModel.test.append(val)

    #endregion

    #region signal

    def binary(self, data):
        data = np.where(data==255,0,1)
        return data

    def biPolar(self,data):
        data = np.where(data == 255,-1,1)
        return data

    def signal_type_changed(self, params):
        #Два типа сигналов: {1,0}, {1,-1}
        #Значения изменяются в самой модели персептрона
        signal_type = params['Signal']
        if (signal_type=='binary') & (self.mModel.signalType!='binary'):
            if len(self.mModel.data)>0:
                for i in range(len(self.mModel.data)):
                    self.mModel.data[i] = np.where(self.mModel.data[i]==-1,0,1)
                    self.mModel.signalType = 'binary'
            if len(self.mModel.test)>0:
                for i in range(len(self.mModel.test)):
                    self.mModel.test[i] = np.where(self.mModel.test[i]==-1,0,1)
                    self.mModel.signalType = 'binary'
        elif (signal_type=='bi_polar') & (self.mModel.signalType!='bi_polar'):
            if len(self.mModel.data)>0:
                for i in range(len(self.mModel.data)):
                    self.mModel.data[i] = np.where(self.mModel.data[i]==0,-1,1)
                    self.mModel.signalType = 'bi_polar'
            if len(self.mModel.test)>0:
                for i in range(len(self.mModel.test)):
                    self.mModel.test[i] = np.where(self.mModel.test[i]==0,-1,1)
                    self.mModel.signalType = 'bi_polar'

    def label_type_changed(self, params):
        self.mModel.labelType = params['Label']

    def activation_changed(self, params):
        params = self.rename_function(params)
        self.mModel.set_activation(params)

    #endregion

    def learn(self, params):
        params = self.rename_function(params)
        return self.mModel.learn(params)

    def test(self,img, params):
        params = self.rename_function(params)
        self.mModel.set_activation(params)
        return self.mModel.test_x(img,params)

    def delete_data(self, label):
        labels = np.array(self.mModel.labels)
        lbl2del = np.squeeze(np.where(labels==label), axis=1).astype(np.uint32)
        self.mModel.data = np.delete(self.mModel.data, lbl2del).tolist()
        self.mModel.labels = np.delete(self.mModel.labels, lbl2del).tolist()

    def delete_test(self):
        self.mModel.test.clear()

    def rename_function(self,params):
        if params['Activation']=='Бинарный порог':
            params['Activation'] = 'binary_treshold'
        elif params['Activation']=='Биполярный порог':
            params['Activation'] = 'bipolar_treshold'
        return params

    def set_bias(self, params):
        self.mModel.set_bias(params['Bias'])




