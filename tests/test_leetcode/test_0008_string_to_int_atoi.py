import unittest
from leetcode.n0008_string_to_int_atoi import Solution


class StringToIntAtoi(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().myAtoi("42"), 42)
        self.assertEqual(Solution().myAtoi("      -42"), -42)
        self.assertEqual(Solution().myAtoi("4193 with words"), 4193)
        self.assertEqual(Solution().myAtoi("words and 987"), 0)
        self.assertEqual(Solution().myAtoi("-91283472332"), -2147483648)
        self.assertEqual(Solution().myAtoi("+123"), 123)
        self.assertEqual(Solution().myAtoi("3.14159"), 3)
        self.assertEqual(Solution().myAtoi(""), 0)
        self.assertEqual(Solution().myAtoi(" "), 0)
        self.assertEqual(Solution().myAtoi("+"), 0)
        self.assertEqual(Solution().myAtoi("21474836460"), 2147483647)
        self.assertEqual(Solution().myAtoi("-5-"), -5)
        self.assertEqual(Solution().myAtoi("+5+"), 5)


if __name__ == '__main__':
    unittest.main()
