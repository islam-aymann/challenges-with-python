import timeit
from typing import List


class Solution:
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        prefix = ""
        ci = 0
        m = len(min(strs, key=lambda s: len(s)))
        while ci < m:
            c = strs[0][ci]
            for st in strs[1:]:
                if st[ci] != c:
                    ci = float('inf')
                    break
            if ci != float('inf'):
                prefix += c
            ci += 1
        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for tup in zip(*strs):
            if len(set(tup)) != 1:
                break
            else:
                prefix += tup[0]

        return prefix


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))
    # print(
    #     1000
    #     * timeit.timeit(
    #         f"Solution().longestCommonPrefix({strs})", number=15000,
    #         globals=globals()
    #     ),
    #     "ms",
    # )
