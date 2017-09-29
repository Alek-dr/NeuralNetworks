from Model.NNModel import NNModel
from Model.NeuralNetwork.Neuron import Neuron

class Perceptron(NNModel):

    def __init__(self):
        self.neuron = None
        self._signal_type = 'polar'

    @property
    def signalType(self):
        return self._signal_type

    @signalType.setter
    def signalType(self, val):
        self._signalType = val

    def learn(self, params):
        if self.dataX is not None:
            if len(self.dataX)>0:
                if params['Hebb']==True:
                    self.Hebb()
                elif params['LMS']==True:
                    self.LMS()

    def Hebb(self):
        pass

    def LMS(self):
        pass
