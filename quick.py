import matplotlib.pyplot as plt
import numpy as np
from numpy import arange, array


class Plotter():
    def __init__(self):
        self.a = 0.141
        self.b = 3.91
        self.R = 8.314
        self.T = np.arange(100, 600, 1)
    def main(self):
        grid = self.Cal()
        self.Plot(grid)

    def Cal(self):
        return self.b - (self.a/(self.R*self.T))
    def Plot(self,grid):
        plt.plot(grid)
        plt.show()

p = Plotter()
p.main()