from Palindrome_Checker import is_palindrome


def test_single_character():
    assert is_palindrome("a")


def test_empty_string():
    assert is_palindrome("")


def test_mixed_case():
    assert is_palindrome("RaceCar")


def test_phrase_with_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama")


def test_non_palindrome():
    assert not is_palindrome("hello")