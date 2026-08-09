# HackerRank: Polar Coordinates
# Problem Link: https://www.hackerrank.com/challenges/polar-coordinates/problem

import cmath

z = complex(input())
modulus = abs(z)
phase = cmath.phase(z)
print(modulus, phase, sep = "\n")