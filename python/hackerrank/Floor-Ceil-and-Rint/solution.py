# HackerRank: Floor, Ceil and Rint
# Problem Link: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy as np

def main():
    # Set legacy print options to match HackerRank's expected output format
    np.set_printoptions(legacy="1.13")
    
    # Read the space-separated input string and convert it directly to a float array
    my_array = np.array(input().split(), dtype=float)
    
    # Print floor, ceil, and rint element-wise
    print(np.floor(my_array))
    print(np.ceil(my_array))
    print(np.rint(my_array))

if __name__ == "__main__":
    main()