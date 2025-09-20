import statistics as stat
from matplotlib import pyplot as plt
import numpy as np
plt.close('all')

class EulerMethod:
    def __init__(self):
        """
        Initializes the EulerMethod class, a class to calculate the 
        behavior of objects on a plot using Euler's Method.
        """
        self._thetaR = 0
        self._nHeight = 0
        self._dThetaR = 0
        self._v0 = 0
        self._dv0 = 0
        self._dy0 = 0
        self._dt = 0.05
        self._ax = 0
        self._ay = 0
        self._t = [0]
        self._x = []
        self._x0 = 0
        self._y = []
        self._x0 = 0
        self._vx = []
        self._vy = []
        self._ranges = []
    def setAcc(self, ax, ay):
        """Set the initial acceleration"""
        self._ax = ax
        self._ay = ay
    def setI(self, ix, iy):
        """Sets the initial x and y positions"""
        self._x.append(ix)
        self._y.append(iy)
        self._x0 = ix
        self._y0 = iy
    def setDT(self, inpt):
        """Set the time step"""
        self._dt = inpt
    def setTheta(self, inpt):
        """Converts the theta from degrees to radians.
        Sets the new value to self._thetaR"""
        theta = inpt
        self._thetaR = theta * np.pi / 180
    def calIVel(self, inpt):
        """Calculate the initial velocity from a list of 
        heights"""
        self._nHeight = [x for x in inpt]
        HeiAvg = stat.mean(self._nHeight)
        self._v0 = np.sqrt(2*9.8*HeiAvg)
        vx = self._v0*np.cos(self._thetaR)
        vy = self._v0*np.sin(self._thetaR)
        self._vx.insert(0, vx)
        self._vy.insert(0, vy)
    def RndNum(self, value, uncertainty):
        new_value = value + (uncertainty*np.random.rand())
        return new_value
    def setUncertainty(self, theta, dy):
        """Sets the uncertainties of the calculation."""
        dHei = np.std(self._nHeight) #standard deviation of the height
        #use standard deviation of the height to calculate the uncertainty of v0
        self._dv0 = np.sqrt(2*9.8*dHei)/(np.sqrt(len(self._nHeight))) 
        dTheta = theta
        #convert to radians
        self._dThetaR = dTheta*np.pi/180 
        self._dy0 = dy
    def method(self):
        while self._y[-1] > 0.0:
        # update the x-position
            self._x.append(self._x[-1] + self._vx[-1] * self._dt)
        # update the y-position
            self._y.append(self._y[-1] + self._vy[-1] * self._dt)
        # update the x-velocity
            self._vx.append(self._vx[-1] + self._ax * self._dt)
        # update the y-velocity
            self._vy.append(self._vy[-1] + self._ay * self._dt)
        # update time
            self._t.append(self._t[-1] + self._dt)
        #ending point
        #self._ranges.append(self._x[-1])
    def uncertainMethod(self):
        angle = self.RndNum(self._thetaR,self._dThetaR)
        velocity = self.RndNum(self._v0, self._dv0)
        height = self.RndNum(self._y0, self._dy0)
        self.t  = [0.0]                       # initial time
        self.x  = [0.0]                       #initial x-position
        self.y  = [height]                    #randomize initial height
        self.vx = [velocity*np.cos(angle)]    #calculate initial x-velocity
        self.vy = [velocity*np.sin(angle)]    #claculate initial y-velocity
        self.method()
        self.updatePlot()
        self._ranges.append(self.x[-1])
        # self.Empty()
    def plot(self):
        """Displays the plotted information."""
        plt.ylabel("y")
        plt.xlabel("x")
        #plt.plot(self._t, self._x, 'r')
        plt.plot(self._t, self._y, 'g')
        plt.show()
    def updatePlot(self):
        """Updates the plot"""
        plt.plot(self.x, self.y)
    def metaData(self):
        """Displays the information about the average
        ranges and their deviation."""
        avgRange = np.mean(self._ranges) #Average landing point in (m)
        dRange = np.std(self._ranges)/(np.sqrt(len(self._ranges))) #deviation of the landing point in (m)
        print(round(avgRange, 3))
        print(round(dRange,3))
    def Empty(self):
        """Empty all the lists used for the simulation.
        (except the self._ranges)"""
        self._t.clear()
        self._x.clear()
        self._y.clear()
        self._vx.clear()
        self._vy.clear()

euler = EulerMethod()
g = 9.8
x0 = 0
y0 = 26.5
dy = 0.1
theta = 60
dtheta = 0.5
dt = 0.05
ax = 0
ay = -g
dt = 0.005
maxY = [155,153,156,157,154,155,155,154,154,155,156,155]

euler.setTheta(theta)
euler.calIVel(maxY)
euler.setAcc(ax, ay)
euler.setI(x0, y0)
euler.setDT(dt)
euler.setUncertainty(dtheta, dy)
for n in range(0,10):
    euler.uncertainMethod()
euler.metaData()
euler.plot()