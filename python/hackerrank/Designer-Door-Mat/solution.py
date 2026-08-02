# HackerRank: Designer Door Mat
# Problem Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

import textwrap

# Read input
N, M = map(int, input().split())

pattern = ".|."

# Top half
for i in range(N // 2):
    print((pattern * (2 * i + 1)).center(M, "-"))

# Middle
print("WELCOME".center(M, "-"))

# Bottom half
for i in range(N // 2 - 1, -1, -1):
    print((pattern * (2 * i + 1)).center(M, "-"))