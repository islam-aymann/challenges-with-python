if __name__ == "__main__":
    N = int(input())
    lst = []
    i = 0
    e = 0

    for c in range(N):
        command = input()
        op_args = command.split(" ")
        op = op_args[0]
        size = len(op_args)

        if size == 3:
            i = int(op_args[1])
            e = int(op_args[2])
        elif size == 2:
            e = int(op_args[1])

        if op == "insert":
            lst.insert(i, e)

        elif op == "print":
            print(lst)

        elif op == "append":
            lst.append(e)
        elif op == "remove":
            lst.remove(e)
        elif op == "sort":
            lst.sort()
        elif op == "pop":
            lst.pop()
        elif op == "reverse":
            lst.reverse()
