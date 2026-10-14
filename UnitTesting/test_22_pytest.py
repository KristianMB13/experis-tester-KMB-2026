import pytest
import csv
from Math import *


def load_csv(path):
    with open(path) as file:
        return [tuple(row) for row in csv.reader(file)]

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (10, 100, 110),
    (-1, -2, -3)
])

def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", load_csv("UnitTesting/test_data.csv"))
def test_subtract(a, b, expected):
    assert subtract(int(a), int(b)) == int(expected)
