from Model.NNModel import NNModel
from Model.NeuralNetwork.Neuron import Neuron

class Perceptron(NNModel):

    def __init__(self):
        self.neuron = None
        pass

    @ super.setter
    def dataX(self, val):
        self.dataX = val

    @super.setter
    def dataY(self, val):
        self.dataY = val

    @super.setter
    def dataTest(self, val):
        self.dataTest = val
