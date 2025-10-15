import numpy as np
import matplotlib.pyplot as plt

# Collaboration between Erik Benson and Jarom Peterson

class Box():
    def __init__(self):
        #self.N = 50
        self.N = 1000
        self.n = self.N
        self.box = np.array([self.N,0])
        self.t = np.arange(0,50000,1)
        # Box 1
        self.X = []
        # Box 2
        self.Y = []
        # Relative variance
        self.Z = []

    def main(self):
        def random():
            return np.random.default_rng().random()
        def move(r):
            if r < self.n/self.N:
                self.box[0] -= 1
                self.box[1] += 1
            else:
                self.box[0] += 1
                self.box[1] -= 1
        for i in self.t:
            move(random())
            self.n = self.box[0]
            # The left box
            self.X.append(self.box[0])
            # The right box
            self.Y.append(self.box[1])
            # The variance
            n_avg = np.mean(self.X)
            sigma2 = np.var(self.X)
            sigma = np.sqrt(sigma2)
            self.Z.append(sigma/n_avg)
        #self.Plot(self.X)
        #self.Plot(self.Y)
        self.Plot(self.Z)

    def Plot(self,B):
        plt.plot(self.t,B)
        plt.show()

B = Box()
B.main()