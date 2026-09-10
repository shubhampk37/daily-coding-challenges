# HackerRank: Arrays
# Problem Link: https://www.hackerrank.com/challenges/np-arrays/problem

import numpy

def arrays(arr):
    """Convert to float numpy array and reverse it's sequence"""
    return numpy.array(arr, float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)