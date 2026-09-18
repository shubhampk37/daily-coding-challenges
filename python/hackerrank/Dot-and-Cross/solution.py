# HackerRank: Dot and Cross
# Problem Link: https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy as np

def main():
    # Dimension of the square matrices
    n = int(input())
    
    # Parse row inputs on the fly and cast them directly into a 2D NumPy array structure
    matrix_a = np.array([list(map(int, input().split())) for _ in range(n)])
    matrix_b = np.array([list(map(int, input().split())) for _ in range(n)])
    
    # Compute the matrix product (equivalently written as matrix_a @ matrix_b)
    result = np.dot(matrix_a, matrix_b)
    
    print(result)

if __name__ == "__main__":
    main()