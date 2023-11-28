from collections import deque

MAX_CAFFEINE = 300

caffeine = list(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

stamat_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    total_caffeine = current_caffeine * current_energy_drink

    if stamat_caffeine + total_caffeine > MAX_CAFFEINE:
        stamat_caffeine = max(stamat_caffeine - 30, 0)
        energy_drinks.append(current_energy_drink)

    else:
        stamat_caffeine += total_caffeine

print(f"Drinks left: {', '.join(map(str, energy_drinks))}") if energy_drinks \
    else print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")
