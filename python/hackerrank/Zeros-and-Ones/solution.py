# HackerRank: Zeros and Ones
# Problem Link: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy as np


import numpy as np

def create_arrays_from_dimensions(dimensions: tuple[int, ...]) -> None:
    """Creates and prints zero-filled and one-filled NumPy arrays

    of the specified shape with integer data type.
    """
    zero_array = np.zeros(dimensions, dtype=int)
    ones_array = np.ones(dimensions, dtype=int)

    print(zero_array)
    print(ones_array)


if __name__ == "__main__":
    input_dimensions = tuple(map(int, input().split()))
    create_arrays_from_dimensions(input_dimensions)

