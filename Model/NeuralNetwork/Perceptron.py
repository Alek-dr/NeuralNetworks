from Model.NNModel import NNModel
from Model.NeuralNetwork.Neuron import Neuron
from numpy import zeros, square, squeeze, array, unique, ravel, multiply

class Perceptron(NNModel):

    def __init__(self):
        #self.neuron = Neuron(0)
        self._signal_type = 'binary'
        self._lbl_type = 'binary'
        self.data = []
        self.labels = []
        self.test = []
        self.neurons = []

    @property
    def signalType(self):
        return self._signal_type

    @property
    def labelType(self):
        return self._lbl_type

    @signalType.setter
    def signalType(self, val):
        self._signal_type = val

    @labelType.setter
    def labelType(self, val):
        self._lbl_type = val

    def learn(self, params):
        iter = 0
        n_neurons = params['Neurons']
        self.labelType = params['Label']
        for i in range(n_neurons):
            self.neurons.append(Neuron(0))
        if params['Signal'] == 'polar':
            for n in self.neurons:
                n.activation = 'binary_treshold'
        elif params['Signal'] == 'bi_polar':
            for n in self.neurons:
                n.activation = 'bipolar_treshold'

        if (len(self.data) > 0):
            for n in self.neurons:
                n.weights = zeros(square(self.data[0].shape[0]))
            if params['Learn'] == 'Hebb':
                self.Hebb()
        return iter

    def Hebb(self):
        learned = False
        while learned==False:
            for i, n in enumerate(self.neurons):
                i+=1
                for j, x in enumerate(self.data):
                    lbl = self.labels[j]
                    lbl_ = self.define_label(lbl,i)
                    self.correct(x, n, lbl_)
            if self.check_stop()==True:
                learned=True

    def check_stop(self):
        for i, n in enumerate(self.neurons):
            i+=1
            for j, x in enumerate(self.data):
                lbl = self.labels[j]
                lbl_ = self.define_label(lbl,i)
                test_lbl = n.through(x)
                if test_lbl!=lbl_:
                    return False
        return True

    def define_label(self,lbl, n):
        lbl = int(lbl)
        if self._lbl_type=='binary':
            if lbl==n:
                return 1
            else:
                return 0
        elif self._lbl_type=='bi_polar':
            if lbl==n:
                return 1
            else:
                return -1


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

    def correct(self,inputs,n,y):
        inputs = ravel(inputs)
        k = len(inputs)
        lbl = zeros(shape=[k])
        lbl.fill(y)
        n.weights += multiply(inputs,lbl)

    def test_x(self, img):
        #пока так
        self.neuron.through(self.test[img])

    def LMS(self):
        pass
