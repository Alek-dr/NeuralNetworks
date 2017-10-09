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
        if self.mModel.__class__ == Perceptron:
            if params['Signal'] == 'binary':
                val = self.polar(val)
            elif params['Signal'] == 'bi_polar':
                val = self.biPolar(val)
            # val= val[..., np.newaxis]
            # val[0,0,0] = lbl
            self.mModel.labels.append(lbl)
            self.mModel.data.append(val)

    def add_test(self, val, params):
        if self.mModel.__class__ == Perceptron:
            if params['Signal'] == 'polar':
                val = self.polar(val)
            elif params['Signal'] == 'bi_polar':
                val = self.biPolar(val)
            self.mModel.test.append(val)

    #endregion

    #region signal

    def polar(self, data):
        data = np.where(data==255,0,1)
        return data

    def biPolar(self,data):
        data = np.where(data == 255,-1,1)
        return data

    def signal_type_changed(self, params):
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

    #endregion

    def learn(self, params):
        iter = self.mModel.learn(params)
        return iter

    def test(self,img):
        #потом придумаю как передать конкретную картинку
        self.mModel.test_x(img)




