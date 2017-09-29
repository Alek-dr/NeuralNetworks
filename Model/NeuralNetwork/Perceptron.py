from Model.NNModel import NNModel
from Model.NeuralNetwork.Neuron import Neuron
from numpy import zeros, square

class Perceptron(NNModel):

    def __init__(self):
        self.neuron = Neuron(0)
        self._signal_type = 'polar'
        self.dataX = []
        self.dataY = []
        self.dataTest = []

    @property
    def signalType(self):
        return self._signal_type

    @signalType.setter
    def signalType(self, val):
        self._signal_type = val

    def learn(self, params):
        if (len(self.dataX)>0)&(len(self.dataY)>0):
            if self.neuron.weights.shape[0] == 0:
                self.neuron.weights = zeros(square(self.dataX[0].shape[0]))
            if len(self.dataX)>0:
                if params['Hebb']==True:
                    self.Hebb(params['signal'])
                elif params['LMS']==True:
                    self.LMS()

    def Hebb(self, signal_type):
        learn = False
        while not learn:
            w = 0
            z = self.define_delta_w(signal_type, 1)
            k = self.dataX[0].shape[0]
            for x in self.dataX:
                for i in range(k):
                    for j in range(k):
                        self.neuron.weights[w] += x[i][j] * z
                        w+=1
            w = 0
            z = self.define_delta_w(signal_type, 0)
            for y in self.dataY:
                for i in range(k):
                    for j in range(k):
                        self.neuron.weights[w] += y[i][j] * z
                        w+=1
            has_learned = True
            for x in self.dataX:
                y = self.neuron.through(x)
                if y!=1:
                    has_learned=False
                    break
            if has_learned==False:
                continue
            else:
                for y in self.dataY:
                    y = self.neuron.through(y)
                    if y != -1:
                        break
            if has_learned==True:
                learn=True


    def define_delta_w(self, signal, label):
        if signal==True:
            #если бинарный
            if label==1:
                return 1
            elif label==0:
                return 0
            else:
                return 1
        else:
            if label==1:
                return 1
            else:
                return -1

    def correct(self,inputs,y):
        k = len(inputs)
        w = 0
        for i in range(k):
            for j in range(k):
                self.weights[w] += self.weights[w]*inputs[i][j]*y

    def LMS(self):
        pass
