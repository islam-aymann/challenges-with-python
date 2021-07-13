import unittest

from leetcode.n0022_generate_parentheses import Solution


class TestGenerateParentheses(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().generateParenthesis(3),
                         ["((()))", "(()())", "(())()", "()(())", "()()()"])
        self.assertEqual(Solution().generateParenthesis(1), ["()"])


if __name__ == '__main__':
    unittest.main()
