from collections import deque

materials = list(map(int, input().split()))
magics = deque(map(int, input().split()))

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

result = {}
while materials and magics:
    last_material = materials.pop() if magics[0] or not materials[0] else False
    first_magic = magics.popleft() if last_material or not magics[0] else False
    if not first_magic:
        continue

    magic_craft = last_material * first_magic

    if magic_craft in presents:
        if presents[magic_craft] not in result:
            result[presents[magic_craft]] = 0
        result[presents[magic_craft]] += 1

    elif magic_craft < 0:
        materials.append(last_material + first_magic)

    else:
        materials.append(last_material + 15)

doll_combo = True if "Doll" in result and "Wooden train" in result else False
bear_combo = True if "Teddy bear" in result and "Bicycle" in result else False

print("The presents are crafted! Merry Christmas!") if doll_combo or bear_combo \
    else print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")

for el in sorted(result):
    print(f"{el}: {result[el]}")