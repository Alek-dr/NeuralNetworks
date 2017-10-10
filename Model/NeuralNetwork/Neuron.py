from numpy import zeros, dot, square, ravel, double

from Model.NeuralNetwork.ActivationFunctions import bipolar_treshold, binary_treshold


class Neuron:

    def __init__(self, id, inputs=0, activation='bipolar_treshold'):
        self.id = id
        self.weights = zeros(inputs)
        self.bias = 0
        self.activation = activation

    def through(self, inputs):
        if len(self.weights)==0:
            self.weights = zeros(square(inputs.shape[0]))
        out = self.adderOutput(inputs)
        y = self.functionOutput(out)
        return y

    def adderOutput(self,inputs):
        inputs = ravel(inputs)
        out = dot(self.weights,inputs) + double(self.bias)
        return out

    def functionOutput(self, v):
        if self.activation == 'binary_treshold':
            return binary_treshold(v)
        elif self.activation == 'bipolar_treshold':
            return bipolar_treshold(v)
