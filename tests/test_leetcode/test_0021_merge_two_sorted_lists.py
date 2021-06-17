import unittest

from leetcode.n0021_merge_two_sorted_lists import Solution, ListNode


class TestMergeTwoSortedLists(unittest.TestCase):
    def test(self):
        self.assertEqual(
            Solution().mergeTwoLists(
                ListNode(1, ListNode(2, ListNode(4))),
                ListNode(1, ListNode(3, ListNode(4))),
            ),
            ListNode(1,
                     ListNode(1,
                              ListNode(2,
                                       ListNode(3,
                                                ListNode(4,
                                                         ListNode(4)))))
                     ),
        )
        self.assertEqual(Solution().mergeTwoLists(None, ListNode(0)), ListNode(0))
        self.assertEqual(Solution().mergeTwoLists(None, None), None)


if __name__ == "__main__":
    unittest.main()
