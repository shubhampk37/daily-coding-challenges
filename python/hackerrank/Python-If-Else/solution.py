# HackerRank: Python If-Else
# Problem Link: https://www.hackerrank.com/challenges/py-if-else/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0 or (6 <= n <=20):
        print("Weird")
    else:
        print("Not Weird")