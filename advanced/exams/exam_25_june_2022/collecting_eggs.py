from collections import deque

BOX_SIZE = 50

eggs_size = deque(map(int, input().split(", ")))
paper_size = list(map(int, input().split(", ")))

boxes = 0

while eggs_size and paper_size:
    current_egg = eggs_size.popleft()
    if current_egg > 0:
        if current_egg == 13:
            paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]
            continue
        current_paper = paper_size.pop()
        current_size = current_egg + current_paper
        if current_size <= BOX_SIZE:
            boxes += 1

print("Sorry! You couldn't fill any boxes!") if not boxes \
    else print(f"Great! You filled {boxes} boxes.")
if eggs_size:
    print(f"Eggs left: {', '.join(map(str, eggs_size))}")
if paper_size:
    print(f"Pieces of paper left: {', '.join(map(str, paper_size))}")
