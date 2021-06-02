import itertools
from collections import defaultdict


class Solution:
    def convert1(self, s: str, numRows: int) -> str:
        zigzags = defaultdict(str)
        pattern = list(range(numRows)) + list(range(numRows - 2, 0, -1))

        i = 0
        for p in itertools.cycle(pattern):
            zigzags[p] += s[i]
            i += 1
            if i >= len(s):
                break
        return ''.join(zigzags.values())

    def convert2(self, s: str, numRows: int) -> str:
        rows = ['' for i in range(numRows)]

        pattern = list(range(numRows)) + list(range(numRows - 2, 0, -1))

        i = 0
        for p in itertools.cycle(pattern):
            rows[p] += s[i]
            i += 1
            if i >= len(s):
                break
        return ''.join(rows)

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return ''.join(L)


if __name__ == "__main__":
    s = "PAYPALISHIRING", 3
    # s = "aaaabbaa", 4
    # s = "A", 1
    print(Solution().convert(*s))
    # print(timeit.timeit(f"Solution().convert({s})",
    #                     number=1000,
    #                     globals=globals()))
