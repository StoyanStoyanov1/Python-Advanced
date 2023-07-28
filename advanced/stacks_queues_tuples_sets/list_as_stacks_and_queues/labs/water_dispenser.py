from collections import deque

quantity_of_water = int(input())
names = deque()

while True:
    name = input()

    if name == "Start":
        break

    names.append(name)

while True:
    command = input()

    if command == "End":
        print(f"{quantity_of_water} liters left")
        break
    if command.isdigit():
        litters = int(command)
        if quantity_of_water >= litters:
            quantity_of_water -= litters
            print(f"{names.popleft()} got water")
        else:
            print(f"{names.popleft()} must wait")

    else:
        refill_litters = int(command.split()[1])
        quantity_of_water += refill_litters
