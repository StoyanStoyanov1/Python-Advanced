def find_tunel(matrix):
    for row in range(len(matrix)):
        if "T" in matrix[row]:
            col = matrix[row].index('T')
            matrix[row][col] = "."
            return [row, col]

matrix_size = int(input())
racing_number = input()

matrix = [x.split() for x in [input() for _ in range(matrix_size)]]

distance_covered = 0
current_position = [0, 0]

directions = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}

while True:
    command = input()
    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        matrix[current_position[0]][current_position[1]] = "C"
        break

    current_position = (current_position[0] + directions[command][0],
                        current_position[1] + directions[command][1])

    if matrix[current_position[0]][current_position[1]] == "T":
        distance_covered += 30
        matrix[current_position[0]][current_position[1]] = "."
        current_position = find_tunel(matrix)

    elif matrix[current_position[0]][current_position[1]] == "F":
        distance_covered += 10
        matrix[current_position[0]][current_position[1]] = "C"
        print(f"Racing car {racing_number} finished the stage!")
        break

    else:
        distance_covered += 10

print(f"Distance covered {distance_covered} km.")
[print(''.join(x)) for x in matrix]