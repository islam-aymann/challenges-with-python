import timeit
from typing import List


class Solution:
    number_digits = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations1(self, digits):
        interpret_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        all_combinations = [''] if digits else []
        for digit in digits:
            current_combinations = list()
            for letter in interpret_digit[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations
        return all_combinations

    def letterCombinations2(self, digits):
        number_digits = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        cmb = [''] if digits else []
        for d in digits:
            cmb = [p + q for p in cmb for q in number_digits[d]]
        return cmb

    def letterCombinations(self, digits: str) -> List[str]:

        size = len(digits)

        if not size:
            return []
        elif size == 1:
            return list(self.number_digits[digits[0]])

        prev = self.letterCombinations(digits[:-1])
        additional = self.number_digits[digits[-1]]
        return [s + c for s in prev for c in additional]


if __name__ == "__main__":
    # digits = "237"
    # digits = "234"
    digits = "23"
    # digits = ""
    # digits = "2"

    # print(Solution().letterCombinations(digits))
    print(
        1000
        * timeit.timeit(
            f"Solution().letterCombinations('{digits}')", number=100000,
            globals=globals()
        ),
        "ms",
    )
