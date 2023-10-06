def shopping_cart(*args):
    limit_products = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }

    products = {
        "Soup": [],
        "Dessert": [],
        "Pizza": []
    }

    not_products = True

    for el in args:
        if el == "Stop":
            break

        not_products = False
        meal, product = el[0], el[1]
        if product not in products[meal] and len(products[meal]) < limit_products[meal]:
            products[meal].append(product)

    if not_products:
        return "No products in the cart!"

    sorted_products = dict(sorted(products.items(), key=lambda x: (-len(x[1]), x[0])))

    result = []

    for meal, product in sorted_products.items():
        result.append(meal + ":")
        for p in sorted(product):
            result.append(f" - {p}")

    return "\n".join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
