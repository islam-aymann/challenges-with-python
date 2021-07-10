from math import sqrt


def find_roots(a, b, c):
    d = sqrt(b ** 2 - 4 * a * c)
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)

    return x1, x2


if __name__ == '__main__':
    print(find_roots(2, 10, 8))
