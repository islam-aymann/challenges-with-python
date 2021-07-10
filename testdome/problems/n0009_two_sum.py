from operator import itemgetter


def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    size = len(numbers)
    numbers = [(i, n) for i, n in enumerate(numbers)]
    numbers.sort(key=itemgetter(1))

    i = 0
    j = size - 1

    while i < j:
        s = numbers[i][1] + numbers[j][1]
        if s == target_sum:
            return numbers[i][0], numbers[j][0]
        elif s > target_sum:
            j -= 1
        else:
            i += 1


if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
