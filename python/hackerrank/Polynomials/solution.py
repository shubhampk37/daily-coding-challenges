# HackerRank: Polynomials
# Problem Link: https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy as np

def evaluate_polynomial():
    # Fetching coefficients and the target point from standard input
    coefficients = list(map(float, input().split()))
    evaluation_point = float(input())
    
    # np.polyval is chosen here to evaluate the polynomial efficiently 
    # using Horner's scheme, avoiding manual exponentiation logic.
    result = np.polyval(coefficients, evaluation_point)
    
    print(result)

if __name__ == "__main__":
    evaluate_polynomial()