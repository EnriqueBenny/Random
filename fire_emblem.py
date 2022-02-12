from cgitb import reset
from urllib.parse import DefragResult



class Stats():
    def __init__(self):
        """tracks the stats in the game"""
        self.Str = 0
        self.Mag = 0
        self.Dex = 0
        self.Spd = 0
        self.Lck = 0
        self.Def = 0
        self.Res = 0
        self.Cha = 0
    
    def increment(self):
        """increase the stats in the init"""
        print("Str(1), Mag(2), Dex(3), Spd(4), Lck(5), Def(6), ")
        nav = int(input("Which Stat do you want to increase? "))
