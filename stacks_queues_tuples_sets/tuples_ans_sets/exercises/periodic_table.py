elements = set()


for _ in range(int(input())):
    current_elements = input().split()
    [elements.add(element) for element in current_elements]

print(*elements, sep="\n")

