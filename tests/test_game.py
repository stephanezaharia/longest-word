# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        print(grid)
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list("OQUWRBAZE")
        result=new_game.is_valid('toto')
        self.assertEqual(result,False)


    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list("OQUWRBAZE")
        result=new_game.is_valid('BAROQUE')
        self.assertEqual(result,True)

    def test_empty(self):
        new_game = Game()
        new_game.grid = list("OQUWRBAZE")
        result=new_game.is_valid('')
        self.assertEqual(result,False)

    def test_letter_repeat(self):
        new_game = Game()
        new_game.grid = list("OQUWRBAZE")
        result = new_game.is_valid('BAAOQUE')
        self.assertEqual(result,False)

    def test_random_grid(self):
        new_game = Game()
        print (new_game.grid)
        for letter in new_game.grid:
            if new_game.grid.count(letter)!=1:
                return False
        return True
