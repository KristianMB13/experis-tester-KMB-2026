def is_palindrome(text):
    cleaned_text = ""

    for character in text:
        if character.isalnum():
            cleaned_text += character.lower()


    reversed_text = ""
    for character in cleaned_text:
        reversed_text = character + reversed_text

    return cleaned_text == reversed_text