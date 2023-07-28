from collections import deque

cups_capacity = deque(map(int, input().split()))
bottles_capacity = deque(map(int, input().split()))

wasted_litters_of_water = 0

while cups_capacity and bottles_capacity:
    current_cup = cups_capacity.popleft()
    current_bottle = bottles_capacity.pop()

    if current_bottle >= current_cup:
        wasted_litters_of_water += current_bottle - current_cup
    else:
        cups_capacity.appendleft(current_cup - current_bottle)

if cups_capacity:
    print("Cups:", *cups_capacity, sep=" ")

elif bottles_capacity:
    print("Bottles:", *bottles_capacity, sep=" ")

print(f"Wasted litters of water: {wasted_litters_of_water}")

