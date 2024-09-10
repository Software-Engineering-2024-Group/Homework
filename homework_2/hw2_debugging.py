"""
This module implements the merge sort algorithm. It provides the `merge_sort`
function to sort an array using the merge sort approach with the helper
function `recombine` to merge two sorted arrays.
"""
from homework_2 import rand


def merge_sort(input_arr):
    """
    This function is used to sort an array using the merge sort algorithm.

    Parameters:
    input_arr(list of int): The list of integers to be sorted.

    Returns:
    list of int: A new list containing all integers from arr, sorted
    in ASC order.
    """
    if len(input_arr) == 1:
        return input_arr

    half = len(input_arr)//2

    left_sorted = merge_sort(input_arr[:half])
    right_sorted = merge_sort(input_arr[half:])

    return recombine(left_sorted, right_sorted)


def recombine(left_arr, right_arr):
    """
    This helper function is used to merge two sorted arrays
    into a single sorted array.

    Parameters:
    left_arr (list of int): The first sorted list.
    right_arr (list of int): The second sorted list.

    Returns:
    list of int: A new list containing all elements from left_arr
    and right_arr, sorted in ASC order.
    """
    left_index = 0
    right_index = 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    # Append remaining elements from left_arr, if any
    while left_index < len(left_arr):
        merge_arr.append(left_arr[left_index])
        left_index += 1

    # Append remaining elements from right_arr, if any
    while right_index < len(right_arr):
        merge_arr.append(right_arr[right_index])
        right_index += 1

    return merge_arr


unsorted_array = rand.random_array(20)
print("original array: ", unsorted_array)
sorted_array = merge_sort(unsorted_array)

print(sorted_array)
