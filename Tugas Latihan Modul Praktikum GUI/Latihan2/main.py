import sys
from PyQt5.QtWidgets import QApplication

from Latihan2 import *

if __name__=='__main__':
        a = QApplication(sys.argv)

        minform = Latihan2()
        minform.show()

        a.exec_()
