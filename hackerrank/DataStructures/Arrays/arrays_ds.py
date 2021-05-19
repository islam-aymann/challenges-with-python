def hourglassSum(arr):
    y = 0
    results = list()
    while (y + 3) <= len(arr):
        x = 0
        while (x + 3) <= len(arr):
            r1 = arr[y][x: x + 3]
            r2 = arr[y + 1][x + 1:x + 2]
            r3 = arr[y + 2][x: x + 3]
            results.append(sum(r1 + r2 + r3))
            x += 1

        y += 1

    return max(results)


if __name__ == '__main__':
    print(hourglassSum(
        [[1, 1, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0],
         [0, 0, 2, 4, 4, 0],
         [0, 0, 0, 2, 0, 0],
         [0, 0, 1, 2, 4, 0]]
    ))
