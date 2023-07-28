text = input()
opening_parenthesis_indexes = []

for index, symbol in enumerate(text):
    if symbol == "(":
        opening_parenthesis_indexes.append(index)
    elif symbol == ")":
        print(text[opening_parenthesis_indexes.pop():index + 1])
