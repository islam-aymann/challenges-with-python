def BracketCombinations(num):
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


if __name__ == '__main__':
    print(BracketCombinations(2))
