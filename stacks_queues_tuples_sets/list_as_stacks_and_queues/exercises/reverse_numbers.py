from collections import deque

numbers = reversed(deque(input().split()))

print(*numbers, sep=" ")