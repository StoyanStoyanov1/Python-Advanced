def find_number_of_battles(matrix, steps, row, col):
    current_number_of_battle = 0

    for step in steps:
        current_row = row + step[0]
        current_col = col + step[1]
        if current_row in range(len(matrix)) and current_col in range(len(matrix[0])):
            if matrix[current_row][current_col] == "K":
                current_number_of_battle += 1

    return current_number_of_battle


def result(matrix, steps):
    counter = 0

    while True:
        max_battles = 0
        max_battles_knight = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "K":
                    found_number_of_battle = find_number_of_battles(matrix, steps, row, col)

                    if found_number_of_battle > max_battles:
                        max_battles = found_number_of_battle
                        max_battles_knight = [row, col]

        if max_battles:
            counter += 1
            r, c = max_battles_knight
            matrix[r][c] = "O"

        else:
            return counter


matrix = [list(input()) for _ in range(int(input()))]

steps = (
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2)
)

print(result(matrix, steps))
