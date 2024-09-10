import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hw2_debugging import merge_sort

def test_sorted_list():
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]

def test_unsorted_list():
    arr = [5, 3, 8, 4, 2]
    assert merge_sort(arr) == [2, 3, 4, 5, 8]

def test_reverse_sorted_list():
    arr = [9, 7, 5, 3, 1]
    assert merge_sort(arr) == [1, 3, 5, 7, 9]

def test_list_with_duplicates():
    arr = [4, 2, 2, 8, 4]
    assert merge_sort(arr) == [2, 2, 4, 4, 8]
