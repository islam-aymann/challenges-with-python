def solution(A, K):
    # write your code in Python 3.6
    l = len(A)
    if l == K or len(set(A)) == 1:
        return A

    p = [0 for i in range(l)]

    for i, num in enumerate(A):
        p[(i + K) % l] = num

    return p


if __name__ == '__main__':
    A, K = [3, 8, 9, 7, 6], 3
    # A, K = [1, 2, 3, 4], 4
    # A, K = [0, 0, 0, 0], 4
    print(solution(A, K))
