import unittest

from leetcode._0001_two_sum import Solution


class TestTwoSum(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(Solution().twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(Solution().twoSum([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()
