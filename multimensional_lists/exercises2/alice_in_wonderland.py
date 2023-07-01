def find_alice_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "A":
                return [row, col]


size = int(input())
matrix = [input().split() for _ in range(size)]

alice_position = find_alice_position(matrix)
matrix[alice_position[0]][alice_position[1]] = "*"
tea_bags = 0

steps = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    current_step = input()

    alice_position = alice_position[0] + steps[current_step][0], alice_position[1] + steps[current_step][1]
    row, col = alice_position[0], alice_position[1]

    if row in range(size) and col in range(size):

        if matrix[row][col] == "R":
            matrix[row][col] = "*"
            print("Alice didn't make it to the tea party.")
            break

        elif matrix[row][col].isdigit():
            tea_bags += int(matrix[row][col])
            matrix[row][col] = "*"
            if tea_bags >= 10:
                print("She did it! She went to the party.")
                break

        else:
            matrix[row][col] = "*"
    else:
        print("Alice didn't make it to the tea party.")
        break

[print(*x) for x in matrix]
