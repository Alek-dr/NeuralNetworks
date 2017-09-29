class NNModel:

    def __init__(self):
        self._X = []
        self._Y = []
        self._Test = []
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
