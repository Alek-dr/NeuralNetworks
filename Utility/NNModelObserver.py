from abc import ABCMeta, abstractmethod

class NNModelObserver(metaclass=ABCMeta):

    @abstractmethod
    def modelIsChanged(self):
        pass