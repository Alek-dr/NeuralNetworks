from Model.NNModel import NNModel
from Model.NeuralNetwork.Neuron import Neuron
from numpy import zeros, ravel, multiply, double

class Perceptron(NNModel):

    def __init__(self):
        self._signal_type = 'binary' # тип сигнала - {1,0} или {1,-1}
        self._lbl_type = 'binary' #тип меток - {1,0} или {1,-1}
        self.data = [] #данные для обучения
        self.labels = [] #метки классов
        self.test = [] #данные для теста
        self.neurons = [] #нейроны

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
        #Обучение, params содержит всю необходимую информацию
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
        #Обучение Хебба
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
        #Проврка условия останова для Хебба
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
        #Придерживаемся идеи, что метки и функция активации - не одно и то же!!!
        #т.е. если метка класса -1, а функция активации вернула 0, это класс с меткой -1
        #здесь два параметра, потому что авторефакторинг
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

    def correct(self,inputs,n,y):
        #Корректировка весов
        inputs = ravel(inputs)
        k = len(inputs)
        lbl = zeros(shape=[k])
        lbl.fill(y)
        n.weights += multiply(inputs,lbl)

    def set_activation(self, params):
        #Установка функции активации
        for n in self.neurons:
            n.activation = params['Activation']

    def test_x(self, img, params):
        #Тест входного изображения img
        self._lbl_type = params['Label']
        outputs = zeros(len(self.neurons))
        for i, n in enumerate(self.neurons):
            lbl = n.through(self.test[img])
            lbl, _ = self.label_definition(lbl, 1)
            outputs[i] = lbl
        return outputs

    def LMS(self):
        pass
