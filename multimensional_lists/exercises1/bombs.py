matrix = [list(map(int, input().split())) for _ in range(int(input()))]

indexes = [x.split(",") for x in input().split()]

steps = (
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
)

for current_indexes in indexes:
    row, col = int(current_indexes[0]), int(current_indexes[1])

    if matrix[row][col] > 0:

        for step_row, step_col in steps:
            current_row = row + step_row
            current_col = col + step_col

            if current_row in range(len(matrix)) and current_col in range(len(matrix[0])):

                if matrix[current_row][current_col] > 0:
                    matrix[current_row][current_col] -= matrix[row][col]

        matrix[row][col] = 0

alive_cells = [number for current_list in matrix for number in current_list if number > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*bombs) for bombs in matrix]
