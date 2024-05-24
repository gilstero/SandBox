import sys
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QApplication, QSplashScreen
from PyQt5.uic import loadUi

class Container(): # container is built on Q1 of the graph where both x and y are positive
    def __init__(self, length, height): 
        self.length = length
        self.height = height

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
        self.xVel = 1
        self.yVel = 1
    
    def velocity(self):
        '''Returns the veloctity vector,
        Requires (x-coord, y-coord)'''
        return round(np.sqrt(self.xVel**2 + self.yVel**2), 3)
    
    def increment(self, container: Container):
        self.x += self.xVel
        self.y += self.yVel
        container.checkCollisionWithContainer(self)

if __name__ == '__main__':
    Ball1 = Ball()
    mainContainer = Container(200, 200)
    while True:
        Ball1.increment(mainContainer)
        print(Ball1.velocity())
        time.sleep(.1)