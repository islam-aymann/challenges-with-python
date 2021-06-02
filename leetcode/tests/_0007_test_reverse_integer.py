import unittest

from leetcode._0007_reverse_integer import Solution


class TestZigzagConversion(unittest.TestCase):
    def test_something(self):
        self.assertEqual(Solution().reverse(123), 321)
        self.assertEqual(Solution().reverse(-123), -321)
        self.assertEqual(Solution().reverse(0), 0)
        self.assertEqual(Solution().reverse(2**31), 8463847412)
        self.assertEqual(Solution().reverse(-2**31), -8463847412)
        self.assertEqual(Solution().reverse(-2**32), 0)
        self.assertEqual(Solution().reverse(2**32), 0)
        self.assertEqual(Solution().reverse(1534236469), 0)


if __name__ == '__main__':
    unittest.main()
