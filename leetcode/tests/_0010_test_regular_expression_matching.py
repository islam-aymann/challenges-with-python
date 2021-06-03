import unittest

from leetcode._0010_regular_expression_matching import Solution


class TestRegularExpressionMatching(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().isMatch("aa", "a"), False)
        self.assertEqual(Solution().isMatch("aa", "a*"), True)
        self.assertEqual(Solution().isMatch("ab", ".*"), True)
        self.assertEqual(Solution().isMatch("aab", "c*a*b"), True)
        self.assertEqual(Solution().isMatch("mississippi",
                                            "mis*is*p*."), False)
        self.assertEqual(Solution().isMatch("ab", ".*c"), False)
        self.assertEqual(Solution().isMatch("aaa", "a*a"), True)
        self.assertEqual(Solution().isMatch("aaa", "ab*a*c*a"), True)


if __name__ == "__main__":
    unittest.main()
