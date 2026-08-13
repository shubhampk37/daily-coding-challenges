# HackerRank: DefaultDict Tutorial
# Problem Link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

def solve_defaultdict() -> None:
    """
    Solve the DefaultDict challenge by tracking 1-indexed positions 
    of words from group A and printing occurrences for group B queries.
    """
    # Read n (size of group A) and m (size of group B)
    n, m = map(int, input().split())
    
    # Dictionary to store the 1-based indices of words in group A
    group_a_indices = defaultdict(list)
    
    # Populate group A indices
    for i in range(1, n + 1):
        word = input().strip()
        group_a_indices[word].append(str(i))
        
    # Process group B queries
    for _ in range(m):
        query_word = input().strip()
        if query_word in group_a_indices:
            print(' '.join(group_a_indices[query_word]))
        else:
            print('-1')

if __name__ == '__main__':
    solve_defaultdict()
