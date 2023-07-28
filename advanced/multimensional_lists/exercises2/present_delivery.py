def find_santa_position(matrix):
    santa_position = []
    nice_kids = 0
    for row in range(len(matrix)):
        if "S" in matrix[row]:
            santa_position = [row, matrix[row].index("S")]

        if "V" in matrix[row]:
            nice_kids += matrix[row].count("V")

    return santa_position, nice_kids


number_of_presents = int(input())
size = int(input())
matrix = [input().split() for _ in range(size)]

santa_position, number_of_nice_kids = find_santa_position(matrix)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1]
}

happy_nice_kids = 0

while number_of_presents and number_of_nice_kids >= happy_nice_kids:
    command = input()
    if command == "Christmas morning":
        break

    if santa_position[0] + directions[command][0] in range(size) \
            and santa_position[1] + directions[command][1] in range(size):
        matrix[santa_position[0]][santa_position[1]] = "-"
        santa_position = [santa_position[0] + directions[command][0], santa_position[1] + directions[command][1]]
        current_row, current_col = santa_position

        if matrix[current_row][current_col] == "V":
            happy_nice_kids += 1
            number_of_presents -= 1



        elif matrix[current_row][current_col] == "C":
            for step in directions.keys():
                row, col = current_row + directions[step][0], current_col + directions[step][1]
                if row in range(size) and col in range(size) and number_of_presents:
                    if matrix[row][col] != "-":
                        if matrix[row][col] == "V":
                            happy_nice_kids += 1

                        number_of_presents -= 1
                        matrix[row][col] = "-"

        matrix[current_row][current_col] = "S"
if not number_of_presents and happy_nice_kids < number_of_nice_kids:
    print("Santa ran out of presents!")

[print(*x) for x in matrix]

if happy_nice_kids == number_of_nice_kids:
    print(f"Good job, Santa! {happy_nice_kids} happy nice kid/s.")

else:
    print(f"No presents for {number_of_nice_kids - happy_nice_kids} nice kid/s.")
