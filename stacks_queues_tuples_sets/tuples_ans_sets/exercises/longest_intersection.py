longest_intersection = set()

for _ in range(int(input())):
    ranges = input().split("-")
    first_start, first_end = ranges[0].split(",")
    second_start, second_end = ranges[1].split(",")

    first_numbers = set(number for number in range(int(first_start), int(first_end) + 1))
    second_second = set(number for number in range(int(second_start), int(second_end) + 1))

    current_intersection = first_numbers.intersection(second_second)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")

