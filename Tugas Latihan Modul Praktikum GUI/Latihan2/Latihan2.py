from PyQt5.QtWidgets import QWidget, QLabel

class Latihan2(QWidget):
        def __init__(self):
            super().__init__()
            self.setupUi()

        def setupUi(self):
            self.resize(500,200)
            self.move(400,400)
            self.setWindowTitle('Latihan 2 <Tag HTML>')

            self.label1 = QLabel('<h1>Rekayasa <font color=red>Perangkat <font color=blue>Lunak</font></h1>')
            self.label2 = QLabel('<b>Peserta Praktikum Pemrograman GUI</b>')
            self.label3 = QLabel('1. Monkey D Luffy')
            self.label4 = QLabel('2. Roronoa Zorro')
            self.label5 = QLabel('3. Takiya Genji')
            self.label1.move(10,10)
            self.label2.move(10,50)
            self.label3.move(35,75)
            self.label4.move(35,85)
            self.label5.move(35,95)
            self.label1.setParent(self)
            self.label2.setParent(self)
            self.label3.setParent(self)
            self.label4.setParent(self)
            self.label5.setParent(self)
