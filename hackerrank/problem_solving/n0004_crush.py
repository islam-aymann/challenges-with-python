import timeit
from collections import Counter


def arrayManipulation1(n, queries):
    arr = [0 for _ in range(n)]
    for query in queries:
        a, b, k = query
        for i in range(a - 1, b):
            arr[i] += k

    return max(arr)


def arrayManipulation(n, queries):
    # please note that this solution takes more time than the previous one,
    # but actually for large data sets it will perform better this
    c = Counter()
    for a, b, k in queries:
        c[a] += k
        c[b + 1] -= k

    arr_sum = 0
    max_sum = 0
    for i in sorted(c)[:-1]:
        arr_sum += c[i]
        max_sum = max(max_sum, arr_sum)

    return max_sum


if __name__ == "__main__":
    # print(
    #     arrayManipulation(
    #         10,
    #         [
    #             [1, 5, 3],
    #             [4, 8, 7],
    #             [6, 9, 1],
    #         ],
    #     )
    # )

    print(
        1000
        * timeit.timeit(
            lambda: arrayManipulation(
                10,
                [
                    [1, 5, 3],
                    [4, 8, 7],
                    [6, 9, 1],
                ],
            ),
            number=100000,
            globals=globals(),
        ),
        "ms",
    )
