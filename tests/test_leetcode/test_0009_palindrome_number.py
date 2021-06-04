import unittest
from leetcode.n0009_palindrome_number import Solution


class TestPalindromeNumber(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().isPalindrome(121), True)
        self.assertEqual(Solution().isPalindrome(-121), False)
        self.assertEqual(Solution().isPalindrome(10), False)
        self.assertEqual(Solution().isPalindrome(-101), False)
        self.assertEqual(Solution().isPalindrome(0), True)


if __name__ == '__main__':
    unittest.main()
