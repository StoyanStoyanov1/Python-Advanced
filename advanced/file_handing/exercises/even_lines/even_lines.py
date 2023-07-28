symbols = ["-", ",", ".", "!", "?"]

with open("text.txt") as file:
    for row, text in enumerate(file):
        if row % 2 == 0:
            result = " ".join(reversed(text.strip().split()))

            for symbol in symbols:
                result = result.replace(symbol, "@")

            print(result)

