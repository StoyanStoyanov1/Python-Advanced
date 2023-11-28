rows = int(input())
commands = input().split()
matrix = [input().split() for _ in range(rows)]

current_index = [(int(row), int(col)) for row in range(rows) for col in range(rows) if matrix[row][col] == "s"]

for command in commands:

    steps = {"up": (current_index[0][0] - 1, current_index[0][1]),
             "down": (current_index[0][0] + 1, current_index[0][1]),
             "left": (current_index[0][0], current_index[0][1] - 1),
             "right": (current_index[0][0], current_index[0][1] + 1)
             }

    row, col = steps[command]

    if row in range(len(matrix)) and col in range(len(matrix[0])):
        current_index = [(row, col)]
        if matrix[row][col] == "c":
            matrix[row][col] = "*"

        elif matrix[row][col] == "e":
            print(f"Game over! {current_index[0]}")
            break

else:

    number_of_coal = [1 for row in range(rows) for col in range(rows) if matrix[row][col] == "c"]

    if number_of_coal:
        print(f"{sum(number_of_coal)} pieces of coal left. {current_index[0]}")

    else:
        print(f"You collected all coal! {current_index[0]}")
