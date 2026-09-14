# HackerRank: Array Mathematics
# Problem Link: https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np


def perform_array_operations() -> None:
    """Reads two 2D arrays from standard input and prints the results of

    element-wise addition, subtraction, multiplication, integer division,
    modulo, and exponentiation.
    """
    dimensions = input().split()
    
    row_count = int(dimensions[0])

    array_a = np.array(
        [list(map(int, input().split())) for _ in range(row_count)], dtype=int
    )
    array_b = np.array(
        [list(map(int, input().split())) for _ in range(row_count)], dtype=int
    )

    print(array_a + array_b)
    print(array_a - array_b)
    print(array_a * array_b)
    print(array_a // array_b)
    print(array_a % array_b)
    print(array_a**array_b)


if __name__ == "__main__":
    perform_array_operations()

