def find_current_position(matrix):
    position = []
    count_of_x_target = 0
    for row in range(5):
        count_of_x_target += matrix[row].count("x")
        if "A" in matrix[row]:
            position = [row, matrix[row].index("A")]

    return position, count_of_x_target


def shoot(matrix, step, directions, current_position, count_of_x_target):
    row, col = current_position
    while True:
        row += directions[step][0]
        col += directions[step][1]
        if row in range(5) and col in range(5):
            if matrix[row][col] == "x":
                indexes_of_shoot_targets.append([row, col])
                matrix[row][col] = "."
                count_of_x_target -= 1
                return matrix, count_of_x_target

        else:
            return matrix, count_of_x_target


def move(matrix, step, count, directions, current_position):
    current_row, current_col = current_position

    row = current_row + (directions[step][0] * count)
    col = current_col + (directions[step][1] * count)

    if row in range(5) and col in range(5):
        if matrix[row][col] == ".":
            return [row, col]

    return [current_row, current_col]


matrix = [input().split() for _ in range(5)]
position, count_of_x_target = find_current_position(matrix)
indexes_of_shoot_targets = []

directions = {
    "right": [0, 1],
    "left": [0, -1],
    "up": [-1, 0],
    "down": [1, 0]
}

for _ in range(int(input())):
    command, *step = input().split()

    if command == "shoot":

        matrix, count_of_x_target = shoot(matrix, step[0], directions, position, count_of_x_target)

    elif command == "move":
        position = move(matrix, step[0], int(step[1]), directions, position)

    if count_of_x_target == 0:
        print(f"Training completed! All {len(indexes_of_shoot_targets)} targets hit.")
        break

else:
    print(f"Training not completed! {count_of_x_target} targets left.")

print(*indexes_of_shoot_targets, sep='\n')
