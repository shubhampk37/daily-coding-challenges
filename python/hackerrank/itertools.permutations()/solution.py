# HackerRank: itertools.permutations()
# Problem Link: https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations 

s, k = input().split()
k = int(k)

sorted_s = "".join(sorted(s))

for perm in permutations(sorted_s, k):
    print("".join(perm))
