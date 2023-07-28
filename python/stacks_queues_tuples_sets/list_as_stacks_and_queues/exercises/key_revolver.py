from collections import deque

price_per_bullet = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
value_of_intelligence = int(input())

total_price = 0
bullets_left = gun_barrel_size

while bullets and locks:

    current_bullet = bullets.pop()
    bullets_left -= 1

    current_lock = locks.popleft()

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.insert(0, current_lock)

    total_price += price_per_bullet

    if bullets_left == 0 and bullets:
        print("Reloading!")
        bullets_left = gun_barrel_size

if not locks:
    value_of_intelligence -= total_price
    print(f"{len(bullets)} bullets left. Earned ${value_of_intelligence}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")