import unittest

from leetcode.n0020_valid_parentheses import Solution


class TestValidParentheses(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().isValid("{}"), True)
        self.assertEqual(Solution().isValid("()[]{}"), True)
        self.assertEqual(Solution().isValid("(]"), False)
        self.assertEqual(Solution().isValid("([)]"), False)
        self.assertEqual(Solution().isValid("]"), False)


if __name__ == '__main__':
    unittest.main()
