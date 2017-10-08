class NNModel:

    def __init__(self):
        self.data = []
        self.test = []
        self._observers = []

    def addObserver(self, observer):
        self._observers.append(observer)

    def deleteObserver(self, observer):
        self._observers.remove(observer)

    def notifyObservers(self):
        for x in self._observers:
            x.modelIsChanged()

    def learn(self, params):
        pass

    def through(self, inputs):
        pass
