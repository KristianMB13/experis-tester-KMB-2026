import pytest
from Fizzbuzz import fizz_buzz


def test_one():
    assert fizz_buzz(1) == ["1"]


def test_three():
    assert fizz_buzz(3) == ["1", "2", "Fizz"]


def test_five():
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_fifteen():
    result = fizz_buzz(15)
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"


def test_zero_raises_value_error():
    with pytest.raises(ValueError):
        fizz_buzz(0)


def test_negative_number_raises_value_error():
    with pytest.raises(ValueError):
        fizz_buzz(-1)


def test_non_integer_raises_value_error():
    with pytest.raises(ValueError):
        fizz_buzz(2.5)