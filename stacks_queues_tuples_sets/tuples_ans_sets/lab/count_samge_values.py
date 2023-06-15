def numbers_counter(numbers):
    numbers_counter = {}
    for number in numbers:
        if number not in numbers_counter:
            numbers_counter[number] = 0
        numbers_counter[number] += 1

    return numbers_counter


def print_result(current_numbers):
    result = []

    for number, count in numbers_counter(current_numbers).items():
        result.append(f"{number} - {count} times")

    return result


numbers = tuple(map(float, input().split()))

print(*print_result(numbers), sep="\n")
