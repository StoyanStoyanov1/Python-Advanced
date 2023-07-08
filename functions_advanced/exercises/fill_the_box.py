from functools import reduce


def fill_the_box(*args):
    size_box = reduce(lambda x, y: x * y, args[:3])
    total_cubes = sum(args[3:args.index("Finish")])

    if size_box < total_cubes:
        return f"No more free space! You have {total_cubes - size_box} more cubes."
    else:
        return f"There is free space in the box. You could put {size_box - total_cubes} more cubes."


print(fill_the_box(5, 5,
                   2, 40, 11, 7, 3, 1, 5,
                   "Finish"))

print(fill_the_box(2, 8,
                   2, 2, 1, 7, 3, 1, 5,
                   "Finish"))

print(fill_the_box(10, 10,
                   10, 40, "Finish", 2, 15,
                   30))
