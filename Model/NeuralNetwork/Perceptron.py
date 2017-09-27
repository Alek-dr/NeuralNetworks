from Model.NNModel import NNModel
from Model.NeuralNetwork.Neuron import Neuron

class Perceptron(NNModel):

    def __init__(self):
        self.neuron = None
        pass

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
