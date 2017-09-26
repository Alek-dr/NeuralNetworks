import sys
from PyQt4.QtGui import QApplication

from Model.NNModel import NNModel
from Controller.NNController import NNController

def main():
    app = QApplication(sys.argv)

    # создаём модель
    model = NNModel()

    # создаём контроллер и передаём ему ссылку на модель
    controller = NNController(model)

    app.exec()

if __name__ == '__main__':
    sys.exit(main())