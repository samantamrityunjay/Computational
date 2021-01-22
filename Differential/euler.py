import numpy as np


class eulerMethod:
    def __init__(self,x0,xf,y0,dx):
        self.x0 = x0
        self.xf = xf
        self.y0 = y0
        self.dx = dx
        self.X = [x0+i*dx for i in range(int((xf-x0)/dx)+1)]
        
    def euler(self,func):
        y=self.y0
        Y = [y]
        for i in range(int((self.xf-self.x0)/self.dx)):
            y = y + func(y)*self.dx
            Y.append(y)
        return Y
    def modifiedEuler(self,func):
        y=self.y0
        Y = [y]
        for i in range(int((self.xf-self.x0)/self.dx)):
            y1 = y + func(y)*self.dx/2
            f1 = func(y1)
            y = y + f1*self.dx
            Y.append(y)
        return Y
    def improvedEuler(self,func):
        y=self.y0
        Y = [y]
        for i in range(int((self.xf-self.x0)/self.dx)):
            y1 = y + func(y)*self.dx
            f1 = (func(y1) + func(y))/2
            y = y + f1*self.dx
            Y.append(y)
        return Y
    def RK4(self,func):
        y=self.y0
        Y = [y]
        for i in range(int((self.xf-self.x0)/self.dx)):
            y1 = y + func(y)*self.dx/2
            y2 = y + func(y1)*self.dx/2
            y3 = y + func(y2)*self.dx
            y = y + (func(y)+2*func(y1)+2*func(y2)+func(y3))*self.dx/6
            Y.append(y)
        return Y
    
    
        
