def are_anagrams(first_text, second_text):
    first_cleaned = ""
    second_cleaned = ""

    for character in first_text:
        if character.isalnum():
            first_cleaned += character.lower()

    for character in second_text:
        if character.isalnum():
            second_cleaned += character.lower()

    return sorted(first_cleaned) == sorted(second_cleaned)
