from collections import deque
from datetime import datetime, timedelta

robots = {robot.split("-")[0]: [int(robot.split("-")[1]), 0]for robot in input().split(";")}
current_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    current_product = products.popleft()
    current_time += timedelta(0, 1)

    robots = {name: [values[0], values[1] - 1] if values[1] != 0 else values for name, values in robots.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    if not free_robots:
        products.append(current_product)
        continue

    robots[free_robots[0][0]][1] = free_robots[0][1][0]

    print(f'{free_robots[0][0]} - {current_product} [{current_time.strftime("%H:%M:%S")}]')
