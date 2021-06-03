import unittest

from leetcode._0003_longest_subsring_without_repeating_characters import \
    Solution


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(Solution().lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring(""), 0)


if __name__ == '__main__':
    unittest.main()
