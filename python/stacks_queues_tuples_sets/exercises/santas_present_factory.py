from collections import deque

materials = deque(map(int, input().split()))
magics = deque(map(int, input().split()))

result = []

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    499: "Bicycle"
}

while magics and materials:
    current_material = materials.pop() if magics[0] or not materials[0] else 0
    current_magic = magics.pop() if current_material or magics[0] else 0

    if not current_magic:
        continue

    product = current_material * current_magic

    if presents.get(product):
        result.append(presents[product])

    elif product < 0:
        materials.append(product + current_magic)

    elif product > 0:
        materials.append(product + 15)

print(result)