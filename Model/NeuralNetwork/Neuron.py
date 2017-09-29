from numpy import zeros

from Model.NeuralNetwork.ActivationFunctions import bipolar_treshold, binary_treshold


class Neuron:

    def __init__(self, id, inputs=0, activation='bipolar_treshold'):
        self.id = id
        self.weights = zeros(inputs)
        self.bias = 1
        self.activation = activation

    def through(self, inputs):
        out = self.adderOutput(inputs)
        y = self.functionOutput(out)
        return y

    def adderOutput(self,inputs):
        k = len(inputs)
        out = 0
        w = 0
        for i in range(k):
            for j in range(k):
                out += self.weights[w]*inputs[i][j]
                w+=1
        out += 1*self.bias
        return out

    def functionOutput(self, v):
        if self.activation == 'binary_treshold':
            return binary_treshold(v)
        elif self.activation == 'bipolar_treshold':
            return bipolar_treshold(v)
