# HackerRank: Word Order
# Problem Link: https://www.hackerrank.com/challenges/word-order/problem

import sys
from collections import Counter

def distinct_count() -> None:
    
    input_data = sys.stdin.read().splitlines()
    
    # The first line gives us the number of words 'n'
    n = int(input_data[0])
    
    # all the other words as the input
    words = [word.strip() for word in input_data[1 : n + 1]]
    
    # store the words according to the insertion order and their counts in the words list as well 
    word_counts = Counter(words)
    
    # number of distinct words
    print(len(word_counts))
    
    print(*(word_counts.values()))
    
    
if __name__ == '__main__':
    # n = int(input())
    distinct_count()
    
