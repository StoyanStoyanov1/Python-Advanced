rows, cols = 6, 6
matrix = [[i for i in input().split()] for _ in range(rows)]
my_position = [int(i) for i in input() if i.isdigit()]

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

while True:
    command = input()
    if command == "Stop":
        break

    current_command, *step = command.split(", ")
    my_position[0], my_position[1] = (my_position[0] + directions[step[0]][0],
                                      my_position[1] + directions[step[0]][1])
    if current_command == 'Create':
        if matrix[my_position[0]][my_position[1]] == ".":
            matrix[my_position[0]][my_position[1]] = step[1]

    elif current_command == "Update":
        if matrix[my_position[0]][my_position[1]] != ".":
            matrix[my_position[0]][my_position[1]] = step[1]

    elif current_command == "Delete":
        matrix[my_position[0]][my_position[1]] = '.'

    elif current_command == "Read":
        if matrix[my_position[0]][my_position[1]] != '.':
            print(matrix[my_position[0]][my_position[1]])

[print(' '.join(x)) for x in matrix]