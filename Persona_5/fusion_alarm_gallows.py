from locale import DAY_1
import math as mt
class Gallows:
    def __init__(self, name, c, lv, st, ma, en, ag, lu, d1, c1, d2, c2):
        """Initiates the gallows class. 
        Calculates how many Fusion Alarm loops 
        are needed to finish a demon.
        Arguments:
            Name: Name of the Demon
            Cost: Price of demon
            Level: Current level
            Strength: stat current value
            Magic: Stat Current Value
            Endurance: Stat Current Value"""
        self.name = name
        self.cst = c + c1+ c2
        self.level = lv
        self.strength = st
        self.magic = ma
        self.endurance = en
        self.agility = ag
        self.luck = lu
        self.fodder = d1 + ', ' + d2
        lv_lft = 99 - self.level
        self.lv_st = lv_lft * 3
        self.curr_total = st + ma + en + ag + lu
        self.total_stats = 495
        self.total_count = 0

    def otput(self):
        print(self._otput())
        
    def _otput(self):
        left = self.total_stats - self.curr_total - self.lv_st
        num = mt.ceil(left/10)
        otpt = (self.name, num)
        self.total_count = num
        return otpt
    def cost(self):
        print(self._cost())
    def _cost(self):
        num = self.cst * self.total_count
        otpt = (num, self.name, self.fodder)
        return otpt

track = [46301, 49361, 52521, 55781]
rslt = [3060, 3160, 3260, ]

nm = 'Tower: Yoshitsune'
c = (127505 + 44513) / 2
lv = 90
st = 69
ma = 56
en = 55
ag = 60
lu = 53
d1 = 'Emperor: Oberon'
c1 = 26313
d2 = 'Strength: Zaou-Gongen'
c2 = 37450
"""
nm = 'Tower: M. Izanagi Picaro'
c = (127505 + 20405) / 2
lv = 49
st = 44
ma = 44
en = 43
ag = 33
lu = 25
d1 = 'Emperor: Oberon'
c1 = 26313
d2 = 'Strength: Zaou-Gongen'
c2 = 37450
"""
gl = Gallows(nm, c, lv, st, ma, en, ag, lu, d1, c1, d2, c2)
gl.otput()
gl.cost()
