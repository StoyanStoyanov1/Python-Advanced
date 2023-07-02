def add(matrix, row, col, value):
    if row in range(len(matrix)) and col in range(len(matrix[0])):
        matrix[row][col] += value

    else:
        print("Invalid coordinates")

    return matrix


def subtract(matrix, row, col, value):
    if row in range(len(matrix)) and col in range(len(matrix[0])):
        matrix[row][col] -= value

    else:
        print("Invalid coordinates")

    return matrix


matrix = [list(map(int, input().split())) for _ in range(int(input()))]

while True:
    command = input()
    if command == "END":
        break

    current_command, row, col, value = command.split()

    if current_command == "Add":
        matrix = add(matrix, int(row), int(col), int(value))

    elif current_command == "Subtract":
        matrix = subtract(matrix, int(row), int(col), int(value))

[print(*i) for i in matrix]
