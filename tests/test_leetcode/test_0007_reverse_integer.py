import unittest

from leetcode.n0007_reverse_integer import Solution


class TestReverseInteger(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().reverse(123), 321)
        self.assertEqual(Solution().reverse(-123), -321)
        self.assertEqual(Solution().reverse(0), 0)
        self.assertEqual(Solution().reverse(2**31), 0)
        self.assertEqual(Solution().reverse(-2**31), 0)
        self.assertEqual(Solution().reverse(-2**32), 0)
        self.assertEqual(Solution().reverse(2**32), 0)
        self.assertEqual(Solution().reverse(1534236469), 0)


if __name__ == '__main__':
    unittest.main()
