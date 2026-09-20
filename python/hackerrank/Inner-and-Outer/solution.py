# HackerRank: Inner and Outer
# Problem Link: https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy as np


import numpy as np

# Read input arrays
array_a = np.array(list(map(int, input().split())))
array_b = np.array(list(map(int, input().split())))

# Compute and print inner and outer products
print(np.inner(array_a, array_b))
print(np.outer(array_a, array_b))