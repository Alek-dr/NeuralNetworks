from View.NNView import NNView

class NNController():

    def __init__(self, inModel):
        self.mModel = inModel
        self.mView = NNView(self, self.mModel)
        self.mView.show()

        self.X = None
        self.Y = None
        self.Test = None

    def addDataX(self, val):
        self.mModel.dataX = val

