rows, columns = list(map(int, input().split(", ")))

matrix = [[int(number) for number in input().split()] for _ in range(rows)]

sum_of_columns = [print(sum([matrix[row][column]for row in range(rows)]))for column in range(columns)]