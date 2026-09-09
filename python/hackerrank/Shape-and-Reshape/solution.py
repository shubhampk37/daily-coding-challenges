# HackerRank: Shape and Reshape
# Problem Link: https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy as np

def reshape_input_to_matrix(
    raw_input: str, rows: int = 3, cols: int = 3
) -> np.ndarray:
  """Parses a space-separated string of integers and reshapes it

  into a 2D NumPy array of the target dimensions.
  """
  elements = [int(item) for item in raw_input.strip().split()]
  return np.array(elements).reshape((rows, cols))


if __name__ == "__main__":
  input_data = input()
  matrix = reshape_input_to_matrix(input_data)
  print(matrix)