from Anagram import are_anagrams


def test_anagram_words():
    assert are_anagrams("listen", "silent")


def test_mixed_case_and_spaces():
    assert are_anagrams("Dormitory", "Dirty room")


def test_different_letters():
    assert not are_anagrams("hello", "world")


def test_different_number_of_letters():
    assert not are_anagrams("listen", "listens")


def test_empty_strings():
    assert are_anagrams("", "")