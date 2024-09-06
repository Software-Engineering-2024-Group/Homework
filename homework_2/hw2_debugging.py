"""
This module implements the merge sort algorithm. It provides the `merge_sort`
function to sort an array using the merge sort approach with the helper
function `recombine` to merge two sorted arrays.
"""
import rand


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
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


sortedArray = rand.random_array(20)
arr_out = merge_sort(sortedArray)

print(arr_out)
