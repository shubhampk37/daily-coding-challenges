# HackerRank: Group(), Groups() & Groupdict()
# Problem Link: https://www.hackerrank.com/challenges/re-group-groups/problem

import re

def first_repeating_alnum(string) -> str:
    """
    Finds the first occurrence of an alphanumeric character
    in the string
    """
    
    # ([a-zA-Z0-9]) captures any alphanumeric character into group 1
    # \1+ checks for one or more consecutive repetitions of that exact character
    
    match = re.search(r'([a-zA-Z0-9])\1+', string)
    
    return match.group(1) if match else -1


if __name__ == '__main__':
    string_input = input()
    print(first_repeating_alnum(string_input))