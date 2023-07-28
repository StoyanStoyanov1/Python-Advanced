def grocery_store(**kwargs):
    sorted_kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    return "\n".join(f"{key}: {value}" for key, value in sorted_kwargs.items())


print(grocery_store(
 bread=2,
 pasta=2,
 eggs=20,
 carrot=1,
))