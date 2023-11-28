def find_squares(matrix, rows, columns):
    found_squares = 0

    for row in range(rows - 1):
        for column in range(columns - 1):
            current_symbol = matrix[row][column]

            if current_symbol in matrix[row][column + 1] and \
                    current_symbol in matrix[row + 1][column] and \
                    current_symbol in matrix[row + 1][column + 1]:
                found_squares += 1

    return found_squares


rows, columns = list(map(int, input().split()))

matrix = [input().split() for _ in range(rows)]

found_squares = find_squares(matrix, rows, columns)

print(found_squares)
