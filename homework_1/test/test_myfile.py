# test/test_myfile.py
from homework_1.myfile import add


def test_add_valid_input():
    assert add(2, 3) == 5


def test_add_fail():  # correct it
    assert add(3, 2) != 7
