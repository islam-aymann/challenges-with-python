def solution(N):
    b = str(bin(N))[2:]
    s = len(b)
    i = m = c = 0

    while i < s:

        if b[i] == "1":
            c = 0
            i += 1

        while i < s and b[i] == "0":
            c += 1
            i += 1

        if i < s and b[i] == "1":
            if c > m:
                m = c
        else:
            i += 1

    return m


if __name__ == '__main__':
    print(solution(561892))
