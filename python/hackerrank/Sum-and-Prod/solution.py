# HackerRank: Sum and Prod
# Problem Link: https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy as np


def solve_sum_and_product() -> None:
    """Reads a 2D array, computes the sum along axis 0,

    and then prints the product of that resulting array.
    """
    dimensions = input().split()

    row_count = int(dimensions[0])

    matrix = np.array(
        [list(map(int, input().split())) for _ in range(row_count)], dtype=int
    )

    column_sums = np.sum(matrix, axis=0)
    final_result = np.prod(column_sums)

    print(final_result)


if __name__ == "__main__":
    solve_sum_and_product()

