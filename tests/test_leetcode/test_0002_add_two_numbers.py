import unittest

from leetcode.n0002_add_two_numbers import Solution, ListNode


class TestAddTwoNumbers(unittest.TestCase):
    def test(self):
        self.assertEqual(
            Solution().addTwoNumbers(
                ListNode(2, ListNode(4, ListNode(3))),
                ListNode(5, ListNode(6, ListNode(4))),
            ),
            ListNode(7, ListNode(0, ListNode(8))),
        )

        self.assertEqual(
            Solution().addTwoNumbers(ListNode(0), ListNode(0)), ListNode(0)
        )

        self.assertEqual(
            Solution().addTwoNumbers(
                ListNode(
                    9,
                    ListNode(
                        9,
                        ListNode(
                            9,
                            ListNode(
                                9,
                                ListNode(
                                    9,
                                    ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
                                ),
                            ),
                        ),
                    ),
                ),
                ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
            ),
            ListNode(
                8,
                ListNode(
                    9,
                    ListNode(
                        9,
                        ListNode(
                            9,
                            ListNode(0, ListNode(0, ListNode(0, ListNode(1)))),
                        ),
                    ),
                ),
            ),
        )


if __name__ == "__main__":
    unittest.main()
