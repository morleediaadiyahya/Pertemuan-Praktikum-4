from PyQt5.QtWidgets import QWidget, QPushButton, QLabel

class About(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(155,110)
        self.move(50,50)
        self.setWindowTitle('About')

        self.label1 = QLabel('Dibuat oleh Tim RPL')
        self.label2 = QLabel('Versi 1.0')
        self.label3 = QLabel('Copyright@2019')
        self.label1.move(30,20)
        self.label2.move(30,30)
        self.label3.move(30,40)
        self.label1.setParent(self)
        self.label2.setParent(self)
        self.label3.setParent(self)

        self.button = QPushButton('OK')
        self.button.move(70,70)
        self.button.setParent(self)

        self.button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.close()
