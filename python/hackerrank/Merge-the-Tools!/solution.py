# HackerRank: Merge the Tools!
# Problem Link: https://www.hackerrank.com/challenges/merge-the-tools/problem

#!/bin/python3

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # Extract the substring of length k
        substring = string[i : i + k]

        # Remove duplicate characters while maintaining the original order
        # dict.fromkeys() preserves insertion order in Python 3.7+
        seen_characters = "".join(dict.fromkeys(substring))
        
        # Print the processed string
        print(seen_characters)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)