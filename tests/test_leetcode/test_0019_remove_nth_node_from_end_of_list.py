import unittest

from leetcode.n0019_remove_nth_node_from_end_of_list import Solution, ListNode


class TestRemoveNthNodeFromEndOfList(unittest.TestCase):

    def test(self):
        self.assertEqual(
            Solution().removeNthFromEnd1(
                ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
            ),
            ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
        )

        self.assertEqual(Solution().removeNthFromEnd1(ListNode(1), 1), None)

        self.assertEqual(
            Solution().removeNthFromEnd1(ListNode(1, ListNode(2)), 1), ListNode(1)
        )

        self.assertEqual(
            Solution().removeNthFromEnd1(ListNode(1, ListNode(2)), 2), ListNode(2)
        )

        self.assertEqual(
            Solution().removeNthFromEnd1(ListNode(1, ListNode(2, ListNode(3))), 1),
            ListNode(1, ListNode(2)),
        )

        self.assertEqual(
            Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3))), 2),
            ListNode(1, ListNode(3)),
        )

        self.assertEqual(
            Solution().removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3))), 3),
            ListNode(2, ListNode(3)),
        )


if __name__ == "__main__":
    unittest.main()
