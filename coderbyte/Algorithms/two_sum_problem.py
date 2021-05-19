def two_sum(arr, s):
    answers = list()

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and (arr[i] + arr[j] == s) and (
                    (arr[i], arr[j]) not in answers) and (
                    (arr[j], arr[i]) not in answers):
                answers.append((arr[i], arr[j]))

    return answers


# TODO fix it
def two_sum_dict(arr, s):
    sums = list()
    table = dict()

    for i in range(len(arr)):
        sum_minus_element = s - arr[i]

        if sum_minus_element not in table.keys():
            sums.append((arr[i], sum_minus_element))

        table[sum_minus_element] = arr[i]

    return sums


if __name__ == '__main__':
    print(two_sum([3, 5, 2, -4, 8, 11], 7))
    print(two_sum_dict([3, 5, 2, -4, 8, 11], 7))
