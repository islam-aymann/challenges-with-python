import timeit
from collections import deque
from typing import List


def rotateLeft1(d: int, arr: List[int]) -> List[int]:
    d %= len(arr)
    if not d:
        return arr

    new_arr = []
    arr.reverse()
    for _ in range(d):
        new_arr.append(arr.pop())

    arr.reverse()
    arr += new_arr
    return arr


def rotateLeft2(d: int, arr: List[int]) -> List[int]:
    q = deque(arr)
    q.rotate(-d)
    return list(q)


def rotateLeft(d: int, arr: List[int]) -> List[int]:
    d %= len(arr)
    if not d:
        return arr

    return arr[d:] + arr[:d]


if __name__ == "__main__":
    # d = 2
    # arr = [1, 2, 3, 4, 5]
    d = 6
    arr = [1, 2, 3, 4, 5]
    # print(rotateLeft(d, arr))
    #
    print(
        1000
        * timeit.timeit(
            lambda: rotateLeft(d, arr), number=100000, globals=globals()
        ),
        "ms",
    )
