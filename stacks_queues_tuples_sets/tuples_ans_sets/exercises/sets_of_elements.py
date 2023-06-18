from collections import deque

count = deque(int(count) for count in input().split())

first_set_number = set(input() for _ in range(count.popleft()))
second_set_number = set(input() for _ in range(count.popleft()))

print("\n".join(first_set_number.intersection(second_set_number)))