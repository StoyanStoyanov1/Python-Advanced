try:
    with open("numbers.txt") as numbers:
        print(sum(list(map(int, numbers))))

except FileNotFoundError:
    print("File was not found")
