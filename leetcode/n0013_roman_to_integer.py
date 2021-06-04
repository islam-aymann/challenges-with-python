import timeit


class Solution:
    def romanToInt1(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number

    def romanToInt2(self, s: str) -> int:
        fixed = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }

        ln = len(s)
        value = 0

        i = 0
        while i < ln:
            c1 = s[i]
            v1 = fixed[c1]

            try:
                v2 = fixed[c1 + s[i + 1]]
                i += 1
            except (ValueError, KeyError, IndexError):
                v2 = None

            value += v2 if v2 else v1

            i += 1
        return value

    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        trans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        for i in reversed(s):  # rev the s
            if trans[i] >= prev:
                res += trans[i]  # sum the value iff previous value same or more
            else:
                res -= trans[
                    i
                ]  # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc
            prev = trans[i]
        return res


if __name__ == "__main__":
    # r = "LVIII"
    # r = "IV"
    r = "MCMXCIV"
    # print(Solution().romanToInt(r))
    print(
        1000
        * timeit.timeit(
            f"Solution().romanToInt1('{r}')", number=100000, globals=globals()
        ),
        "ms",
    )
