import numpy as np
import matplotlib.pyplot as plt

class T():
    def __init__(self,N=50):
        self.N = N
        self.n = []
    def main(self):
        for i in range(self.N):
            self.n.append(self.Choose(self.N,i)/2**self.N)
        x = [i+1 for i in range(self.N)]
        self.Plot(x)

    def Choose(self, N,n):
        def fact(x):
            f = 1
            if x == 1 or x == 0:
                return f
            for i in range(1,x+1):
                #print(i)
                f *= i
            return f
        return fact(N)/(fact(n)*fact(N-n))
    
    def Plot(self,X):
        plt.plot(X,self.n)
        plt.show()

t = T()
#t.main()

class Ten():
    def __init__(self,N=100000):
        self.N = N
        self.q = 1
        self.X = []
        self.X2 = []
        self.eq22 = []
        self.eqZ = []
    def main(self):
        for i in np.linspace(0.00001,1,100):
            self.X2.append(i)
            self.eqZ.append(self.sharp(i))
        #for i in range(self.N):
            #self.X.append(i)
            #self.eq22.append(self.eq2_2(i))
            #print(self.eq2_2(i))
        
        self.Plot()

    def sharp(self, qa):
        z = qa/self.q
        return (4*z*(1-z))**self.N

        #def eq2_2(self,qa):
        #    qa = qa/(self.q*1000)
        #    qb = self.q - qa
        #    print(qa)
        #    #print(qb)
        #    return ((np.e/self.N)**(2*self.N))*((qa*qb)**self.N)

    def Choose(self, N,n):
        def fact(x):
            f = 1
            if x == 1 or x == 0:
                return f
            for i in range(1,x+1):
                #print(i)
                f *= i
            return f
        return fact(N)/(fact(n)*fact(N-n))
    
    def Plot(self):

        plt.plot(self.X2, self.eqZ, label='Equation Z', color='navy', linewidth=2, linestyle='-')
        plt.title('N=10000', fontsize=12, fontweight='bold', pad=10)
        plt.xlim(0,1)
        #ax2.set_xlabel('X-axis Label (units)', fontsize=11)
        #ax2.set_ylabel('Y-axis Label (units)', fontsize=11)
        plt.legend(loc='best', fontsize=10, frameon=True, shadow=True)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tick_params(axis='both', labelsize=10)        
        plt.legend(loc='best', fontsize=10, frameon=True, shadow=True)
        plt.show()

TT = Ten()
#TT.main()

def Choose(N,n):
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
    # Omega
    print(fact(N)/(fact(n)*fact(N-n)))
    #print(N_a*k*np.log(2))

N = 7
n = 4
Choose(N,n)
