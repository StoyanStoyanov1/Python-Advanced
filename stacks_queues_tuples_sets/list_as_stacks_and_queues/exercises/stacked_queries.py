from collections import deque

numbers = deque()
commands = {
    1: lambda number: numbers.append(number[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None
}

for _ in range(int(input())):
    current_command = [int(command) for command in input().split()]
    commands[current_command[0]](current_command)

numbers.reverse()
print(*numbers, sep=", ")