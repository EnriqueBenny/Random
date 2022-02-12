from renown_calculation.calculate import Calculate
from renown_calculation.data import Data
class Director:
    """Director class, represents user."""
    def __init__(self):
        """initiates the Dirctor class to represent the user.
        """
        self.name = ""
        self.gold = 0
        self.time = 0
        self.renown = 0
        self.rnwn_tm = 0
        self.rnwn_gld = 0
        self.gld_tm = 0
        self.counter = 1
    def start(self):
        """starts the code"""
        while self.counter < 7:
            self.search()
            self.update()
            self.send()

    def search(self):
        """searches for the different values
        Returns:
            Nothing
        """
        data = Calculate.set_var(self, self.counter)
        self.name = data[0]
        self.gold = data[1]
        self.time = data[2]
        self.renown = data[3]

    def update(self):
        """updates the self values"""
        self.rnwn_tm = Calculate.renown_time(self, self.renown, self.time)
        self.rnwn_gld = Calculate.renown_gold(self, self.renown, self.gold)
        self.gld_tm = Calculate.gold_time(self, self.gold, self.time)

    def send(self):
        """sends everything to tkinter to output"""
        Data.otpt(self, self.name, self.rnwn_tm, self.rnwn_gld, self.gld_tm, self.gold)
        self.counter += 1