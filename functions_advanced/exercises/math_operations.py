def math_operations(*numbers, **operations):
    for index, number in enumerate(numbers):
        key = list(operations.keys())[index % 4]

        if key == "a":
            operations[key] += number

        elif key == "s":
            operations[key] -= number

        elif key == "d" and number != 0:
            operations[key] /= number

        elif key == "m":
            operations[key] *= number

    operations = dict(sorted(operations.items(), key=lambda x: (-x[1], x[0])))

    return "\n".join(f"{key}: {value:.1f}" for key, value in operations.items())


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,
                      d=33, m=15))
