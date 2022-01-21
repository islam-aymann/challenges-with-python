import unittest

from coderbyte.challenges.n0001_bracket_combinations import BracketCombinations


class TestBracketCombinations(unittest.TestCase):
    def test(self):
        self.assertEqual(BracketCombinations(1), 1)
        self.assertEqual(BracketCombinations(2), 2)
        self.assertEqual(BracketCombinations(3), 5)
