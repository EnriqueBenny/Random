import math
class Uncertainty:
    def __init__(self):
        pass
    def Addition(a, ua, b, ub):
        c_0 = (a*ua)^2
        c_1 = (b*ub)^2
        c_2 = c_0 + c_1
        c_3 = math.sqrt(c_2)
        return c_3
    def Subtraction():
        pass
    def Division():
        pass
    def Multiplication():
        pass