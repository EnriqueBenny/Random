import math

def rt_bisection(v1):
    'perform root bisection'
    while v1 > 1:
        pass
# 1 is the proton heading to the right
# 2 is the duteron heading to the left
# Velocities
v1= .94
v2= .59
# Gammas
g1 = 1/((1-((v1*3*10**8)/(3*10**8)))**(1/2))
g2 = 1/((1-((v2*3*10**8)/(3*10**8)))**(1/2))
# Masses
m1 = 1.673*10**-27
m2 = 3.344*10**-27
# Since we have known values that can become a single number, 
# they have been combined into variable a.
a = g1*m1 + g2*m2
