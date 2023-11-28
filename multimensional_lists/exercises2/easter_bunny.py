def find_bunny_index(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "B":
                return [row, col]


size = int(input())
matrix = [input().split() for _ in range(size)]
bunny_index = find_bunny_index(matrix)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

max_eggs = 0
best_direction = ""
best_steps = []

for direction, step in directions.items():
    current_number_of_eggs = 0
    row, col = bunny_index
    current_steps = []

    while True:
        row += step[0]
        col += step[1]

        if row not in range(size) or col not in range(size):
            break

        if matrix[row][col] == "X":
            break

        number_of_eggs = int(matrix[row][col])
        current_number_of_eggs += number_of_eggs
        current_steps.append([row, col])

    if current_number_of_eggs >= max_eggs:
        max_eggs = current_number_of_eggs
        best_direction = direction
        best_steps = current_steps

print(best_direction)
print(*best_steps, sep="\n")
print(max_eggs)
