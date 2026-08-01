# HackerRank: Text Wrap
# Problem Link: https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

#  Manual Way
    
# def wrap(string, max_width):
#     text_parts = []
    
#     for i in range(0, len(string), max_width):
#         text_parts.append(string[i:i+max_width])
#     return "\n".join(text_parts)

# Extremely quick compared to the Manual Way

def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)