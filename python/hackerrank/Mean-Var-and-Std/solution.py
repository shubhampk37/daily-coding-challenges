# HackerRank: Mean, Var, and Std
# Problem Link: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy as np


def main():
    n_rows, _ = map(int, input().split())
    matrix = np.array([list(map(int, input().split())) for _ in range(n_rows)])

    print(np.mean(matrix, axis=1))
    print(np.var(matrix, axis=0))
    print(round(float(np.std(matrix)), 11))


if __name__ == "__main__":
    main()