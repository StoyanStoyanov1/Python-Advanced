rows, cols = list(map(int, input().split()))

for row in range(ord("a"), ord("a") + rows):
    for col in range(cols):
        print(f"{chr(row)}{chr(col + row)}{chr(row)}", end=" ")
    print()
