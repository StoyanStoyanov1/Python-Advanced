from collections import deque


def forecast(*args):
    locations = {}
    weather = deque(["Sunny", "Cloudy", "Rainy"])

    for date in args:
        if date[1] not in locations:
            locations[date[1]] = []

        locations[date[1]].append(date[0])

    result = []

    while weather:
        current_weather = weather.popleft()
        if current_weather in locations:
            for location in sorted(locations[current_weather]):
                result.append(f"{location} - {current_weather}")

    return "\n".join(result)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print()

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print()

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))