from distutils import command
import tkinter as tk
from tkinter import *
from tkinter.tix import LabelEntry
class Data:
    """The database for the code, this contains the dictionary."""
    def __init__(self):
        """Initiate the Data class. Stores the data for reference.
        """
        self.data = ""
    def store(self, search):
        """searches the dictionary to get a result.
        Returns
            variables (int/str): contains the information from the dictionary
        """
        """The Various categories need to be organized into names.
        1* Seeds = Seeds costing 50gold from the Southern Merchant. (5 Renown)
        2* Seeds = Seeds costing 100gold from the Southern Merchant. (10 Renown)
        3* Seeds = Seeds costing 300gold from the Southern Merchant. (15 Renown)
        2* Teas = Teas costing 500gold from the Eastern Merchant. (5 Renown, Except: Tea of the Saints)
        3* Teas = Teas costing 1000gold from the Eastern Merchant. (10 Renown)
        4* Teas = Teas costing 1500gold from the Eastern Merchant. (15 Renown)
        Time from 1-99 items = 4.5 seconds
        Time for a loop = 94 seconds
        """
        #{"code": [name, gold, time, renown]}
        materials = {
        "1":["1* Seeds", 19800, 112, 1980],
        "2":["2* Seeds", 29700, 107.5, 2970], 
        "3":["3* Seeds", 207900, 125.5, 10395],
        "4":["2* Teas", 346500, 125.5, 3465],
        "5":["3* Teas", 495000, 116.5, 4950],
        "6":["4* Teas", 445500, 107.5, 4455]
        }
        srch = str(search)
        self.data = materials[srch]
    def name(self):
        """Gets the name from self.data
        Returns:
            name (str): the name of the category.
        """
        name = self.data[0]
        return name
    def gold(self):
        """Gets the gold from self.data
        Returns:
            gold (int): the gold total
        """
        gold = self.data[1]
        return gold
    def time(self):
        """Gets the time from self.data
        Returns:
            time (int): the total time
        """
        tm = self.data[2]
        return tm
    def renown(self):
        """Gets the renown from self.data
        Returns:
            renown (int): the total renown
        """
        renown = self.data[3]
        return renown
    def otpt(self, nm, rnt, rng, glt):
        """displays information to tkinter
        Returns:
            Nothing
        """
        root = tk.Tk()
        name = Label(text=f"Group Name: {nm}", height=2, width=40, font=("Arial", 50))
        name.pack()
        gold = Label(text=f"Renown/Time: {rnt}", height=2, width=40, font=("Arial", 50))
        gold.pack()
        time = Label(text=f"Renown/Gold: {rng}", height=2, width=40, font=("Arial", 50))
        time.pack()
        renown = Label(text=f"Gold/Time: {glt}", height=2, width=40, font=("Arial", 50))
        renown.pack()
        qt = Button(root, text="Next", font=("Arial", 50), command= lambda:root.destroy())
        qt.pack()
        ex = Button(root, text="Exit", font=("Arial", 50), command= lambda:quit())
        ex.pack()
        root.mainloop()
#Data.otpt("", "young", 900, 152, 500)