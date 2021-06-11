import unittest

from leetcode.n0018_4_sum import Solution


class Test4Sum(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().fourSum([1, 0, -1, 0, -2, 2], 0),
                         [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
        self.assertEqual(Solution().fourSum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]])
        self.assertEqual(Solution().fourSum([-3, -1, 0, 2, 4, 5], 2), [[-3, -1, 2, 4]])


if __name__ == '__main__':
    unittest.main()
