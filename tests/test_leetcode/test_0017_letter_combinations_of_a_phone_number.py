import unittest

from leetcode.n0017_letter_combinations_of_a_phone_number import Solution


class TestLetterCombinationsOfAPhoneNumber(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().letterCombinations("23"),
                         ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce",
                          "cf"])
        self.assertEqual(Solution().letterCombinations(""), [])
        self.assertEqual(Solution().letterCombinations("2"), ["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
