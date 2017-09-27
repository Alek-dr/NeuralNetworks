class NNModel:

    def __init__(self):
        self._X = []
        self._Y = []
        self._Test = []
        self._observers = []

    @property
    def dataX(self):
        return self._X

    @property
    def dataY(self):
        return self._Y

    @property
    def dataTest(self):
        return self._Test

    @dataX.setter
    def dataX(self,val):
        self._X = val

    @dataY.setter
    def dataY(self, val):
        self._Y = val

    @dataTest.setter
    def dataTest(self, val):
        self._Test = val

    def addObserver(self, observer):
        self._observers.append(observer)

    def deleteObserver(self, observer):
        self._observers.remove(observer)

    def notifyObservers(self):
        for x in self._observers:
            x.modelIsChanged()
