import unittest

from leetcode.n0023_merge_k_sorted_lists import Solution, ListNode


class TestMergeKSortedLists(unittest.TestCase):
    def test(self):
        self.assertEqual(
            Solution().mergeKLists(
                [
                    ListNode(1, ListNode(4, ListNode(5))),
                    ListNode(1, ListNode(3, ListNode(4))),
                    ListNode(2, ListNode(6)),
                ]
            ),
            ListNode(
                1,
                ListNode(
                    1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
                ),
            ),
        )
        self.assertEqual(Solution().mergeKLists([]), None)
        self.assertEqual(Solution().mergeKLists([[]]), None)
        self.assertEqual(Solution().mergeKLists([ListNode(1)]), ListNode(1))


if __name__ == "__main__":
    unittest.main()
