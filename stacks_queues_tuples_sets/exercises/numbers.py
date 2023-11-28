first = set(map(int, input().split()))
second = set(map(int, input().split()))

commands = {
    "Add First": lambda x: [first.add(number) for number in x],
    "Remove First": lambda x: [first.discard(number) for number in x],
    "Add Second": lambda x: [second.add(number) for number in x],
    "Remove Second": lambda x: [second.discard(number) for number in x],
    "Check Subset": lambda: True if first.issubset(second) or second.issubset(first) else False
}

for _ in range(int(input())):
    command, *data = input().split()
    command += " " + data.pop(0)

    if data:
        commands[command](set(map(int, data)))
    else:
        print(commands[command]())

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
