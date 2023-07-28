result = {}

for element in input():

    if element not in result:
        result[element] = 0

    result[element] += 1

print('\n'.join([f"{element}: {count} time/s" for element, count in sorted(result.items())]))
