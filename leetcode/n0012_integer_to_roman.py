import timeit


class Solution:
    def intToRoman1(self, num: int) -> str:
        fixed = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        try:
            return fixed[num]
        except KeyError:
            pass

        fixed_items = list(fixed.items())
        roman = ""
        i = len(fixed_items) - 1
        while i > -1:
            m = fixed_items[i][0]
            if m <= num:
                sub = num - m
                if sub > -1:
                    num = sub
                    roman += fixed_items[i][1]
                else:
                    i -= 1
            else:
                i -= 1

        return roman

    def intToRoman2(self, num: int) -> str:
        fixed = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        try:
            return fixed[num]
        except KeyError:
            pass

        roman = ""
        fixed_list = []
        for i in fixed:
            if i > num:
                break

            fixed_list.append((i, fixed[i]))

        while num:
            m = fixed_list.pop()
            sub = num - m[0]
            while sub >= 0:
                num = sub
                sub = num - m[0]
                roman += m[1]

        return roman

    def intToRoman3(self, num: int) -> str:
        fixed = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        if fixed.get(num):
            return fixed[num]

        roman = ""
        fixed_list = []
        for i in fixed:
            if i > num:
                break

            fixed_list.append((i, fixed[i]))

        for i in reversed(fixed_list):
            m = i[0]
            sub = num - m
            while sub >= 0:
                num = sub
                sub = num - m
                roman += i[1]

        return roman

    def intToRoman(self, num: int) -> str:
        fixed = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        roman = ""
        for k in fixed:
            if k > num:
                continue
            sub = num - k
            while sub >= 0:
                num = sub
                sub = num - k
                roman += fixed[k]

        return roman


if __name__ == "__main__":
    n = 6
    # print(Solution().intToRoman(n))
    print(1000 * timeit.timeit(f"Solution().intToRoman({n})", number=100000,
                               globals=globals()), "ms")
