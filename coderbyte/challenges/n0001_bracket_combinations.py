import timeit
from math import factorial



def BracketCombinations1(num):
    def _bracket_combinations(ans_list, combo, num_open, num_close, n):
        if len(combo) == 2 * n:
            ans_list.append(combo)
            return

        if num_open < n:
            _bracket_combinations(ans_list,
                                  combo + "(",
                                  num_open + 1,
                                  num_close,
                                  n)

        if num_close < num_open:
            _bracket_combinations(ans_list,
                                  combo + ")",
                                  num_open,
                                  num_close + 1,
                                  n)

    try:
        num = int(num)
    except ValueError:
        return 0

    if not num or num == 1:
        return 1

    result = list()
    _bracket_combinations(result, '', 0, 0, num)
    return len(result)


def BracketCombinations(num):
    # https://en.wikipedia.org/wiki/Catalan_number
    num = factorial(2 * num) // (factorial(num + 1) * factorial(num))
    return num


def factorial1(n):
    if n == 1:
        return 1
    return n * factorial1(n - 1)


def factorial2(n):
    for i in range(n - 1, 1, -1):
        n *= n - 1

    return n


if __name__ == '__main__':
    print(1000*timeit.timeit(lambda: BracketCombinations(3), number=100000, globals=globals()))
