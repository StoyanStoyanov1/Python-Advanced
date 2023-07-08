def concatenate(*args, **kwargs):
    text = "".join(args)

    for key, word in kwargs.items():
        text = text.replace(key, word)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!",
UNI="Uni", Grate="Great"))