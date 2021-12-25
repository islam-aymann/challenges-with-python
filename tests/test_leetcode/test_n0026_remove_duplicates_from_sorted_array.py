import unittest

from leetcode.n0026_remove_duplicates_from_sorted_array import Solution


class TestRemoveDuplicatesFromSortedArray(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)


if __name__ == "__main__":
    unittest.main()
