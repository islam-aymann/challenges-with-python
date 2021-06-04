import unittest

from leetcode.n0013_roman_to_integer import Solution


class TestRomanToInteger(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().romanToInt("I"), 1)
        self.assertEqual(Solution().romanToInt("II"), 2)
        self.assertEqual(Solution().romanToInt("III"), 3)
        self.assertEqual(Solution().romanToInt("IV"), 4)
        self.assertEqual(Solution().romanToInt("V"), 5)
        self.assertEqual(Solution().romanToInt("IX"), 9)
        self.assertEqual(Solution().romanToInt("LVIII"), 58)
        self.assertEqual(Solution().romanToInt("MCMXCIV"), 1994)
        self.assertEqual(Solution().romanToInt("XL"), 40)
        self.assertEqual(Solution().romanToInt("XC"), 90)
        self.assertEqual(Solution().romanToInt("CD"), 400)
        self.assertEqual(Solution().romanToInt("CM"), 900)
        self.assertEqual(Solution().romanToInt("MMMCMXCIX"), 3999)


if __name__ == "__main__":
    unittest.main()
