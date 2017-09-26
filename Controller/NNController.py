from View.NNView import NNView

class NNController():

    def __init__(self, inModel):
        self.mModel = inModel
        self.mView = NNView(self, self.mModel)
        self.mView.show()

    def addDataX(self):
        print('Add')
