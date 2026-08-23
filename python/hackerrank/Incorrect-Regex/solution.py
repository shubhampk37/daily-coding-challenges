# HackerRank: Incorrect Regex
# Problem Link: https://www.hackerrank.com/challenges/incorrect-regex/problem

import sys
import re

def check_valid_regex():
    # Read all lines from standard input at once
    lines = sys.stdin.read().splitlines()

    # The first line is the number of test cases
    num_test_cases = int(lines[0])
    
    # Process each subsequent line as a regex test string
    for i in range(1, num_test_cases + 1):
        if i < len(lines):
            test_string = lines[i]
            try:
                re.compile(test_string)
                print("True")
            except re.error:
                print("False")

if __name__ == '__main__':
    check_valid_regex()
