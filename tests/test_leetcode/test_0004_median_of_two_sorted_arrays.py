import unittest

from leetcode.n0004_median_of_two_sorted_arrays import Solution


class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().findMedianSortedArrays([1, 3], [2]), 2.0)
        self.assertEqual(Solution().findMedianSortedArrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(Solution().findMedianSortedArrays([0, 0], [0, 0]), 0)
        self.assertEqual(Solution().findMedianSortedArrays([], [1]), 1)
        self.assertEqual(Solution().findMedianSortedArrays([2], []), 2.0)


if __name__ == "__main__":
    unittest.main()
