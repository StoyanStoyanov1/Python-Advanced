from collections import deque

petrol_pumps = deque(input().split() for _ in range(int(input())))

for index in range(len(petrol_pumps)):
    litters = 0
    for pump in petrol_pumps:
        litters += int(pump[0])
        litters -= int(pump[1])
        if litters < 0:
            petrol_pumps.append(petrol_pumps.popleft())
            break

    else:
        print(index)
        break





