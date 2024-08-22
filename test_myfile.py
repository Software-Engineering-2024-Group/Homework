# test_myfile.py
from myfile import add, div


def test_add_valid_input():
    assert add(2, 3) == 5


def test_div_by_zero():
    assert div(0, 0) == 0
