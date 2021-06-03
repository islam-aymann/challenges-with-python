import unittest

from leetcode._0006_zigzag_conversion import Solution


class TestZigzagConversion(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().convert("PAYPALISHIRING", 3),
                         "PAHNAPLSIIGYIR")
        self.assertEqual(Solution().convert("PAYPALISHIRING", 4),
                         "PINALSIGYAHRPI")
        self.assertEqual(Solution().convert("A", 1),
                         "A")


if __name__ == '__main__':
    unittest.main()
