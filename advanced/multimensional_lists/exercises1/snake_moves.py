rows, cols = list(map(int, input().split()))

text = input()
copy_text = text

while len(text) < cols:
    text += copy_text

for row in range(rows):

    rest = text[cols:]
    text = text[:cols]

    if row % 2 != 0:
        print(text[::-1])
    else:
        print(text)

    text = rest + text
