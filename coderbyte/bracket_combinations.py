import itertools

# brute-force O(2^n)
from math import factorial


def bracket_combinations1(num):
    if not num or num == "1":
        return num

    try:
        num = int(num)
    except ValueError:
        return 0

    bracket_list = num * ["(", ")"]
    all_comb = set(["".join(perm) for perm in
                    itertools.permutations(bracket_list)
                    if (perm[0], perm[-1]) == ("(", ")")])

    new_comb = list()
    for i, comb in enumerate(all_comb):
        stack = list()
        for j, char in enumerate(comb):
            if char == "(":
                stack.append(char)
            else:
                if not stack:
                    break

                stack.pop()
        if not stack and j == len(comb) - 1:
            new_comb.append(comb)

    return len(new_comb)


# backtracking
def bracket_combinations2(num):
    try:
        num = int(num)
    except ValueError:
        return 0

    if not num or num == 1:
        return 1

    ans_list = list()
    _bracket_combinations2(ans_list, "", 0, 0, num)

    return len(ans_list)


# factorial
def bracket_combinations3(num):
    return int(factorial(2 * num) /
               (factorial(num + 1) * factorial(num)))


def _bracket_combinations2(ans_list, combo, num_open, num_close, n):
    if len(combo) == 2 * n:
        ans_list.append(combo)
        return

    if num_open < n:
        _bracket_combinations2(ans_list,
                               combo + "(",
                               num_open + 1,
                               num_close,
                               n)

    if num_close < num_open:
        _bracket_combinations2(ans_list,
                               combo + ")",
                               num_open,
                               num_close + 1,
                               n)


if __name__ == '__main__':
    print(bracket_combinations3(3))
