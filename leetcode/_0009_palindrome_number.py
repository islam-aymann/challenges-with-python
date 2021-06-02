class Solution:
    def isPalindrome1(self, x: int) -> bool:
        sx = str(x)
        return sx == sx[::-1]

    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        i = 0
        j = len(sx) - 1

        while i <= j and sx[i] == sx[j]:
            i += 1
            j -= 1

        return i > j


if __name__ == "__main__":
    # x = 101
    # x = 111
    # x = 121
    # x = 12344321
    x = -100

    print(Solution().isPalindrome(x))
    # print(timeit.timeit(f"Solution().myAtoi(x)",
    #                     number=1000,
    #                     globals=globals()))
