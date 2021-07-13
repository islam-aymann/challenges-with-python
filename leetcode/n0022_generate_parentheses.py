import itertools
import timeit
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if stack:
                    p = stack[-1]
                    if p != "(":
                        break

                    stack.pop()
                else:
                    stack.append(c)
                    break
        return not stack

    def generateParenthesis1(self, n: int) -> List[str]:
        opening = "(" * n
        closing = ")" * n

        results = []
        for i in itertools.permutations(opening + closing):
            result = "".join(i)
            if result not in results and self.isValid(result):
                results.append(result)

        return results

    def generateParenthesis2(self, n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + "(", left - 1, right):
                    yield q
                for q in generate(p + ")", left, right - 1):
                    yield q

        return list(generate("", n, n))

    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + "(", left - 1, right)
            if right > left:
                generate(p + ")", left, right - 1)
            if not right:
                parens += (p,)
            return parens

        return generate("", n, n)


if __name__ == "__main__":
    n = 4
    # n = 1
    # sol = Solution().generateParenthesis1(n)
    # for i in sol:
    #     print(i)

    # enabled = False
    enabled = True
    if enabled:
        print(
            1000
            * timeit.timeit(
                lambda: Solution().generateParenthesis(n),
                number=10000,
                globals=globals(),
            ),
            "ms",
        )
