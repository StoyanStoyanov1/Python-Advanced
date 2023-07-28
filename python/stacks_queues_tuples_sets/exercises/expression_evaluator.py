from functools import reduce

data = input().split()

operators = {
    "*": lambda i: reduce(lambda a, b: a * b, [int(number) for number in data[:i]]),
    "/": lambda i: reduce(lambda a, b: a / b, [int(number) for number in data[:i]]),
    "+": lambda i: reduce(lambda a, b: a + b, [int(number) for number in data[:i]]),
    "-": lambda i: reduce(lambda a, b: a - b, [int(number) for number in data[:i]])
}

index = 0

while index < len(data):
    current_element = data[index]

    if current_element in "+-*/":
        result = operators[current_element](index)
        [data.pop(0) for _ in range(index + 1)]
        data.insert(0, result)
        index = 0

    index += 1

print(int(data[0]))