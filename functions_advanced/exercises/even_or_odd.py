def even_odd(*args):
    numbers = args[:len(args) - 1]
    command = args[-1]

    if command == "odd":
        return [num for num in numbers if num % 2 != 0]

    elif command == "even":
        return [num for num in numbers if num % 2 == 0]


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))