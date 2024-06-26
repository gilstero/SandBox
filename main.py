import sys
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class SandboxLoader(QMainWindow):
    def __init__(self):
        super(SandboxLoader, self).__init__()
        uic.loadUi("Assets/SandBox.ui", self)
        self.show()

class Container(QMainWindow): # container is built on Q1 of the graph where both x and y are positive
    def __init__(self, resistance, accel):
        super(Container, self).__init__()
        self.setWindowTitle("SandBox")
        self.acceptDrops()
        self.resize(1000, 600) # Set geometry of the window to center of screen when loading
        self.center()
        self.length = 1000
        self.height = 600
        self.resistance = resistance
        self.accel = accel

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def checkCollisionWithContainer(self, ball):
        flag = False
        if ((ball.x - ball.size) < 0):
            ball.xVel *= -0.9
            flag = True
        if ((ball.x + ball.size) > self.length):
            ball.xVel *= -0.9
            flag = True
        if ((ball.y - ball.size) < 0):
            ball.yVel *= -0.9
            flag = True
        if ((ball.y + ball.size) > self.height):
            ball.yVel *= -0.9
            flag = True
        if (flag == True):
            print("HIT WALL")
            ball.x += ball.xVel
            ball.y += ball.yVel

class Ball():
    def __init__(self):
        self.size = 10 # radius
        self.color = (0,0,0)
        self.x = 100
        self.y = 100
        self.xVel = 0
        self.yVel = 0
    
    def velocity(self):
        '''Returns the veloctity vector,
        Requires (x-coord, y-coord)'''
        return round(np.sqrt(self.xVel**2 + self.yVel**2), 3)
    
    def increment(self, container: Container):
        self.x += self.xVel
        self.y += self.yVel
        container.checkCollisionWithContainer(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loader = SandboxLoader()

    # mainContainer = Container(0, 0)
    # mainContainer.show()
    app.exec_()