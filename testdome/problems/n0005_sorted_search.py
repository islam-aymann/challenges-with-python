def count_numbers(sorted_list, less_than):
    """only passed one test, I am not sure what are the test cases :("""
    size = len(sorted_list)

    try:
        return sorted_list.index(less_than)
    except ValueError:
        if less_than < sorted_list[0]:
            return 0

        elif less_than > sorted_list[-1]:
            return size

        i = 0
        while i < size and i < sorted_list[i] < less_than:
            i += 1

        return i


if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4))  # should print 2
