def find_start_position(matrix, rows):
    for row in range(rows):
        if "S" in matrix[row]:
            return [row, matrix[row].index("S")]


def number_of_destroys(matrix, rows):
    counter = 0
    for row in range(rows):
        counter += matrix[row].count("C")

    return counter


def battle_field(matrix, rows, current_position, destroys, directions, live):
    while True:
        command = input()
        current_row, current_col = current_position[0] + directions[command][0],\
            current_position[1] + directions[command][1]

        if current_row not in range(rows) or current_col not in range(rows):
            continue

        if matrix[current_row][current_col] == "*":
            live -= 1

        elif matrix[current_row][current_col] == "C":
            destroys -= 1

        matrix[current_position[0]][current_position[1]] = "-"
        matrix[current_row][current_col] = "S"
        current_position = [current_row, current_col]

        if not live:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{current_row}, {current_col}]!")
            return matrix

        if not destroys:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            return matrix


rows = int(input())
LIVE = 3

matrix = [list(input()) for _ in range(rows)]
start_position = find_start_position(matrix, rows)
destroys = number_of_destroys(matrix, rows)
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

battle = battle_field(matrix, rows, start_position, destroys, directions, LIVE)

for row in battle:
    print("".join(row))
