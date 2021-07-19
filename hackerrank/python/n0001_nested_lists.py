import timeit


def print_second_lowest_grade_student_names(name_scores):
    score_names = {}
    for name, score in name_scores:
        score_names[score] = score_names.get(score, []) + [name]
    second_lowest_grade = sorted(score_names.keys())[1]

    for name in sorted(score_names[second_lowest_grade]):
        print(name)
        # pass


if __name__ == "__main__":
    # name_scores = []

    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     name_scores.append([name, score])

    n, name_scores = 5, [
        ["Harry", 37.21],
        ["Berry", 37.21],
        ["Tina", 37.2],
        ["Akriti", 41],
        ["Harsh", 39],
    ]

    # print_second_lowest_grade_student_names(name_scores)
    print(
        1000
        * timeit.timeit(
            lambda: print_second_lowest_grade_student_names(name_scores), number=10000,
            globals=globals()
        ),
        "ms",
    )

