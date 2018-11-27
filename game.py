# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string
import requests

class Game:
    """ This is the longest word implementation class
    """

    def __init__(self):
        """ This is the longest word implementation class
        """
        self.random_grid()

    def random_grid(self):
        """ add a random grid in object. Make sure every letter appears once
        """
        self.grid = []
        for _ in range(0, 9):
            again = True
            while again:
                letter = random.choice(string.ascii_uppercase)
                if letter not in self.grid:
                    again = False
                    self.grid.append(letter)

    def is_valid(self, word):
        """  This is the longest word check function
        """
        if not word or len(word) > len(self.grid):
            return False

        try:
            r = requests.get('https://wagon-dictionary.herokuapp.com/'+word)
            if not r.json()["found"]:
                return False
        except:
            return False

        for letter in word:
            cnt = word.count(letter)
            cntmax = self.grid.count(letter)
            if letter not in self.grid or cnt>cntmax:
                print ("wrong",letter)
                return False

        return True
