from renown_calculation.data import Data
class Calculate:
    """Takes the data and calculates it for the user."""
    def __init__(self):
        """Initiate the Calculate class."""

    def set_var(self, search):
        """Sets the variables in the __init__ to the searched dictionary item."""
        Data.store(self, search)
        name = Data.name(self)
        gold = Data.gold(self)
        time = Data.time(self)
        renown = Data.renown(self)
        return name, gold, time, renown

    def renown_time(self, renown, time):
        """divides points by time.
        Returns:
            efficiency (int): the efficiency ratio of renown to time.
        """
        ratio = round(renown / time, 2)
        return ratio
    def renown_gold(self, renown, gold):
        """divides renown by gold
        Returns:
            efficiency (int): the efficiency ratio of renown to gold.
        """
        ratio = round(renown / gold, 2)
        return ratio
    def gold_time(self, gold, time):
        """gold by time
        Returns:
            efficiency (int): the efficiency ratio of gold to time.
            """
        ratio = round(gold / time, 2)
        return ratio