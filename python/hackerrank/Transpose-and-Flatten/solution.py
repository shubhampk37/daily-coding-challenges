# HackerRank: Transpose and Flatten
# Problem Link: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np


def matrix_operations() -> None:
    rows, _ = map(int, input().split()) #Discarding the input for number of columns

    matrix = np.array(
        [list(map(int, input().split())) for _ in range(rows)]
    )

    print(matrix.T)
    print(matrix.flatten())


if __name__ == "__main__":
    matrix_operations()

