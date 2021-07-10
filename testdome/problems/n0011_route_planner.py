def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    rows = len(map_matrix)
    cols = len(map_matrix[0])

    start = (from_row, from_column)
    goal = (to_row, to_column)

    stack = list()
    stack.append(start)

    predecessors = {start: None}

    while stack:
        current_cell = stack.pop()
        if current_cell == goal:
            return True

        for row_offset, col_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            row = current_cell[0] + row_offset
            col = current_cell[1] + col_offset
            neighbor = row, col
            if (
                neighbor not in predecessors
                and 0 <= row < rows
                and 0 <= col < cols
                and map_matrix[row][col]
            ):
                stack.append(neighbor)
                predecessors[neighbor] = current_cell

    return None


if __name__ == "__main__":
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True],
    ]

    print(route_exists(0, 0, 2, 2, map_matrix))
