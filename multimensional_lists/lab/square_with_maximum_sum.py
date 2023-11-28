def find_squares(matrix, rows, columns):
    found_squares = []
    for row in range(rows - 1):
        for column in range(columns - 1):
            current_square = []
            current_square.append(matrix[row][column])
            current_square.append(matrix[row][column + 1])
            current_square.append(matrix[row + 1][column])
            current_square.append(matrix[row + 1][column + 1])
            found_squares.append(current_square)

    return found_squares


rows, columns = list(map(int, input().split(", ")))

matrix = [list(map(int, input().split(", "))) for _ in range(rows)]

found_squares = find_squares(matrix, rows, columns)

max_found_sum_square = sorted(found_squares, key=lambda x: (sum(x)), reverse=True)

print(*max_found_sum_square[0][:2], sep=" ")
print(*max_found_sum_square[0][2:], sep=" ")
print(sum(max_found_sum_square[0]))