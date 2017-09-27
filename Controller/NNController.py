from View.NNView import NNView
from Model.NeuralNetwork.Perceptron import Perceptron
import numpy as np

class NNController():

    def __init__(self, inModel):
        self.mModel = inModel
        self.mView = NNView(self)
        self.mView.show()

        self.X = None
        self.Y = None
        self.Test = None
        self.params = {}

    def set_params(self):
        if self.mModel.__class__ == Perceptron:
            self.params = {'Hebb':self.mView.ui.Hebb.isChecked(),
                           'LMS' :self.mView.ui.LMS.isChecked()
                           }

    def modelIsChanged(self, modelName):
        if modelName=='Однослойный персептрон':
            self.mModel = Perceptron()

    def addDataX(self, val):
        if self.mModel.__class__ == Perceptron:
            if self.mView.ui.polar.isChecked():
                val = self.polar(val)
            else:
                val = self.biPolar(val)
        self.mModel.dataX = val

    def polar(self, data):
        data = np.where(data==255,1,0)
        return data

    def biPolar(self,data):
        data = np.where(data == 255, 1, -1)
        return data

    def learn(self):
        self.mModel.learn(self.params)

