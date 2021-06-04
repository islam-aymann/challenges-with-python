import timeit


class Solution:
    def reverse1(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2 ** 31) - 1 < rst < 2 ** 31 else 0

    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        if sign == -1:
            x *= -1
        result = int(str(x)[::-1]) * sign
        if not -2 ** 31 <= result <= 2 ** 31:
            return 0
        return result


if __name__ == "__main__":
    x = 123  # 0.0005626999999999993
    # x = -123
    # x = 120
    # x = 0
    # x = 2**31
    # x = -2**31

    print(Solution().reverse(x))
    print(timeit.timeit(f"Solution().reverse(x)",
                        number=1000,
                        globals=globals()))
