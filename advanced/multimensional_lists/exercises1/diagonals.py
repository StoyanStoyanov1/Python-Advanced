rows = int(input())

matrix = [list(map(int, input().split(", "))) for _ in range(rows)]

primary_diagonal = [matrix[index][index] for index in range(rows)]
secondary_diagonal = [matrix[rows - index - 1][index] for index in range(rows - 1, -1, -1)]

print(f"Primary diagonal: {', '.join(str(n) for n in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(n) for n in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")