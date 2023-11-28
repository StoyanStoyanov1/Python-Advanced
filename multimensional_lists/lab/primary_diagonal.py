rows = int(input())

matrix = [[int(number) for number in input().split()]for _ in range(rows)]

sum_of_diagonal = sum([matrix[index][index] for index in range(rows)])

print(sum_of_diagonal)