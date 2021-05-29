class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"LN: {self.val}"


class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     d3 = list()
    #
    #     d3.append(l1.val)
    #     while l1.next:
    #         d3.append(l1.next.val)
    #         l1 = l1.next
    #
    #     d1 = int("".join([str(d3.pop()) for i in range(len(d3))]))
    #
    #     d3.append(l2.val)
    #     while l2.next:
    #         d3.append(l2.next.val)
    #         l2 = l2.next
    #
    #     d2 = int("".join([str(d3.pop()) for i in range(len(d3))]))
    #
    #     ls = [ListNode(int(i)) for i in str(d1 + d2)[::-1]]
    #
    #     for i, n in enumerate(ls[:-1]):
    #         n.next = ls[i + 1]
    #
    #     return ls[0]
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = l1.val + l2.val
        l3 = ListNode(s if s < 10 else s - 10)
        li = l3
        r = 1 if s >= 10 else 0

        while l1.next is not None or l2.next is not None or r:
            try:
                s1 = l1.next.val
            except AttributeError:
                s1 = 0

            try:
                s2 = l2.next.val
            except AttributeError:
                s2 = 0

            s = s1 + s2 + r

            li.next = ListNode(s if s < 10 else s - 10)

            r = 1 if s >= 10 else 0

            if l1.next:
                l1 = l1.next

            if l2.next:
                l2 = l2.next

            li = li.next

        return l3


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))

    l2 = ListNode(5, ListNode(6))
    print(Solution().addTwoNumbers(l1, l2))
    # print(timeit.timeit(f"Solution().addTwoNumbers({l1}, {l2})",
    #                     number=10000,
    #                     globals=globals()))
