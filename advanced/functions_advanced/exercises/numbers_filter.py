def even_odd_filter(**kwargs):
    if "even" in kwargs:
        kwargs["even"] = list(filter(lambda x: x % 2 == 0, kwargs["even"]))

    if "odd" in kwargs:
        kwargs["odd"] = list(filter(lambda x: x % 2 != 0, kwargs["odd"]))

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
