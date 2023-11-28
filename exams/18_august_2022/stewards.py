from collections import deque

seats = input().split(", ")
first = deque(map(int, input().split(", ")))
last = list(map(int, input().split(", ")))

rotations_count = 0
seat_matches = []

for i in range(1, 11):
    rotations_count = i
    current_first = first.popleft()
    current_last = last.pop()
    curren_sum = current_first + current_last
    for el in seats:

        num = int(''.join(str(i) for i in el if i.isdigit()))
        let = ord(''.join(str(i) for i in el if i.isalpha()))

        if let == curren_sum and (num == current_first or num == current_last):
            if el not in seat_matches:
                seat_matches.append(el)
                break

    else:
        first.append(current_first)
        last.insert(0, current_last)

    if len(seat_matches) == 3:
        break

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations_count}")
