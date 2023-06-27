rows = int(input())

matrix = [list(map(int, input().split(" "))) for _ in range(rows)]

primary_diagonal = [matrix[index][index]for index in range(rows)]
secondary_diagonal = [matrix[rows - index - 1][index] for index in range(rows)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
