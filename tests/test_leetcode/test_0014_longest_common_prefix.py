import unittest

from leetcode.n0014_longest_common_prefix import Solution


class TestLongestCommonPrefix(unittest.TestCase):
    def test(self):
        self.assertEqual(
            Solution().longestCommonPrefix(
                [
                    "flower",
                    "flow",
                    "flight",
                ]
            ),
            "fl",
        )

        self.assertEqual(
            Solution().longestCommonPrefix(
                [
                    "dog",
                    "racecar",
                    "car",
                ]
            ),
            "",
        )


if __name__ == "__main__":
    unittest.main()
