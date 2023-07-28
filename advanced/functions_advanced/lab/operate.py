from functools import reduce


def operate(operate, *args):
    operates = {
        "+": reduce(lambda x, y: x + y, args),
        "-": reduce(lambda x, y: x - y, args),
        "*": reduce(lambda x, y: x * y, args),
        "/": reduce(lambda x, y: x / y, args)

    }

    return operates[operate]


print(operate("*", 3, 4))
