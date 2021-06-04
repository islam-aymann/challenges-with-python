import unittest

from leetcode.n0012_integer_to_roman import Solution


class TestIntegerToRoman(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().intToRoman(1), "I")
        self.assertEqual(Solution().intToRoman(2), "II")
        self.assertEqual(Solution().intToRoman(3), "III")
        self.assertEqual(Solution().intToRoman(4), "IV")
        self.assertEqual(Solution().intToRoman(5), "V")
        self.assertEqual(Solution().intToRoman(9), "IX")
        self.assertEqual(Solution().intToRoman(58), "LVIII")
        self.assertEqual(Solution().intToRoman(1994), "MCMXCIV")
        self.assertEqual(Solution().intToRoman(40), "XL")
        self.assertEqual(Solution().intToRoman(90), "XC")
        self.assertEqual(Solution().intToRoman(400), "CD")
        self.assertEqual(Solution().intToRoman(900), "CM")
        self.assertEqual(Solution().intToRoman(3999), 'MMMCMXCIX')


if __name__ == "__main__":
    unittest.main()
