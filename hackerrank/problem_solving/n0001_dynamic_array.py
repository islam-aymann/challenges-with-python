#!/bin/python3

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers_arr = []
    for query in queries:
        q, x, y = query
        if q == 1:
            idx = ((x ^ lastAnswer) % n)
            arr[idx].append(y)
        elif q == 2:
            idx = ((x ^ lastAnswer) % n)
            lastAnswer = arr[idx][y % len((arr[idx]))]
            answers_arr.append(lastAnswer)

    return answers_arr


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # first_multiple_input = input().rstrip().split()
    #
    # n = int(first_multiple_input[0])
    #
    # q = int(first_multiple_input[1])
    #
    # queries = []
    # for _ in range(q):
    #     queries.append(list(map(int, input().rstrip().split())))

    n = 2
    q = 5

    queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
    result = dynamicArray(n, queries)

    # fptr.write("\n".join(map(str, result)))
    # fptr.write("\n")
    #
    # fptr.close()
