import timeit


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printer(self):
        cur = self
        while cur:
            print(cur.val)
            cur = cur.next

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        if isinstance(other, ListNode):
            if other:
                return self.val == other.val
            else:
                return False
        else:
            return self.val == other


class Solution:
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:

        if not head:
            return

        if not head.next:
            return

        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        nodes.pop(-n)

        head = ListNode(nodes[0])
        cur = head
        for i in nodes[1:]:
            cur.next = ListNode(i)
            cur = cur.next

        return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        if not head:
            return

        if not head.next:
            return

        l = head
        t = head
        h = head
        m = -n

        while h:

            if not m:
                l = t
                t = t.next
            else:
                m += 1

            h = h.next

        if t is head:
            return head.next

        l.next = t.next

        return head


if __name__ == "__main__":
    head, n = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
    # head, n = ListNode(1), 1
    # head, n = ListNode(1, ListNode(2)), 1
    # head, n = ListNode(1, ListNode(2)), 2
    # head, n = ListNode(1, ListNode(2, ListNode(3))), 1
    # head, n = ListNode(1, ListNode(2, ListNode(3))), 2
    # head, n = ListNode(1, ListNode(2, ListNode(3))), 3
    # sol = Solution().removeNthFromEnd(head, n)
    # if sol:
    #     sol.printer()

    print(
        1000
        * timeit.timeit(
            lambda: Solution().removeNthFromEnd(head, n), number=100000,
            globals=globals()
        ),
        "ms",
    )
