def abbrev_name(name):
    words = name.split()
    return f"{words[0][0].upper()}.{words[1][0].upper()}"


print(abbrev_name("Hawaii Pizza"))