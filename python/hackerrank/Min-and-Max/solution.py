# HackerRank: Min and Max
# Problem Link: https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy as np

def main():
    # Read N rows and M columns for the matrix
    row_count, col_count = map(int, input().split())
    
    # Read the array elements and cast them to integers
    matrix = np.array([input().split() for _ in range(row_count)], dtype=int)
    
    # Compute the minimum across columns (axis 0) -> changed to axis 1 per task requirement
    min_column_values = np.min(matrix, axis=1)
    
    # Find and print the maximum value from the resulting minimums
    final_result = np.max(min_column_values)
    print(final_result)

if __name__ == '__main__':
    main()