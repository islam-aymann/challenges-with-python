def precedence(op):
    return {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }.get(op, 0)


def apply(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a // b


def calc(expression):
    values = []

    ops = []
    i = 0

    while i < len(expression):

        if expression[i] == ' ':
            i += 1
            continue

        elif expression[i] == '(':
            ops.append(expression[i])

        elif expression[i].isdigit() or (
                expression[i] == '-' and expression[i + 1].isdigit()):
            negative = False
            if expression[i] == '-':
                negative = True
                i += 1

            before = 0
            after = 0

            while i < len(expression) and expression[i].isdigit():
                before = (before * 10) + int(expression[i])
                i += 1

            if i < len(expression) and expression[i] == '.':
                i += 1
                while i < len(expression) and expression[i].isdigit():
                    after = (after * 10) + int(expression[i])
                    i += 1

            val = float(f'-{before}.{after}') if negative else float(
                f'{before}.{after}')

            values.append(val)

            i -= 1

        elif expression[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                op = ops.pop()
                if op == '-' and not values:
                    val1 = 0
                else:
                    val1 = values.pop()

                values.append(apply(val1, val2, op))

            ops.pop()

        else:

            while (len(ops) != 0 and
                   precedence(ops[-1]) >=
                   precedence(expression[i])):
                val2 = values.pop()
                op = ops.pop()
                if not values:
                    val1 = 0
                else:
                    val1 = values.pop()

                values.append(apply(val1, val2, op))

            ops.append(expression[i])

        i += 1

    while len(ops) != 0:
        val2 = values.pop()
        op = ops.pop()
        if not values:
            val1 = 0
        else:
            val1 = values.pop()

        values.append(apply(val1, val2, op))

    return values[-1]


# Driver Code
if __name__ == "__main__":
    # print(calc("10 + 2 * 6"))
    # print(calc("100 * 2 + 12"))
    # print(calc("100 * ( 2 + 12 )"))
    # print(calc("100 * ( 2 + 12 ) / 14"))
    # print(calc("123.509+1"))
    # print(calc("2 / (2 + 3) * 4.33 - -6"))
    # print(calc("-12 * -123"))
    # print(calc("12* 123/-(-5 + 2)"))
    # print(calc("-123.23 + 3"))
    print(calc("(1 - 2) + -(-(-(-4)))"))
    # print(calc("1-(-(-(-4)))"))
    # print(calc("-(-5 + 2)"))
