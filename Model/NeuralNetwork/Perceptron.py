from Model.NNModel import NNModel
from Model.NeuralNetwork.Neuron import Neuron
from numpy import zeros, square, squeeze, array, unique, ravel, multiply

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
                n.weights = zeros(square(self.data[0].shape[0]))
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

    def check_stop(self):
        for i, n in enumerate(self.neurons):
            i+=1
            for j, x in enumerate(self.data):
                lbl = self.labels[j]
                lbl_ = self.define_lbl_for_check(lbl,i)
                test_lbl = n.through(x)
                if test_lbl!=lbl_:
                    return False
        return True

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

    def test_x(self, img):
        outputs = zeros(len(self.neurons))
        for i, n in enumerate(self.neurons):
            outputs[i] = n.through(self.test[img])
        return outputs

    def LMS(self):
        pass
