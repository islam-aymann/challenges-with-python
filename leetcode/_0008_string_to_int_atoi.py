import re


class Solution:
    def myAtoi1(self, s: str) -> int:
        match = re.match(r' *[-,+]?\d+', s)

        if match:
            num = match.group()

            num = int(num)

            if num < -2 ** 31:
                return -2 ** 31
            elif num > 2 ** 31 - 1:
                return 2 ** 31 - 1

            return num

        return 0

    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        cs = ""
        ln = len(s)

        i = 0
        if s[0] in ["-", "+"]:
            cs += s[0]
            i = 1

        while i < ln and s[i].isdigit():
            cs += s[i]
            i += 1

        try:
            result = int(cs) if cs else 0
        except ValueError:
            result = 0

        if result < -2 ** 31:
            return -2 ** 31
        elif result > 2 ** 31 - 1:
            return 2 ** 31 - 1

        return result


if __name__ == "__main__":
    # x = "42"
    # x = "      -42"
    # x = "4193 with words"
    # x = "words and 987"
    # x = "3.14159"
    # x = ""
    # x = "-5-"
    # x = "+5+"
    # x = "123 456"
    x = "+-1"

    print(Solution().myAtoi(x))
    # print(timeit.timeit(f"Solution().myAtoi(x)",
    #                     number=1000,
    #                     globals=globals()))
