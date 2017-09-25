import numpy as np

class NNModel:

    def __init__(self, image_1, image_2):
        self._img1 = image_1
        self._img2 = image_2

        self._observers = []

    @property
    def img1(self):
        return self._img1

    @property
    def img2(self):
        return self._img2

    @img1.setter
    def img1(self,val):
        self.img1 = val

    @img2.setter
    def img2(self, val):
        self.img2 = val

    def addObservers(self, observer):
        self._observers.append(observer)

    def deleteObserver(self, observer):
        self._observers.remove(observer)

    def notifyObservers(self):
        for x in self._observers:
            x.modelIsChanged()
