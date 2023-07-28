rows, columns = list(map(int, input().split()))

matrix = [input().split() for _ in range(rows)]

command = input().split()

while command[0] != "END":
    if command[0] != "swap":
        print("Invalid input!")


    else:
        if len(command[1:]) == 4:
            row1, col1, row2, col2 = [int(x) for x in command[1:]]
            if row1 in range(rows) and row2 in range(rows) and col1 in range(columns) \
                    and col2 in range(columns):
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                [print(*x, sep=" ") for x in matrix]

            else:
                print("Invalid input!")

        else:
            print("Invalid input!")

    command = input().split()
