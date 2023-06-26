def find_symbol(rows):
    for row in range(rows):
        for column in range(rows):
            if matrix[row][column] == symbol:
                found_symbol_index = (row, column)
                return found_symbol_index


rows = int(input())

matrix = [[symbol for symbol in input()] for _ in range(rows)]

symbol = input()

found_symbol = find_symbol(rows)

if not found_symbol:
    print(f"{symbol} does not occur in the matrix")
else:
    print(found_symbol)