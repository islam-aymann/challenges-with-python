# Definition for singly-linked list.
from collections import deque
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val

    def printer(self):
        cur = self
        while cur:
            print(cur.val)
            cur = cur.next

    def __str__(self):
        return str(self.val)


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ol = []
        for i in lists:
            node = i
            while node:
                ol.append(node)
                node = node.next

        sl = deque(sorted(ol, key=lambda x: x.val))
        try:
            i = c = sl[0]
        except IndexError:
            return None

        while sl:
            c.next = sl.popleft()
            c = c.next
        c.next = None
        return i


if __name__ == "__main__":
    # lists = [
    #     ListNode(1, ListNode(4, ListNode(5))),
    #     ListNode(1, ListNode(3, ListNode(4))),
    #     ListNode(2, ListNode(6)),
    # ]
    lists = [
        ListNode(1)
    ]

    s = Solution().mergeKLists(lists)
    s.printer()

    # print(
    #     1000
    #     * timeit.timeit(
    #         lambda: Solution().mergeKLists(nodes), number=1, globals=globals()
    #     ),
    #     "ms",
    # )
