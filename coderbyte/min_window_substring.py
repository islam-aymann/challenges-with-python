from collections import Counter


def min_window_substring(str_list):
    string = str_list[0]
    required = str_list[1]

    if required == string:
        return required
    return _min_window_substring(len(required), required, string)


def _min_window_substring(size, required, string):
    start = 0
    end = start + size
    while end <= len(string):
        window = string[start: end]

        if required == window:
            return window

        matches = 0
        new_window = window[:]
        for char in required:
            if char in new_window:
                matches += 1
                new_window = new_window.replace(char, '', 1)

        if matches == len(required):
            return window

        start += 1
        end += 1

    return _min_window_substring(size + 1, required, string)


def _min_window_substring_ordered(size, required, string):
    start = 0
    end = start + size
    while end <= len(string):
        window = string[start: end]

        if required == window:
            return window

        w_index = 0
        matches = 0

        for char in required:
            while w_index < len(window):
                if char == window[w_index]:
                    matches += 1
                    break
                w_index += 1

        if matches == len(required):
            return window

        start += 1
        end += 1

    return _min_window_substring(size + 1, required, string)


EMPTY_COUNTER = Counter()


def min_window_substring_counter(strArr):
    N, K = strArr
    frequencyK = Counter(K)
    options = []
    for i in range(len(N)):
        curr = Counter()
        for j in range(i, len(N)):
            curr[N[j]] += 1
            if frequencyK - curr == EMPTY_COUNTER:
                options.append(N[i:j + 1])
                break
    return min(options, key=len)


if __name__ == '__main__':
    print(min_window_substring(["ahffaksfajeeubsne", "jefaa"]))
    # print(min_window_substring_counter(["ahffaksfajeeubsne", "jefaa"]))
