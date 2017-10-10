from Model.NNModel import NNModel
from Model.NeuralNetwork.Neuron import Neuron
from numpy import zeros, square, squeeze, array, unique, ravel, multiply, double

class Perceptron(NNModel):

    def __init__(self):
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
        self.neurons.clear()
        for i in range(n_neurons):
            self.neurons.append(Neuron(i))
            self.neurons[i].activation = params['Activation']
            self.neurons[i].bias = params['Bias']
        if (len(self.data) > 0):
            for n in self.neurons:
                n.weights = zeros(self.data[0].size)
            if params['Learn'] == 'Hebb':
                iter = self.Hebb()
        return iter

    def Hebb(self):
        learned = False
        iter = 0
        while learned==False:
            iter+=1
            for i, n in enumerate(self.neurons):
                i+=1
                for j, x in enumerate(self.data):
                    lbl = self.labels[j]
                    lbl_ = self.define_label(lbl,i)
                    self.correct(x, n, lbl_)
            if self.check_stop()==True:
                learned=True
        return iter

    def set_bias(self, val):
        for n in self.neurons:
            n.bias = double(val)

    def check_stop(self):
        for i, n in enumerate(self.neurons):
            i+=1
            for j, x in enumerate(self.data):
                lbl = self.labels[j]
                lbl_ = self.define_label(lbl,i)
                test_lbl = n.through(x)
                lbl_, test_lbl = self.label_definition(lbl_, test_lbl)
                if test_lbl!=lbl_:
                    return False
        return True

    def label_definition(self, lbl_, test_lbl):
        if self._lbl_type == 'binary':
            if lbl_ == -1:
                lbl_ = 0
            if test_lbl == -1:
                test_lbl = 0
        elif self._lbl_type == 'bi_polar':
            if lbl_ == 0:
                lbl_ = -1
            if test_lbl == 0:
                test_lbl = -1
        return lbl_, test_lbl

    def define_label(self,lbl, n):
        lbl = int(lbl)
        if lbl==n:
            return 1
        else:
            return -1

    def define_lbl_for_check(self,lbl, n):
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

    def correct(self,inputs,n,y):
        inputs = ravel(inputs)
        k = len(inputs)
        lbl = zeros(shape=[k])
        lbl.fill(y)
        n.weights += multiply(inputs,lbl)

    def set_activation(self, params):
        for n in self.neurons:
            n.activation = params['Activation']

    def test_x(self, img, params):
        self._lbl_type = params['Label']
        outputs = zeros(len(self.neurons))
        for i, n in enumerate(self.neurons):
            lbl = n.through(self.test[img])
            if self._lbl_type=='binary':
                if lbl == -1:
                    lbl = 0
            elif self._lbl_type=='bi_polar':
                if lbl ==0:
                    lbl = -1
            outputs[i] = lbl
        return outputs

    def LMS(self):
        pass
