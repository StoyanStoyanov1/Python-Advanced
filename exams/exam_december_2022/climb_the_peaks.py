from collections import deque

daily_food = list(map(int, input().split(", ")))
daily_stamina = deque(map(int, input().split(", ")))

mountain_peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
count_mountain_peaks = 0

for _ in range(7):

    food = daily_food.pop()
    stamina = daily_stamina.popleft()

    if food + stamina >= list(mountain_peaks.values())[count_mountain_peaks]:
        count_mountain_peaks += 1
        if count_mountain_peaks > 4:
            print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
            break

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if count_mountain_peaks:
    print("Conquered peaks:")
    for count in range(count_mountain_peaks):
        print(list(mountain_peaks.keys())[count])

