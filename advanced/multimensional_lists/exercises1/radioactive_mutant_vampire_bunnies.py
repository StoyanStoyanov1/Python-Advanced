import copy

rows, cols = list(map(int, input().split()))

matrix = [[symbol for symbol in symbols] for _ in range(rows) for symbols in input().split()]

steps = {"L": [0, -1],
         "R": [0, 1],
         "U": [-1, 0],
         "D": [1, 0]
         }

player_steps = input()

current_index_player = [(row, col) for row in range(rows) for col in range(cols) if matrix[row][col] == "P"]

won = False
dead = False

for current_step in player_steps:

    next_row = current_index_player[0][0] + steps[current_step][0]
    next_col = current_index_player[0][1] + steps[current_step][1]
    matrix[current_index_player[0][0]][current_index_player[0][1]] = "."
    if next_row in range(rows) and next_col in range(cols):

        current_index_player = [(next_row, next_col)]
        if not matrix[current_index_player[0][0]][current_index_player[0][1]] == "B":
            matrix[current_index_player[0][0]][current_index_player[0][1]] = "P"

        else:
            dead = True

    else:
        won = True

    copy_matrix = copy.deepcopy(matrix)

    for row, symbols in enumerate(copy_matrix):
        for col, symbol in enumerate(symbols):
            if symbol == "B":
                for step in steps.values():
                    the_next_row = row + step[0]
                    the_next_col = col + step[1]

                    if the_next_row in range(rows) and the_next_col in range(cols):
                        if matrix[the_next_row][the_next_col] == ".":
                            matrix[the_next_row][the_next_col] = "B"

                        elif matrix[the_next_row][the_next_col] == "P":
                            matrix[the_next_row][the_next_col] = "B"
                            dead = True
                            current_index_player = [(the_next_row, the_next_col)]

    if won:
        break

    if dead:
        break

if won:
    [print("".join(i)) for i in matrix]
    print("won:", current_index_player[0][0], current_index_player[0][1])

if dead:
    [print("".join(i)) for i in matrix]
    print("dead:", current_index_player[0][0], current_index_player[0][1])
