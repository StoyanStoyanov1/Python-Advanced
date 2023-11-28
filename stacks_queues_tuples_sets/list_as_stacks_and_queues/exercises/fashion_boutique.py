clothes = list(map(int, input().split()))
capacity = int(input())

needed_racks = 1
current_needed_space = capacity

while clothes:
    cloth = clothes.pop()
    if current_needed_space - cloth >= 0:
        current_needed_space -= cloth
    else:
        needed_racks += 1
        current_needed_space = capacity - cloth

print(needed_racks)
