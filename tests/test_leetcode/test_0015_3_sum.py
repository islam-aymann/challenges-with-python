import unittest

from leetcode.n0015_3_sum import Solution


class Test3Sum(unittest.TestCase):
    def test(self):
        self.assertEqual(
            Solution().threeSum([-1, 0, 1, 2, -1, -4]),
            [[-1, -1, 2], [-1, 0, 1]]
        )
        self.assertEqual(
            Solution().threeSum([]),
            []
        )

        self.assertEqual(
            Solution().threeSum([0]),
            []
        )


if __name__ == "__main__":
    unittest.main()
