from collections import deque

bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
current_operators = deque(input().split())

operators = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b
}

total_honey = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)

    elif current_nectar > current_bee:
        total_honey += abs(operators[current_operators.popleft()](current_bee, current_nectar))

print("Total honey made:", total_honey)

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")