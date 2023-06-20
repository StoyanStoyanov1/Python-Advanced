parentheses = input()
opening_parentheses = []

is_balanced = True

for parent in parentheses:
    if parent in "[{(":
        opening_parentheses.append(parent)

    else:
        if opening_parentheses:
            current_parentheses = opening_parentheses.pop() + parent

            if current_parentheses not in ["{}", "()", "[]"]:
                is_balanced = False

        else:
            is_balanced = False

    if not is_balanced:
        break

print("YES") if is_balanced else print("NO")