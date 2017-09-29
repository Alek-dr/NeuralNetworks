from View.NNView import NNView
from Model.NeuralNetwork.Perceptron import Perceptron
import numpy as np

class NNController():

    def __init__(self, inModel):
        self.mModel = inModel
        self.mView = NNView(self)
        self.mView.show()

        # self.X = None
        # self.Y = None
        # self.Test = None
        self.params = {}

    def set_params(self):
        if self.mModel.__class__ == Perceptron:
            self.params = {
                            'Hebb': self.mView.ui.Hebb.isChecked(),
                            'LMS' : self.mView.ui.LMS.isChecked(),
                            'signal' : self.mView.ui.polar.isChecked()
                           }

    def modelIsChanged(self, model):
        if model=='SLP':
            self.mModel = Perceptron()
        elif model=='MLP':
            pass

    #region add data to model

    def addDataX(self, val):
        if self.mModel.__class__ == Perceptron:
            if self.mView.ui.polar.isChecked():
                val = self.polar(val)
                self.mModel.signalType = 'polar'
            else:
                val = self.biPolar(val)
                self.mModel.signalType = 'bi_polar'
        self.mModel.dataX.append(val)

    def addDataY(self, val):
        if self.mModel.__class__ == Perceptron:
            if self.mView.ui.polar.isChecked():
                val = self.polar(val)
                self.mModel.signalType = 'polar'
            else:
                val = self.biPolar(val)
                self.mModel.signalType = 'bi_polar'
        self.mModel.dataY.append(val)

    def addDataTest(self, val):
        if self.mModel.__class__ == Perceptron:
            if self.mView.ui.polar.isChecked():
                val = self.polar(val)
                self.mModel.signalType = 'polar'
            else:
                val = self.biPolar(val)
                self.mModel.signalType = 'bi_polar'
        self.mModel.dataTest.append(val)

    #endregion

    #region signal

    def polar(self, data):
        data = np.where(data==255,0,1)
        return data

    def biPolar(self,data):
        data = np.where(data == 255,-1,1)
        return data

    def signal_type_changed(self, signal_type):
        if (signal_type=='polar') & (self.mModel.signalType!='polar'):
            if len(self.mModel.dataX)>0:
                for i in range(len(self.mModel.dataX)):
                    self.mModel.dataX[i] = np.where(self.mModel.dataX[i]==-1,0,1)
                    self.mModel.signalType = 'polar'
            if len(self.mModel.dataY)>0:
                for i in range(len(self.mModel.dataY)):
                    self.mModel.dataY[i] = np.where(self.mModel.dataY[i]==-1,0,1)
                    self.mModel.signalType = 'polar'
            if len(self.mModel.dataTest)>0:
                for i in range(len(self.mModel.dataTest)):
                    self.mModel.dataTest[i] = np.where(self.mModel.dataTest[i]==-1,0,1)
                    self.mModel.signalType = 'polar'
        elif (signal_type=='biPolar') & (self.mModel.signalType!='bi_polar'):
            if len(self.mModel.dataX)>0:
                for i in range(len(self.mModel.dataX)):
                    self.mModel.dataX[i] = np.where(self.mModel.dataX[i]==0,-1,1)
                    self.mModel.signalType = 'bi_polar'
            if len(self.mModel.dataY)>0:
                for i in range(len(self.mModel.dataY)):
                    self.mModel.dataY[i] = np.where(self.mModel.dataY[i]==0,-1,1)
                    self.mModel.signalType = 'bi_polar'
            if len(self.mModel.dataTest)>0:
                for i in range(len(self.mModel.dataTest)):
                    self.mModel.dataTest[i] = np.where(self.mModel.dataTest[i]==0,-1,1)
                    self.mModel.signalType = 'bi_polar'

    #endregion

    def learn(self):
        self.mModel.learn(self.params)



