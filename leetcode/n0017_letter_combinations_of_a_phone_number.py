from typing import List


class Solution:
    number_digits = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> List[str]:

        size = len(digits)

        if not size:
            return []
        elif size == 1:
            return self.number_digits[digits[0]]

        prev = self.letterCombinations(digits[:-1])
        additional = self.number_digits[digits[-1]]
        return [s + c for s in prev for c in additional]


if __name__ == "__main__":
    # digits = "237"
    digits = "234"
    # digits = "23"
    # digits = ""
    # digits = "2"

    print(Solution().letterCombinations(digits))
    # print(
    #     1000
    #     * timeit.timeit(
    #         f"Solution().letterCombinations({digits})", number=100000,
    #         globals=globals()
    #     ),
    #     "ms",
    # )
