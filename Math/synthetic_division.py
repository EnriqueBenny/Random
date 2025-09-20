import math
import numpy as np
from fractions import Fraction as frac
from decimal import Decimal as deci
def SyntheticDivision(d, x1, x2, x3, x4, x5, x6):
    result = []
    result.append(d)
    result.append(x1)
    r1 = x1 * d
    r2 = x2 + r1
    result.append(r2)
    r3 = r2 * d
    r4 = r3 + x3
    result.append(r4)
    r5 = r4 * d
    r6 = r5 + x4
    result.append(r6)
    if x5 != None:
        r7 = r6 * d
        r8 = r7 + x5
        result.append(r8)
    if x6 != None:
        r9 = r8 * d
        r10 = r9 + x6
        result.append(r10)
    print(result)
def QuadraticEquation(a, b, c):
    result = []
    b1 = -b
    b2 = b^2
    b3 = 4 * a * c
    b4 = b2 - b3
    d = 2 * a
    if DetermineNegative(b4) == True:
        b5 = b4 * -1
        s = round(np.sqrt(b5),2)
        rslt1 = (b1 + s) / d
        rslt2 = round(rslt1, 1)
        result.append(rslt2)
        result.append("i")
        rslt1 = (b1 - s) / d
        rslt2 = round(rslt1, 1)
        result.append(rslt2)
        result.append("i")
    elif DetermineNegative(b4) == False:
        s = round(np.sqrt(b4),2)
        rslt1 = (b1 + s) / d
        rslt2 = round(rslt1, 1)
        result.append(rslt2)
        rslt1 = (b1 - s) / d
        rslt2 = round(rslt1, 1)
        result.append(rslt2)
    print(result)
    for i in result:
        if i == "i":
            continue
        l = frac(deci(f'{i}'))
        print(l)
def RationalRoots(x, y):
    z = []    
    for i in x:
        z.append(i*-1)
        o = i
        for i in y:
            z.append(o/i)
            z.append(o/i*-1)
    for i in z:
        if i not in x:
            d.append(i)
def DetermineNegative(x):
    if x >= 0:
        return False
    if x < 0:
        return True

#Factors of the Constant
d = [1,7]
#Leading Coefficient
lc = [1,3,5,15]
#Places in the synthetic division
x1 = -15
x2 = 16
x3 = 0
x4 = 0
x5 = 7
x6 = None


if x4 != None:
    RationalRoots(d, lc)
    for i in d:
        SyntheticDivision(i, x1, x2, x3, x4, x5, x6)
    quit
elif x4 == None:
    QuadraticEquation(x1, x2, x3)