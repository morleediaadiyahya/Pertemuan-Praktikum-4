import sys
from PyQt5.QtWidgets import QApplication

from Latihan1 import *

if __name__=='__main__':
        a = QApplication(sys.argv)

        minform = Latihan1()
        minform.show()

        a.exec_()
