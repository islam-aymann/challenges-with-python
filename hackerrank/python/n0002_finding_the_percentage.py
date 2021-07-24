import timeit


def find_the_percentage_of(n, student_marks, query_name):
    student = student_marks[query_name]
    print(f"{sum(student)/n:.2f}")


if __name__ == "__main__":
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()

    n = 3
    student_marks = {
        "Krishna": [67, 68, 69],
        "Arjun": [70, 98, 63],
        "Malika": [52, 56, 60],
    }
    query_name = "Malika"

    find_the_percentage_of(n, student_marks, query_name)
    # print(
    #     1000
    #     * timeit.timeit(
    #         lambda: find_the_percentage_of(n, student_marks, query_name),
    #         number=10000,
    #         globals=globals(),
    #     ),
    #     "ms",
    # )
