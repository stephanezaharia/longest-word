"""
This is the longest word implementation class
"""

import random
import string

class Game:
    """ This is the longest word implementation class
    """

    def __init__(self):
        """ This is the longest word implementation class
        """
        self.random_grid()
        print(self.grid)

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
        for letter in self.grid:
            cnt = word.count(letter)
            #print(letter,cnt)
            if cnt > 1:
                return False
        for letter in word:
            if letter not in self.grid:
                return False
        return True
