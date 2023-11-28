def add_songs(*args):
    songs = {}
    for el in args:
        if el[0] not in songs:
            songs[el[0]] = el[1]
        else:
            if el[1] != []:
                for i in el[1]:
                    songs[el[0]].append(i)

    result = []
    for song in songs.keys():
        result.append(f"- {song}")
        for t in songs[song]:
            result.append(t)

    return "\n".join(result)


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
