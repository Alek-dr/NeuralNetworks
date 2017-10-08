from Model.NNModel import NNModel
from Model.NeuralNetwork.Neuron import Neuron
from numpy import zeros, square, squeeze

class Perceptron(NNModel):

    def __init__(self):
        self.neuron = Neuron(0)
        self._signal_type = 'polar'
        self.data = []
        self.test = []

    @property
    def signalType(self):
        return self._signal_type

    @signalType.setter
    def signalType(self, val):
        self._signal_type = val

    def learn(self, params):
        iter = 0
        lbl = self.data[0][0,0,0]
        img = squeeze(self.data[0], axis=2)

        if params['signal'] == 'polar':
            self.neuron.activation = 'binary_treshold'
        elif params['signal'] == 'bi_polar':
            self.neuron.activation = 'bipolar_treshold'

        if (len(self.dataX)>0)&(len(self.dataY)>0):
            if self.neuron.weights.shape[0] == 0:
                self.neuron.weights = zeros(square(self.dataX[0].shape[0])+1)
            if len(self.dataX)>0:
                if params['Hebb']==True:
                    iter = self.Hebb(params['signal'])
                elif params['LMS']==True:
                    self.LMS()
        return iter

    def Hebb(self, signal_type):
        learn = False
        iterations = 0
        while not learn:
            iterations+=1
            w = 1
            z = self.define_delta_w(signal_type, 1)
            k = self.dataX[0].shape[0]
            for x in self.dataX:
                w = 1
                for i in range(k):
                    for j in range(k):
                        self.neuron.weights[w] += x[i][j] * z
                        w+=1
            w = 1
            self.neuron.weights[0] += self.neuron.bias*z
            z = self.define_delta_w(signal_type, 0)
            for y in self.dataY:
                w = 1
                for i in range(k):
                    for j in range(k):
                        self.neuron.weights[w] += y[i][j] * z
                        w+=1
            self.neuron.weights[0] += self.neuron.bias * z
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
        return iterations

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
        w = 1
        for i in range(k):
            for j in range(k):
                self.weights[w] += self.weights[w]*inputs[i][j]*y

    def test(self, img):
        #пока так
        label = self.neuron.through(self.dataTest[0])
        return label

    def LMS(self):
        pass
