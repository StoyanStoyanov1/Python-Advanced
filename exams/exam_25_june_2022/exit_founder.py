players = input().split(", ")
rows = 6

matrix = [[i for i in input().split()] for _ in range(rows)]

step = input()
player = 1
player_pause = []
while step:

    row, col = [int(x) for x in step if x.isdigit()]
    player = 1 if player == 0 else 0
    if player in player_pause:
        player_pause.remove(player)
        step = input()
        continue

    if matrix[row][col] == "E":
        print(f'{players[player]} found the Exit and wins the game!')
        break

    elif matrix[row][col] == "T":
        winner = 1 if player == 0 else 0
        print(f"{players[player]} is out of the game! The winner is {players[winner]}.")
        break


    elif matrix[row][col] == "W":
        print(f"{players[player]} hits a wall and needs to rest.")
        player_pause.append(player)

    step = input()