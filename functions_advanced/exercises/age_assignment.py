def age_assignment(*names, **ages):
    result = []

    for name in names:
        for letter, age in ages.items():
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")
                break

    return "\n".join(sorted(result))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
