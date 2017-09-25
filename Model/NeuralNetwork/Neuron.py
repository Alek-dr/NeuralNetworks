from numpy import zeros

from Model.NeuralNetwork.ActivationFunctions import treshold


class Neuron:

    functions = {'Treshold'}

    def __init__(self, id, inputs):
        self.id = id
        self.weights = zeros(inputs)
        self.bias = 1
        self.activation = Neuron.functions[0]

    def __init__(self, id, inputs, activation):
        self.id = id
        self.weights = zeros(inputs)
        self.bias = 1
        self.activation = Neuron.functions[activation]

    def through(self, inputs):
        out = self.adderOutput(inputs)
        y = self.functionOutput(out)
        return y

    def adderOutput(self,inputs):
        k = len(inputs)
        out = 0
        for i in range(k):
            out += self.weights[i]*inputs[i]
        out += 1*self.bias
        return out

    def functionOutput(self, v):
        if self.activation == 'Treshold':
            return treshold(v)
