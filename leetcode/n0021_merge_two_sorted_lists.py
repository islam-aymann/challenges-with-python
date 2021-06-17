import timeit


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        cur = self
        while cur:
            yield cur.val
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
    def who_is_smaller(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val < l2.val:
                return l1
            elif l1.val > l2.val:
                return l2
            return l1

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        elif l1 is None or l2 is None:
            return l1 or l2

        cl1 = l1
        cl2 = l2
        l3 = self.who_is_smaller(cl1, cl2)
        cl3 = l3

        if l3 == l1:
            cl1 = cl1.next
        else:
            cl2 = cl2.next

        while cl1 or cl2:
            if self.who_is_smaller(cl1, cl2) is cl1:
                cl3.next = cl1
                cl1 = cl1.next
            else:
                cl3.next = cl2
                cl2 = cl2.next

            cl3 = cl3.next
        return l3

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        elif l1 is None or l2 is None:
            return l1 or l2

        cl1 = l1
        cl2 = l2

        if l1.val < l2.val:
            cl3 = l3 = l1
            cl1 = l1.next
        else:
            cl3 = l3 = l2
            cl2 = l2.next

        while cl1 or cl2:

            if cl2 is None:
                cl3.next = cl1
                cl1 = cl1.next

            elif cl1 is None:
                cl3.next = cl2
                cl2 = cl2.next

            elif cl1.val < cl2.val:
                cl3.next = cl1
                cl1 = cl1.next

            else:
                cl3.next = cl2
                cl2 = cl2.next

            cl3 = cl3.next
        return l3


if __name__ == "__main__":
    l = ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))
    # l = None, ListNode(1, ListNode(3, ListNode(4)))
    # l = ListNode(1, ListNode(2, ListNode(4))), None
    # l = None, None

    sol = Solution().mergeTwoLists(*l)
    print(list(sol))

    enabled = False
    # enabled = True

    if enabled:
        print(
            1000
            * timeit.timeit(
                lambda: Solution().mergeTwoLists(*l), number=1,
                globals=globals()
            ),
            "ms",
        )
