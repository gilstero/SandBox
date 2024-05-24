import sys
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QApplication, QSplashScreen
from PyQt5.uic import loadUi
from velocity import *

class splashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("loader.ui",self)
        self.setWindowFlag(Qt.FramlessWindowHint)
        pixmap = QPixmap("LightGrey.jpg")
        self.setPixmap(pixmap)

    def wait():
        time.sleep(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = splashScreen()
    splash.show()
    splash.wait()

    app.exec_()