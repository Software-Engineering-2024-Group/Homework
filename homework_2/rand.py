"""
This module contains helper functions for generating random data.
"""
import subprocess
import random


def random_array(size):
    """
    This function is used to generate a list of random integers.

    Parameters:
    size(int): Number of integers to generate

    Returns:
    list of int: List containing randomly generated integers.

    """
    arr = [None] * size
    for i in range(size):
        result = subprocess.run(
            ["shuf", "-i1-20", "-n1"],
            capture_output=True,
            text=True,
            check=True)
        arr[i] = int(result.stdout)
    return arr
