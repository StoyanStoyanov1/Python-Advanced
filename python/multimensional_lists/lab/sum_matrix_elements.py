rows, column = list(map(int, input().split(", ")))

matrix = [[int(number) for number in input().split(", ")]for _ in range(rows)]

print(sum([sum(numbers) for numbers in matrix]))
print(matrix)