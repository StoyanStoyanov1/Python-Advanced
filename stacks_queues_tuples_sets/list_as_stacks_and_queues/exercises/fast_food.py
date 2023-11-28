from collections import deque

quantity_of_food = int(input())
orders = deque(int(order) for order in input().split())

print(max(orders))

for order in orders.copy():
    quantity_of_food -= order
    if quantity_of_food >= 0:
        orders.popleft()
    else:
        break

print(f"Orders left:", *orders, sep=" ") if orders else print("Orders complete")