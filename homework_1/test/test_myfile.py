# test/test_myfile.py

import pytest
from myfile import add


def test_add_valid_input():
    assert add(2, 3) == 5


def test_add_fail(): 
    assert not(add(3,2) == 7)
