import numpy as np
import random as rand
import matplotlib.pyplot as plt


class Flipper():
    def __init__(self, coins=20):
        self.coins = coins
        self.arr = np.ones(coins, dtype=int)
        self.tail = np.zeros(coins, dtype=int)
        self.X = [] # Counts the number of flips
        self.Y = [] # Holds the number of heads
        self.Z = [] # Holds the number of tails/Entropy
    def main(self, f):
        for i in range(f):
            self.fliph(self.D20())
            #self.flipt(self.D20())
            self.X.append(i)
            #self.Y.append(np.sum(self.arr))
            z=self.Choose(self.coins,np.sum(self.arr))
            self.Y.append(z)
            #self.Z.append(np.sum(self.tail))
        self.Plot()
    def D20(self):
        return rand.randint(0,self.coins-1)
    def fliph(self, x):
        if self.arr[x] == 1:
            self.arr[x] = 0
        elif self.arr[x] == 0:
            self.arr[x] = 1
    def flipt(self, x):
        if self.tail[x] == 1:
            self.tail[x] = 0
        elif self.tail[x] == 0:
            self.tail[x] = 1
    def Choose(self,N,n):
        def fact(x):
            f = 1
            if x == 1 or x == 0:
                return f
            for i in range(1,x+1):
                #print(i)
                f *= i
            return f
        k=1.381e-23
        kev = 8.617e-5
        N_a = 6.022e23
        # Entropy
        #print(1*np.log(fact(N)/(fact(n)*fact(N-n))))
        return np.log(fact(N)/(fact(n)*fact(N-n)))
    def Plot(self):
        plt.plot(self.X,self.Y)
        #plt.plot(self.X,self.Z)
        plt.ylim(0,200)
        plt.show()

f = Flipper(coins=200)
f.main(500)