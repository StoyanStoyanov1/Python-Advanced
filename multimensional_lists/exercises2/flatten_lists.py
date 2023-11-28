numbers = [num.split() for num in input().split("|")]

result = []

for num in numbers[::-1]:
    result.extend(num)

print(*result)
