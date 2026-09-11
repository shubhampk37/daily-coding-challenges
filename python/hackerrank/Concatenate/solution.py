# HackerRank: Concatenate
# Problem Link: https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np

def solve_concatenation() -> None:
    try:
        first_line = input().split()
        if not first_line:
            return
        n, m, p = map(int, first_line)
    except EOFError:
        return
        
    # read n lines for the first array
    array_1_data = [list(map(int, input().split())) for _ in range(n)]
    
    # Read m lines for the second array
    array_2_data = [list(map(int, input().split()))
    for _ in range(m)]
    
    array_1 = np.array(array_1_data)
    array_2 = np.array(array_2_data)
    
    concatenated_array = np.concatenate((array_1, array_2), axis=0)
    
    print(concatenated_array)    

if __name__ == '__main__':
    solve_concatenation()

