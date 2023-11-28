from collections import deque

input_colors = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ["red", "yellow"],
                    "purple": ["red", "blue"],
                    "green": ["yellow", "blue"]}

found_colors = []

while input_colors:
    first_color = input_colors.popleft()
    second_color = input_colors.pop() if input_colors else ""
    current_color = [x for x in [first_color + second_color, second_color + first_color]
                     if x in main_colors or x in secondary_colors]
    if current_color:
        found_colors.append(current_color[0])
    else:
        first_color = first_color[:len(first_color) - 1]
        second_color = second_color[:len(second_color) - 1]
        if first_color:
            input_colors.insert(len(input_colors) // 2, first_color)
        if second_color:
            input_colors.insert(len(input_colors) // 2, second_color)

result = []

for color in found_colors:
    if color in main_colors:
        result.append(color)
    else:
        if all(c in found_colors for c in secondary_colors[color]):
            result.append(color)

print(result)

