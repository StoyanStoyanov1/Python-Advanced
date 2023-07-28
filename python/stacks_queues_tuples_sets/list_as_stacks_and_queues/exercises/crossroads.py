from collections import deque

green_light = int(input())
free_window = int(input())

cars = deque()
crash = False
passed = 0

while True and crash != True:
    info = input()

    if info == "END":
        print(f"Everyone is safe.\n{passed} total cars passed the crossroads.")
        break

    if info != "green":
        cars.append(info)
    else:
        current_green_light = green_light
        while current_green_light > 0 and cars:
            car = cars.popleft()

            time = current_green_light + free_window

            if len(car) > time:
                crash = True
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                break

            current_green_light -= len(car)
            passed += 1
