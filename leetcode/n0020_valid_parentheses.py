import timeit


class Solution:
    def isValid1(self, s: str) -> bool:
        while len(s) > 0:
            size = len(s)
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
            new_size = len(s)
            if size == new_size:
                return False
        return True

    def isValid2(self, s: str) -> bool:
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]

        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if stack:
                    p = stack[-1]
                    if opening.index(p) != closing.index(c):
                        break

                    stack.pop()
                else:
                    stack.append(c)
                    break
        return not stack

    def isValid(self, s: str) -> bool:
        # This is a faster solution but leetcode hardly gives it the same rating as
        # the previous one

        opening = ["(", "{", "["]

        lookup = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if stack:
                    p = stack[-1]
                    if p != lookup[c]:
                        break

                    stack.pop()
                else:
                    stack.append(c)
                    break
        return not stack


if __name__ == '__main__':
    # s = "()"
    s = "()[]{}"
    # s = "(]"
    # s = "([)]"
    # s = "([)]"
    # s = "]"
    # print(Solution().isValid(s))

    print(
        1000
        * timeit.timeit(
            lambda: Solution().isValid(s), number=100000,
            globals=globals()
        ),
        "ms",
    )
