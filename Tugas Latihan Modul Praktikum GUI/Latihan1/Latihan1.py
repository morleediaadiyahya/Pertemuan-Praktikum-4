from PyQt5.QtWidgets import QWidget, QLabel

class Latihan1(QWidget):
        def __init__(self):
            super().__init__()
            self.setupUi()

        def setupUi(self):
            self.resize(500,200)
            self.move(400,400)
            self.setWindowTitle('Praktikum Pemrograman GUI')

            self.label1 = QLabel('Dosen Pengampu :')
            self.label2 = QLabel('Afandi Nur Aziz Thohari, S.T.,M.Cs')
            self.label3 = QLabel('Copyright @2019')
            self.label1.move(50,40)
            self.label2.move(50,50)
            self.label3.move(210,180)
            self.label1.setParent(self)
            self.label2.setParent(self)
            self.label3.setParent(self)
