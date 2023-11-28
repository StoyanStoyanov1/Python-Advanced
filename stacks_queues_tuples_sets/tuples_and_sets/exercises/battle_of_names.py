odd_sums = set()
even_sums = set()

for count in range(1, int(input()) + 1):
    current_sum = sum([ord(letter) for letter in input()]) // count

    if current_sum % 2 == 0:
        even_sums.add(current_sum)
    else:
        odd_sums.add(current_sum)

if sum(odd_sums) <= sum(even_sums):
    print(*odd_sums.union(even_sums), sep=", ")
else:
    print(*odd_sums.difference(even_sums), sep=", ")
