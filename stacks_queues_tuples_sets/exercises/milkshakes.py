from collections import deque

chocolates = deque(map(int, input().split(", ")))
cups_of_milk = deque(map(int, input().split(", ")))

prepare_milkshakes = 0
while chocolates and cups_of_milk and prepare_milkshakes < 5:
    current_chocolate = chocolates.pop()
    current_cup_of_milk = cups_of_milk.popleft()

    if not current_chocolate > 0 or not current_cup_of_milk > 0:
        if current_chocolate > 0:
            chocolates.append(current_chocolate)
        if current_cup_of_milk > 0:
            cups_of_milk.appendleft(current_cup_of_milk)
        continue

    if current_chocolate == current_cup_of_milk:
        prepare_milkshakes += 1
        continue

    cups_of_milk.append(current_cup_of_milk)
    chocolates.append(current_chocolate - 5)

print("Great! You made all the chocolate milkshakes needed!") \
    if prepare_milkshakes == 5 else print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(number) for number in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(number) for number in cups_of_milk) or 'empty'}")
