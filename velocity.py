import numpy as np

def velocity(xVel: int, yVel: int):
    '''Returns the veloctity vector,
    Requires (x-coord, y-coord)'''
    return np.sqrt(xVel**2 + yVel**2)

