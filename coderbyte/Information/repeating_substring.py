def smallest_repeating_substring(inputv):
    total_size = len(inputv)
    current_size = 1
    while current_size < total_size:
        seq = inputv[0: current_size]
        remaining = total_size - current_size
        mul = remaining // current_size

        if (mul + 1) * seq == inputv:
            return seq

        current_size += 1

    return inputv


def pattern(inputv):
    pattern_end = 0
    for j in range(pattern_end + 1, len(inputv)):

        pattern_dex = j % (pattern_end + 1)
        if inputv[pattern_dex] != inputv[j]:
            pattern_end = j
            continue

        if j == len(inputv) - 1:
            print(pattern_end)
            return inputv[0:pattern_end + 1]
    return inputv


def pattern2(inputv):
    if not inputv:
        return inputv

    nxt = [0] * len(inputv)
    for i in range(1, len(nxt)):
        k = nxt[i - 1]
        while True:
            if inputv[i] == inputv[k]:
                nxt[i] = k + 1
                break
            elif k == 0:
                nxt[i] = 0
                break
            else:
                k = nxt[k - 1]

    small_piece_len = len(inputv) - nxt[-1]
    if len(inputv) % small_piece_len != 0:
        return inputv

    return inputv[0:small_piece_len]


# largest repeating sequence
def MathChallenge(strParam):
    if len(strParam) == 1:
        return -1

    total_size = len(strParam)
    current_size = 1

    possible_seqs = list()
    while current_size < total_size:
        seq = strParam[0: current_size]

        remaining = total_size - current_size
        mul = remaining // current_size

        if (mul + 1) * seq == strParam:
            possible_seqs.append(seq)

        current_size += 1

    return possible_seqs[-1] if possible_seqs else -1


if __name__ == '__main__':
    print(smallest_repeating_substring('abkebabkebabkeb'))
    print(MathChallenge('abkebabkebabkeb'))
    # print(pattern('abkebabkebabkeb'))
    # print(pattern2('abkebabkebabkeb'))
